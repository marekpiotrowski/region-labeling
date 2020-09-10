from .map_navigator import MapNavigator
from config import Config


class InMemoryMapNavigator(MapNavigator):
    def __init__(self, map_2d_array):
        self.reset()
        self.__map = map_2d_array
        # validation might slow things down, so let's make it configurable
        if Config.validate:
            self.__validate()
        self.__width = len(self.__map[0])
        self.__height = len(self.__map)
        print("H: {}, W: {}".format(self.__height, self.__width))

    def move_right_with_wrapping(self):
        # print("x: {}, y: {}".format(self.__cursor_x, self.__cursor_y))
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
        Returns row above and row of the pixel being analysed without last element (as jagged array):
        [N2, N3, N4]
        [N1, X]
        :return:
        '''
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
        return True

    def update_current_element(self, val):
        self.__map[self.__cursor_y][self.__cursor_x] = val
        # print(self.__map)

    def reset(self):
        # resets the pointer only, not the map itself
        self.__cursor_x = -1  # one element behind so we can start iterating without a need for do...while
        self.__cursor_y = 0
