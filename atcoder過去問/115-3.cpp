#include<iostream>
#include<vector>
#include<algorithm>
#define MAX 100001
using namespace std;
int main(void){
    int N,K;
    long int tree[MAX];
    cin >> N >> K;
    for(int i=0;i<N;i++){
        cin >> tree[i];
    }
    sort(tree,tree+N);
    long int min = tree[N-1] - tree[0];
    for(int i=0;i<N-K+1;i++){
        long int hmin = tree[i+K-1] - tree[i];
        if(hmin<min){
            min = hmin;
        }
    }
    cout << min << endl;
    return 0;
}