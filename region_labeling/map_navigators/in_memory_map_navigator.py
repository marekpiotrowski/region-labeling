from .map_navigator import MapNavigator
from ..config import Config


class InMemoryMapNavigator(MapNavigator):
    """
    Class representing InMemoryMapNavigator, where 2d map of islands is given as a 2d list.

    ...

    Attributes
    ----------
        __cursor_x : int
            Pointer to currently analysed pixel in "x" axis
        __cursor_y : int
            Pointer to currently analysed pixel in "y" axis
        __width : int
            Number of elements in each row.
        __height : int
            Number of elements in each column.
        __map: list of lists of ints
            The "in-memory" 2d array representation of the map.

    Methods
    -------
        Please see MapNavigator specification.
    """
    def __init__(self, map_2d_array):
        self.__cursor_x = -1
        self.__cursor_y = 0
        self.__map = map_2d_array
        # validation might slow things down, so let's make it configurable
        if Config.validate:
            self.__validate()
        self.__width = len(self.__map[0])
        self.__height = len(self.__map)

    def move_right_with_wrapping(self):
        if self.__cursor_y == self.__height - 1 and self.__cursor_x == self.__width - 1:
            return False

        if self.__cursor_x == self.__width - 1:
            self.__cursor_x = 0
            self.__cursor_y = self.__cursor_y + 1
            return True

        self.__cursor_x = self.__cursor_x + 1
        return True

    def get_neighborhood(self):
        y = self.__cursor_y
        x = self.__cursor_x
        r1 = [None, None, None]
        r2 = [None, None]

        if y == 0:
            r1 = [0, 0, 0]
        if x == 0:
            r1[0] = 0
            r2[0] = 0
        if x == self.__width - 1:
            r1[-1] = 0

        r1 = [r1[0] if r1[0] is not None else self.__map[y - 1][x - 1],
              r1[1] if r1[1] is not None else self.__map[y - 1][x],
              r1[2] if r1[2] is not None else self.__map[y - 1][x + 1]]
        r2 = [r2[0] if r2[0] is not None else self.__map[y][x - 1],
              r2[1] if r2[1] is not None else self.__map[y][x]]

        return [r1, r2]

    def __validate(self):
        # TODO add validation
        # let's skip it for in-memory array for now
        return True

    def update_current_element(self, val):
        self.__map[self.__cursor_y][self.__cursor_x] = val

