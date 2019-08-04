#include<iostream>
#include<algorithm>
#define MOD 1000000000 + 7
#define MAX 100000 + 5
using namespace std;
long long fac[MAX], finv[MAX], inv[MAX];
// テーブルを作る前処理
void COMinit(){
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

// 二項係数計算
long long COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}

int main() {
    int N,A,B,C;
    long int count = 0;
    cin >> N >> A >> B >> C;
    // 前処理
    COMinit();

    // 計算例
    for(int i=1;i<=N;i++){
        count += COM(i,A);
    }
    cout << count << endl;
    return 0;
}