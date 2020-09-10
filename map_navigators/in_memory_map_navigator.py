from .map_navigator import MapNavigator
from config import Config


class InMemoryMapNavigator(MapNavigator):
    def __init__(self, map_2d_array):
        self.__cursor_x = 0
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
        '''
        Always returns 3x3 neighbourhood, where res[1][1] is currently analysed pixel. On the edges, map is extended with 0s.
        :return:
        '''
        y = self.__cursor_y
        x = self.__cursor_x
        r1 = [None, None, None]
        r2 = [None, None, None]
        r3 = [None, None, None]

        if y == 0:
            r1 = [0, 0, 0]
        if x == 0:
            r1[0] = 0
            r2[0] = 0
            r3[0] = 0
        if y == self.__height - 1:
            r3 = [0, 0, 0]
        if x == self.__width - 1:
            r1[-1] = 0
            r2[-1] = 0
            r3[-1] = 0

        r1 = [r1[0] if r1[0] is not None else self.__map[y - 1][x - 1],
              r1[1] if r1[1] is not None else self.__map[y - 1][x],
              r1[2] if r1[2] is not None else self.__map[y - 1][x + 1]]
        r2 = [r2[0] if r2[0] is not None else self.__map[y][x - 1],
              r2[1] if r2[1] is not None else self.__map[y][x],
              r2[2] if r2[2] is not None else self.__map[y][x + 1]]
        r3 = [r3[0] if r3[0] is not None else self.__map[y + 1][x - 1],
              r3[1] if r3[1] is not None else self.__map[y + 1][x],
              r3[2] if r3[2] is not None else self.__map[y + 1][x + 1]]

        return [r1, r2, r3]

    def __validate(self):
        return True