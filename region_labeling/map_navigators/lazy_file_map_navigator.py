from .map_navigator import MapNavigator
from ..config import Config

class LazyFileMapNavigator(MapNavigator):
    def __init__(self, abs_file_path):
        self.__abs_file_path = abs_file_path
        # validation might slow things down, so let's make it configurable
        if Config.validate:
            self.__validate()
        self.__cursor_x = -1
        self.reset()
        self.__map_file = None
        self.__ctx = None
        self.__width = None
        self.__eof_reached = False

    def __enter__(self):
        self.__map_file = open(self.__abs_file_path, "r")
        self.__load_ctx()
        # TODO it's assumed that there's some content in the file!
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

        if x == 0:
            r1[0] = 0
            r2[0] = 0
        if x == self.__width - 1:
            r1[-1] = 0

        r1 = [r1[0] if r1[0] is not None else self.__ctx[0][x - 1],
              r1[1] if r1[1] is not None else self.__ctx[0][x],
              r1[2] if r1[2] is not None else self.__ctx[0][x + 1]]
        r2 = [r2[0] if r2[0] is not None else self.__ctx[1][x - 1],
              r2[1] if r2[1] is not None else self.__ctx[1][x]]

        return [r1, r2]

    def __validate(self):
        # TODO add validation
        return True

    def update_current_element(self, val):
        self.__ctx[1][self.__cursor_x] = val

    def reset(self):
        # resets the internal pointer only, not the file pointer
        self.__cursor_x = -1  # one element behind so we can start iterating without a need for do...while
