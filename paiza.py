N, R = map(int, input().split())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_touched(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2 <= (2*R)**2


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # 　探索していった過程で親をできるだけ更新
        return self.parent[p]

    def unite(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

    # 木が深くならないようにしている。
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1


points = [Point(*map(int, input().split())) for _ in range(N)]
uf = UnionFind(N)

for i in range(N):
    for j in range(i+1, N):
        if points[i].is_touched(points[j]):
            uf.unite(i, j)

result = set()
for i in range(N):
    result.add(uf.find(i))

print(len(result))
