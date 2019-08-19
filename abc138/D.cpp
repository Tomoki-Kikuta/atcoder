#include<iostream>
#include<algorithm>
#include<vector>
#define MAX 300005
using namespace std;
int main(void){
    int N,Q,p[MAX] = {0};
    int tree[MAX] = {0};
    cin >> N >> Q;
    for(int i=1;i<=N-1;i++){
        int a,b;
        cin >> a >> b;
        p[b] = a;
    }
    for(int i=0;i<Q;i++){
        int a,b;
        cin >> a >> b;
        tree[a] += b; 
    }
    for(int i=1;i<=N;i++){
        tree[i] += tree[p[i]]; 
    }
    for(int i=1;i<=N;i++){
        if(i > 1){
            cout << ' ';
        }
        cout << tree[i];
    }
    cout << endl;
    return 0;
}