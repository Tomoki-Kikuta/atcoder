#include<iostream>
#include<algorithm>
#define MAX 2 * 100001
using namespace std;
int N,A[MAX];
int main(void){
    cin >> N;
    A[0] = 0;
    A[N+1] = 0;
    for(int i=1;i<=N;i++){
        cin >> A[i];
    }
    int count = 0;
    for(int i=1;i<=N+1;i++){
        count += abs(A[i]-A[i-1]);
    }
    for(int i=1;i<=N;i++){
        int cost = count;
        cost += abs(A[i-1]-A[i+1]) - (abs(A[i-1]-A[i]) + abs(A[i]-A[i+1]));
        cout << cost << endl;
    }
    return 0;
}