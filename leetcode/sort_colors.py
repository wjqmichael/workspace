def sort_colors(a):
    r, w, b = 0, 0, len(a) - 1
    while w <=å b:
        if a[w] == 0:
            a[w], a[r] = a[r], a[w]
            r += 1
            w += 1
        elif a[w] == 2:
            a[w], a[b] = a[b], a[w]
            b -= 1
        else:
            w += 1
    return a

print sort_colors([])
print sort_colors([0, 0, 0])
print sort_colors([1, 1, 1])
print sort_colors([2, 2, 2])

print sort_colors([0,1,1,1,2,2,2,2])
print sort_colors([1,0,2,2,2,1,0,0,1])
print sort_colors([1,0,2,2,2,1,0,0])