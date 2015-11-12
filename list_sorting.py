from collections import defaultdict

lines = list(open('./rubbish.txt').read())

def least(xs, top=20):
    counts = defaultdict(int)
    for x in xs:
        counts[x] += 1
    return sorted(counts.items(), reverse=False, key=lambda tup: tup[1])[:top]

print least(lines)
