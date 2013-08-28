import heapq

'''Library funciton heapq.merge does the same thing: 
print list(heapq.merge([1,3,45], [2,9,11,50], [15,18,19]))
'''

def merge_k_lists(*iterables):
    heap = []
    m = map(iter, iterables)
    for it in m:
        try:
            heap.append([it.next(), it])
        except StopIteration:
            pass
    heapq.heapify(heap)
    while 1:
        try:
            val, it = s = heap[0]
            yield val
            s[0] = it.next()
            heapq.heapreplace(heap, s)
        except StopIteration:
            heapq.heappop(heap)
        except IndexError:
            return

# print merge_k_lists([[1,3,45], [2,9,11,50], [15,18,19]])
# print list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
print list(merge_k_lists([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))