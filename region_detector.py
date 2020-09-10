class RegionDetector(object):
    def __init__(self, map_navigator):
        self.map_navigator = map_navigator

    def __get_labels_from_neighborhood(self, neighborhood):
        result = []
        for el in neighborhood[0]:
            if el is not 0:
                result.append(el)
        if neighborhood[1][0] is not 0:
            result.append(neighborhood[1][0])
        return list(set(result))  # let's get rid of duplicates

    # def __is_land(self, neighborhood, x, y):
    #     return neighborhood[y][x] == 1

    def label_regions(self):
        # algorithm description: https://web.cs.wpi.edu/~emmanuel/courses/cs545/S14/slides/lecture08.pdf
        # data should be validated earlier!
        self.map_navigator.reset()
        next_region_id = 2
        graph = {}
        while self.map_navigator.move_right_with_wrapping():
            neighborhood = self.map_navigator.get_neighborhood()
            if neighborhood[1][1] == 1: #self.__is_land(neighborhood, 1, 1):
                labels_around = self.__get_labels_from_neighborhood(neighborhood)
                print(labels_around)
                if not labels_around:
                    graph[next_region_id] = []
                    self.map_navigator.update_current_element(next_region_id)
                    next_region_id = next_region_id + 1
                elif len(labels_around) is 1:
                    self.map_navigator.update_current_element(labels_around[0])
                else:
                    # due to sequential nature of algorithm, we can safely assume that labels_around can have up to 2 elements
                    graph[min(labels_around)].append(max(labels_around))
                    self.map_navigator.update_current_element(min(labels_around))
        # self.__remove_child_nodes(graph)
        print(graph)
