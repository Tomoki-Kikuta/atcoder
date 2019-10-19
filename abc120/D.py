def make_union_find(N):
    union_find = []
    rank = []
    for i in range(N):
        union_find.append(i)
        rank.append(1)
    return union_find, rank


def find(v, union_find):
    if union_find[v] != v:
        union_find[v] = find(union_find[v], union_find)
        return union_find[v]
    else:
        return union_find[v]


def unite(union_find, rank, a, b, parent_a, parent_b):
    if rank[parent_a] > rank[parent_b]:
        union_find[b] = parent_a
        rank[parent_b] += rank[parent_a]
    elif rank[parent_a] < rank[parent_b]:
        union_find[a] = parent_b
        rank[parent_a] += rank[parent_b]
    else:
        union_find[a] = parent_b
        rank[parent_b] += rank[parent_a]


def main():
    N, M = map(int, input().split())
    combination = []
    ans = []
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        combination.append((a, b))
    ans.append(int(N * (N - 1) / 2))
    union_find, rank = make_union_find(N)
    for i in range(M-1, -1, -1):
        a, b = combination[i]
        parent_a = find(a, union_find)
        parent_b = find(b, union_find)
        if parent_a == parent_b:
            ans.append(ans[-1])
        else:
            ans.append(ans[-1] - rank[parent_a] * rank[parent_b])
            unite(union_find, rank, a, b, parent_a, parent_b)
    for i in range(M - 1, -1, -1):
        print(ans[i])


if __name__ == "__main__":
    main()
