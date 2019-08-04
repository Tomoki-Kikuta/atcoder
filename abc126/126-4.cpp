#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#define MAX 100001
using namespace std;
int color[MAX] ={0};
int N;
struct Weight{
    int ver;
    long int w;
};
vector<Weight> tree[MAX];
void dfs(int r){
    int v = tree[r][0].ver;
    long int weight = tree[r][0].w;
    if(weight%2==0){
        color[v] = '1';
    }
}
int main(void){
    cin >> N;
    for(int i=0;i<N-1;i++){
        int u,v;
        Weight a;
        long int wei;
        cin >> u >> a.ver >> a.w;
        u--;
        a.ver--;
        tree[u].push_back(a);
        //cout << tree[u][0].ver << ' ' << tree[u][0].w << endl;;
    }
    dfs(1);
    return 0;
}