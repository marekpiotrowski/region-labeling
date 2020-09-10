from .map_navigator import MapNavigator
from ..config import Config


class LazyFileMapNavigator(MapNavigator):
    """
    Class representing LazyFileMapNavigator, where 2d map of islands is given via filepath.
    The file is read sequentially and is being loaded in chunks (2 rows at a time).
    The file shall remain opened throught the whole execution. Class should close the file handle in case something
    goes wrong (assuming it's being used via context manager!).

    cursor_y is missing in this case, as the "context" will always contain row being analyzed and the row above. y will
    be relative to current context.

    ...

    Attributes
    ----------
        __cursor_x : int
            Pointer to currently analysed pixel in "x" axis
        __width : int
            Number of elements in each row. Initialized after first context load.
        __map_file : FileHandle
            Handle to the map file.
        __ctx: two-element list of integers
            Two-element list containing currently analyzed row at idx = 1 and row above at idx = 0, already parsed
            as a list of integers.
        __eof_reached: boolean
            Flag used to denoted that we're done with the file. EOF is reached when reading last line, so we cannot
            return immediately.

    Methods
    -------
        Please see MapNavigator specification.
    """
    def __init__(self, abs_file_path):
        self.__abs_file_path = abs_file_path
        # validation might slow things down, so let's make it configurable
        if Config.validate:
            self.__validate()
        self.__cursor_x = -1
        self.__map_file = None
        self.__ctx = None
        self.__width = None
        self.__eof_reached = False

    def __enter__(self):
        self.__map_file = open(self.__abs_file_path, "r")
        self.__load_ctx()
        # it's assumed that there's some content in the file!
        self.__width = len(self.__ctx[0])
        return self

    def __exit__(self, type, value, traceback):
        if self.__map_file:
            self.__map_file.close()

    def __load_ctx(self):
        self.__ctx = [[], []]
        while True:
            c = self.__map_file.read(1)
            if c is '\n':
                break
            self.__ctx[1].append(int(c))
            # first row, so prepend with 0s
            self.__ctx[0].append(0)

    def __reload_ctx(self):
        # when loading next line, line which has already been analyzed should be swapped (and become the "row above")
        # all modifications should be persisted, at least between the context is fully switched
        self.__ctx[0] = self.__ctx[-1]
        self.__ctx[1] = []
        while True:
            c = self.__map_file.read(1)
            if c is '\n':
                break
            if c is '':  # EOF
                self.__eof_reached = True
                break
            self.__ctx[1].append(int(c))

    def move_right_with_wrapping(self):
        # we are ar right-most idx and EOF reached when loading the line:
        if self.__cursor_x == self.__width - 1 and self.__eof_reached:
            return False

        if self.__cursor_x == self.__width - 1:
            self.__reload_ctx()
            self.__cursor_x = 0
            return True

        self.__cursor_x = self.__cursor_x + 1
        return True

    def get_neighborhood(self):
        '''
        Returns row above and row of the pixel being analysed without last element (as jagged array):
        [N2, N3, N4]
        [N1, X]
        :return:
        '''
        x = self.__cursor_x
        r1 = [None, None, None]
        r2 = [None, None]

        # in case we're at left-most index, pad the neighborhood array with 0s to the left
        if x == 0:
            r1[0] = 0
            r2[0] = 0
        # in case we're at right-most index, pad the right-most neighbor element with 0 to the right
        if x == self.__width - 1:
            r1[-1] = 0

        r1 = [r1[0] if r1[0] is not None else self.__ctx[0][x - 1],
              r1[1] if r1[1] is not None else self.__ctx[0][x],
              r1[2] if r1[2] is not None else self.__ctx[0][x + 1]]
        r2 = [r2[0] if r2[0] is not None else self.__ctx[1][x - 1],
              r2[1] if r2[1] is not None else self.__ctx[1][x]]

        return [r1, r2]

    def __validate(self):
        try:
            file_for_validation = open(self.__abs_file_path, "r")
        except:
            raise Exception("Problem opening the map file.")
        else:
            lines = [line.strip() for line in file_for_validation.readlines()]
            # TODO clarify if empty file should yield 0 regions or throw an error!
            if not lines:
                raise Exception("Map file is empty.")
            for line in lines:
                try:
                    # if it consists of 1s and 0s, we should be able to parse it to a number in binary
                    number = int(line, 2)
                except ValueError:
                    raise Exception("Incorrect entries in map file.")
            file_for_validation.close()
        return True

    def update_current_element(self, val):
        self.__ctx[1][self.__cursor_x] = val
