import itertools

def my_permutatins(iterable):
    def on_index(iterable, helper):
        return tuple(iterable[i] for i in helper)

    if len(iterable) <= 1:
        return
    helper = range(len(iterable))
    yield on_index(iterable, helper)
    while True:
        i, j = len(helper) - 2, len(helper) - 1
        while helper[i] > helper[i + 1]:
            i -= 1
        if i == -1:
            return
        while helper[j] < helper[i]:
            j -= 1
        helper[i], helper[j] = helper[j], helper[i]
        helper[i + 1:] = reversed(helper[i + 1:])
        yield on_index(iterable, helper)

test_data = [[1,2,3], [], ['a','b','c','d'], [1]]
for data in test_data:
    print 'data=%s' % data
    print list(itertools.permutations(data))
    print list(my_permutatins(data))