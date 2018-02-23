from collections import namedtuple, deque, defaultdict, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'], dd['key2'])

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
