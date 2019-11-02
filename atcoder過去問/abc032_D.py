import bisect
MAX = 1000

def make_combination(harf, weight, value, W):
    combination = []
    for i in range(1 << harf):
        w, v = 0, 0
        for j in range(harf):
            if i >> j & 1:
                w += weight[j]
                v += value[j]
        combination.append([w, v])

    combination.sort()
    pre_v = -1
    for i in range(len(combination)):
        v = combination[i][1]
        if pre_v > v:
            combination[i][1] = pre_v
        pre_v = v
    return combination


def cal_max_weight(N, harf, combination, weight, value, W):
    ans = 0
    for i in range(1 << N - harf):
        w, v = 0, 0
        for j in range(N - harf):
            if i >> j & 1:
                w += weight[harf + j]
                v += value[harf + j]
        if w <= W:
            left = 0
            right = len(combination) - 1
            count = 0
            while count < 100:
                mid = (left + right) // 2
                if combination[mid][0] + w <= W:
                    ans = max(ans, v + combination[mid][1])
                    left = mid + 1
                else:
                    right = mid - 1
                count += 1

    return ans


def weight_dp(N, weight, value, W):
    dp = []
    for i in range(N+1):
        dp.append([])
        for j in range(MAX * N + 1):
            dp[i].append(0)
        
    for i in range(1, N + 1):
        for j in range(1, MAX * N + 1):
            if weight[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    if W > MAX * N:
        return dp[N][-1]
    else:
        return dp[N][W]


def value_dp(N, weight, value, W):
    INF = 10 ** 9 + 1
    dp = []
    ans = 0
    for i in range(N+1):
        dp.append([])
        for j in range(MAX * N + 1):
            if j == 0:
                dp[i].append(0)
            else:
                dp[i].append(INF)

    for i in range(1, N + 1):
        for j in range(1, MAX * N + 1):
            if value[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - value[i - 1]] + weight[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    for i in range(1, MAX * N + 1):
        if dp[N][i] <= W:
            ans = i
    return ans


def main():
    N, W = map(int, input().split())
    value = []
    weight = []
    flag_value = True
    for i in range(N):
        v, w = map(int, input().split())
        value.append(v)
        weight.append(w)
        if v > 1000:
            flag_value = False

    if N <= 30:
        harf = len(value) // 2
        combination = make_combination(harf, weight, value, W)
        ans = cal_max_weight(N, harf, combination, weight, value, W)
    else:
        if flag_value:
                # 1000より大きいvalueが存在しない時、1000より大きいweightがある可能性がある
            ans = value_dp(N, weight, value, W)
        else:
            # 1000より大きいvalueが存在する時、1000以下のweightしかない
            ans = weight_dp(N, weight, value, W)
    print(ans)


if __name__ == "__main__":
    main()
