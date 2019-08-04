#include<iostream>
#include<algorithm>
#include<vector>
#define MAX 100005
using namespace std;
int main(void){
    int N,M,count_0,count_1;
    vector<int> tree[MAX];
    vector<int> print_tree[MAX];
    cin >> N >> M;
    if(M%2==1){
        cout << -1 << endl;
        return 0;
    }else{
        for(int i=0;i<M;i++){
            int a,b;
            cin >> a >> b;
            tree[a].push_back(b);
            tree[b].push_back(a);
        }
        
        for(int i=1;i<=N;i++){
            count_0 = 0;
            count_1 = 0;
            for(int j=0;j<tree[i].size();j++){
                int next = tree[i][j];
                if(tree[next].size() % 2 == 1){
                    count_1 +=1;
                }else{
                    count_0 +=1;
                }
                if(count_0)
            }
        }
        for(int i=1;i<=N;i++){
            for(int j=0;j<tree[i].size();j++){
                cout << i << ' ' << print_tree[i][j] << endl;
            }
        }
    }
    return 0;
}