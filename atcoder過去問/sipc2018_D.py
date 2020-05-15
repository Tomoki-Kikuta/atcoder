import heapq
INF = 10 ** 16


def dijkstra(n, town, k, start):
    d = []
    queue = []
    for i in range(n):
        d.append(INF)
    d[start] = 0
    heapq.heappush(queue, (0, start))
    # 都市kで交換した時の円またはスヌークのの最小値
    while len(queue) != 0:
        distance, v = heapq.heappop(queue)
        if d[v] < distance:
            continue
        for u in range(len(town[v])):
            if d[town[v][u][0]] > d[v] + town[v][u][k]:
                d[town[v][u][0]] = d[v] + town[v][u][k]
                heapq.heappush(queue, (d[town[v][u][0]], town[v][u][0]))

    return d


def main():
    n, m, s, t = map(int, input().split())
    s -= 1
    t -= 1
    money = 10 ** 15
    town = []

    for i in range(n):
        town.append([])
    for i in range(m):
        fro, to, a, b = map(int, input().split())
        fro -= 1
        to -= 1
        town[fro].append((to, a, b))
        town[to].append((fro, a, b))

    a = dijkstra(n, town, 1, s)
    b = dijkstra(n, town, 2, t)

    total = []
    for i in range(n):
        heapq.heappush(total, (a[i] + b[i], i + 1))
    mon, year = heapq.heappop(total)
    for i in range(n):
        while year <= i:
            mon, year = heapq.heappop(total)
        print(money - mon)


if __name__ == '__main__':
    main()
