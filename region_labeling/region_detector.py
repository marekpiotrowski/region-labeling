class RegionDetector(object):
    """
    Class representing RegionDetector.

    ...

    Attributes
    ----------
        __map_navigator : instance of class implementing MapNavigator interface
            Map navigator instance used for map traversal.

    Methods
    -------
        count_regions():
            Returns number of regions ("islands") within a "map" traversable via injected map_navigator
    """
    def __init__(self, map_navigator):
        """
        Constructs RegionDetector with given MapNavigator implementation.

        Parameters
        ----------
            map_navigator : instance of class implementing MapNavigator interface
                map navigator which will be used for map traversal
        """
        self.__map_navigator = map_navigator

    @staticmethod
    def __remove_duplicates(original_list):
        return list(set(original_list))

    @staticmethod
    def __get_labels_in_the_neighborhood(neighborhood):
        result = []
        # all 3 neighbors above are checked...
        for el in neighborhood[0]:
            if el is not 0 and el not in result:
                result.append(el)
        # ...and the one to the left of currently analysed pixed
        if neighborhood[1][0] is not 0 and neighborhood[1][0] not in result:
            result.append(neighborhood[1][0])
        return result

    @staticmethod
    def __remove_nodes_with_parent(graph):
        nodes_with_parent = []
        for children in graph.values():
            # if a node has some children, let's collect them...
            nodes_with_parent = nodes_with_parent + children
        nodes_with_parent = RegionDetector.__remove_duplicates(nodes_with_parent)
        # ...and remove, as these regions might be merged with 'parent'
        for n in nodes_with_parent:
            del graph[n]

    def count_regions(self):
        """
        Counts regions (or "islands") within a map traversable via injected map navigator.
        Full algorithm description with pictures: https://web.cs.wpi.edu/~emmanuel/courses/cs545/S14/slides/lecture08.pdf

        IMPORTANT! The method will mutate the map_navigator provided, so it's better to assume that the object will be
        no longer valid (neither detector, nor the map_navigator) TODO possibly could re-factor it in the future
        If there's such need, please construct new objects.

        Returns
        -------
            number_of_regions (int): Number of regions (or "islands") within the map.
        """
        # it's assumed that data is validated earlier in the navigator
        next_region_id = 2
        # let's model graph with a dictionary
        graph = {}
        while self.__map_navigator.move_right_with_wrapping():
            neighborhood = self.__map_navigator.get_neighborhood()
            if neighborhood[1][1] == 1:  # TODO possibly wrap in some __is_land(...)
                labels_around = self.__get_labels_in_the_neighborhood(neighborhood)
                if not labels_around:
                    graph[next_region_id] = []
                    self.__map_navigator.update_current_element(next_region_id)
                    next_region_id = next_region_id + 1
                elif len(labels_around) is 1:
                    self.__map_navigator.update_current_element(labels_around[0])
                else:
                    # due to sequential nature of algorithm, we can safely assume that
                    # labels_around can have up to 2 elements
                    graph[min(labels_around)].append(max(labels_around))
                    self.__map_navigator.update_current_element(min(labels_around))
        self.__remove_nodes_with_parent(graph)
        return len(graph.keys())
