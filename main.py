from map_navigators.in_memory_map_navigator import InMemoryMapNavigator

if __name__ == '__main__':
    map_navigator = InMemoryMapNavigator([[1, 1, 0, 0, 1], [0, 1, 0, 0, 1], [1, 0, 0, 0, 0]])
    print(map_navigator.get_neighborhood())
    map_navigator.move_right_with_wrapping()
    print(map_navigator.get_neighborhood())
