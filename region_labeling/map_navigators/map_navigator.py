from abc import ABC, abstractmethod


class MapNavigator(ABC):
    @abstractmethod
    def move_right_with_wrapping(self):
        """
        Moves the navigator's pointer to next pixel for analysis on the image. In case there's no next element,
        navigator's pointer should wrap to next row and start from the left-hand side.

        IMPORTANT! Client should assume that as a side effect, the method will supposedly mutate the navigator object!

        Returns
        -------
            None
        """
        pass

    @abstractmethod
    def get_neighborhood(self):
        """
        Returns least required neighborhood for a given pixel as a jagged array.
        Eg, given such map, where current element is denoted by 'X':
        01001
        1X011
        Method shall return [[0,1,0], [1,X]]
        It's assumed that currently analyzed pixel will be at [1][1].

        Returns
        -------
            neighborhood (jagged array/list of ints): Nearest pixel's neighborhood.
        """
        pass

    @abstractmethod
    def update_current_element(self, val):
        """
        Method gives possibility to update map contents. Functionality will vary between implementations, but in case of
        "in-memory" map, the list will be mutated. In case of "file-map", only the "context" will be mutated
        (for reference on what's the "context", please see lazy_file_map_navigator.py).

        IMPORTANT! Client should assume that as a side effect, the method will supposedly mutate the navigator object,
        as well as the original map!

        Returns
        -------
            None
        """
        pass
