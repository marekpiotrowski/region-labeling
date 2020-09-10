# from .map_navigators.in_memory_map_navigator import InMemoryMapNavigator
# from .region_detector import RegionDetector
#
# if __name__ == '__main__':
#     # map_navigator = InMemoryMapNavigator([[1, 1, 0, 0, 1], [0, 1, 0, 0, 1], [1, 0, 0, 0, 0]])
#     # rd = RegionDetector(map_navigator)
#     # rd.count_regions()
#
#     # mn1 = InMemoryMapNavigator([[0, 0, 0, 0, 0, 0, 0, 0, 0],
#     #                             [0, 1, 0, 0, 0, 0, 0, 0, 0],
#     #                             [1, 1, 1, 0, 0, 0, 1, 0, 0],
#     #                             [1, 1, 0, 0, 0, 1, 1, 1, 0],
#     #                             [0, 0, 0, 0, 0, 1, 1, 0, 0],
#     #                             [0, 0, 1, 0, 0, 0, 0, 0, 0],
#     #                             [1, 1, 0, 0, 0, 0, 0, 0, 0],
#     #                             [0, 0, 0, 0, 0, 1, 1, 0, 0]])
#     # rd1 = RegionDetector(mn1)
#     # print(rd2.count_regions())
#
#     mn2 = InMemoryMapNavigator([[1, 0, 1, 0, 1],
#                                 [0, 1, 0, 1, 0],
#                                 [1, 0, 1, 0, 1],
#                                 [0, 1, 0, 1, 0],
#                                 [1, 0, 1, 0, 1]])
#     rd2 = RegionDetector(mn2)
#     print(rd2.count_regions())

dim = 1000
f = open('test.txt', 'w+')
for i in range(dim):
    row = []
    for j in range(dim):
        f.write(str((j + ((i + 1) % 2)) % 2))
    f.write('\n')
f.close()
