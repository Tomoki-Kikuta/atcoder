#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#define MAX 100000 + 5 
using namespace std;
int main(void){
    int N,c[MAX],color[MAX],d[MAX],count=0;
    vector<int> tree[MAX];
    queue<int> ver;
    cin >> N;
    for(int i=1;i<N;i++){
        int a,b;
        cin >> a >> b;
        a--;
        b--;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }
    for(int i=0;i<N;i++){
        color[i] = 0;
        cin >> c[i];
    }
    sort(c,c+N, greater<int>());
    int max_v = 0;
    for(int i=0;i<N;i++){
        if(i!=0){
            count += c[i];
        }
        if(max_v < tree[i].size()){
            max_v = i;
        }
    }
    ver.push(max_v);
    color[max_v] = 1;
    d[max_v] = c[0]; 
    int u = 1;
    while(!ver.empty()){
        //cout << count << endl;
        int v = ver.front();
        ver.pop();
        for(int i=0;i<tree[v].size();i++){
            int next_v = tree[v][i];
            if(color[next_v]==0){
                d[next_v] = c[u];
                ver.push(next_v);
                color[next_v] = 1;
                u++;
            }
        }
    }
    cout << count << endl;
    for(int i=0;i<N;i++){
        if(i>0){
            cout << ' ';
        }
        cout << d[i];
    }
    cout << endl;
    return 0;
}