from collections import Counter
def get_smallest(s):
    cnt = Counter(s)
    require = {k:int(v/2) for k,v in cnt.items()}
    remain = dict(cnt)
    s = s[::-1]
    res = []

    def can_pop(c):
        return require[c] + 1 <= remain[c]

    for c in s:
        if require[c] > 0:

            while res and res[-1] > c and can_pop(res[-1]):
                pc = res.pop()
                require[pc] += 1

            res.append(c)
            require[c] -= 1

        remain[c] -= 1

    return ''.join(res)

