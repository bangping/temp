def find_pos(s, pos, c):
    end = len(s)
    for i in pos[::-1]:
        for j in range(i + 1, end):
            if c == s[j]:
                return j
        end = min(i, end)

def get_smallest(s):
    cnt = Counter(s)
    halfcnt = Counter({k:int(v/2) for k,v in cnt.items()})
    keyseq = sorted(halfcnt.elements())
    pos = [0]
    s = list(reversed(s))
    selected = []

    for key in keyseq:
        # find key as per order of pos
        idx = find_pos(s, pos, key)
        pos.append(idx)
        selected.append((idx, s[idx]))
        s[idx] = '_'

    return ''.join([t[1] for t in sorted(selected, key=lambda i: i[0])])
