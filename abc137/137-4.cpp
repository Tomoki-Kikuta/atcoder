#include<iostream>
#include<algorithm>
#include<queue>
#define MAX 100005
using namespace std;
int main(void){
    int N,M,money = 0;
    pair<int,int> A_B[MAX];
    priority_queue<int> candidate;
    cin >> N >> M;
    for(int i=0;i<N;i++){
        int A,B;
        cin >> A >> B;
        A_B[i].first = A;
        A_B[i].second = B;
    }
    sort(A_B,A_B+N);
    int u = 0;
    for(int i=1;i<=M;i++){
        bool flag = true;
        while(A_B[u].first == i && flag == true){
            candidate.push(A_B[u].second);
            u++;
            if(u == N){
                flag = false;
                break;
            }
        }
        if(candidate.size()==0){
            continue;
        }
        money += candidate.top();
        candidate.pop();
    }
    cout << money << endl;
    return 0;
}