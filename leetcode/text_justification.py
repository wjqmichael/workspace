def full_justify(words, L):
    def format_line(line, cc):
        if len(line) == 1:
            return line[0]
        space = (L - cc) / (len(line) - 1) + 1
        rmd = (L - cc) % (len(line) - 1)
        rt = line[0]
        for i in xrange(1, len(line)):
            rt += ' ' * space
            if rmd:
                rt += ' '
                rmd -= 1
            rt += line[i]
        return rt

    rt = []
    line = []
    cc = 0
    i = 0
    while i < len(words):
        cc = len(words[i])
        line.append(words[i])
        i += 1
        while i < len(words) and cc + 1 + len(words[i]) <= L:
            cc += (len(words[i]) + 1)
            line.append(words[i])
            i += 1
        rt.append(format_line(line, cc))
        line = []
        cc = 0
    return rt 


words = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16
rt = full_justify(words, L)
for i in rt:
    print i
