fh = open('1.txt')
manifold = set()
for line in fh:
    manifold = manifold.union(list(line))
print(manifold)