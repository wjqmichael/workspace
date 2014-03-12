def simplify_path(path):
    parsed = filter(lambda x: x, path.split('/'))
    if not len(parsed):
        return '~'
    rt = ['.']
    for i in parsed:
        if i == '.': 
            continue
        if i == '..':
            rt.pop()
            continue
        rt.append(i)
    if len(rt) > 1:
        rt.pop(0)
    return '/' + '/'.join(rt)

print simplify_path('/home/')
print simplify_path('/a/./b/../../c/')