def merge(intervals):
    sorted_inv = sorted(intervals, key=lambda x: x[0])
    rt = []
    for inv in sorted_inv:
        if not rt or inv[0] > rt[-1][1]:
            rt.append(inv)
        elif inv[0] <= rt[-1][1]:
            rt[-1][1] = max(rt[-1][1], inv[1])
    return rt


intervals = [[15,18],[2,6],[1,3],[8,10]]
assert(merge(intervals) == [[1,6],[8,10],[15,18]])