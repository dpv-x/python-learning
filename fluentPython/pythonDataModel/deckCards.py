import collections as cols

Cards = cols.namedtuple('Card', ['rank', 'suit'])

print(Cards)


ranks = [str(n) for n in range(2, 11)] + list('JQKA')

for n in ranks:
    print(n)

print(ranks)
