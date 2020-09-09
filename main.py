# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class RangeRegion(object):
    def __init__(self, l, r):
        self.r = range(l, r+1)
        self.region_id = -1

def sum_up_to_continuous_range(range_in_row, range_in_next_row):
    return len(range(min(range_in_row.r[0], range_in_next_row.r[0]),
                     max(range_in_row.r[-1], range_in_next_row.r[-1]))) == len(range_in_row.r) + len(range_in_next_row.r)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    z = []
    a = [RangeRegion(1,1)]
    b = [RangeRegion(0,2), RangeRegion(6,6)]
    c = [RangeRegion(0,1), RangeRegion(5,7)]
    d = [RangeRegion(5,6)]
    e = [RangeRegion(2,2)]
    f = [RangeRegion(2, 2)]
    rr = [z,a,b,c,d,e,f]
    next_region_id = 1
    for row_idx in range(len(rr) - 1):
        if len(rr[row_idx]) == 0:
            continue
        for range_in_row in rr[row_idx]:
            if range_in_row.region_id == -1:
                range_in_row.region_id = next_region_id
                next_region_id = next_region_id + 1
            for range_in_next_row in rr[row_idx + 1]:
                if range_in_row.r in range_in_next_row.r or range_in_next_row.r in range_in_row.r:
                    range_in_next_row.region_id = range_in_row.region_id
                elif sum_up_to_continuous_range(range_in_row, range_in_next_row):
                    range_in_next_row.region_id = range_in_row.region_id



    print(r)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
