d = {'a': 1, 'b': 2, 'c': 3}
print(d.get('a'))

things = {1, 10, 20, 1, 10}
things.add(20)
print(len(things))

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print([v + 1 for v in d.values() if v < 3])

a = {1, 2, 3, 4}
b = {2, 4, 6}
print(a - b)
print(a ^ b)


d = {'a': 3, 'b': 2, 'c': 1}
for k in sorted(list(d.keys())):
    print(k, d[k], sep='', end='')

print("")
d = {'a': 1, 'b': 2, 'c': 3}
print(d.get(2))


