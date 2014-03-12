def insert_interval(intervals, new_interval):
    i = 0
    rt = []
    while i < len(intervals) and new_interval[0] > intervals[i][1]:
        rt.append(intervals[i])
        i += 1
    while i < len(intervals) and new_interval[1] >= intervals[i][0]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    rt.append(new_interval)
    while i < len(intervals):
        rt.append(intervals[i])
        i += 1
    return rt

assert(insert_interval([[1,3],[6,9]], [2,5]) == [[1,5], [6,9]])
assert(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]) == [[1,2],[3,10],[12,16]])