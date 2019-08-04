#include<iostream>
#include<algorithm>
#define MAX 2*100001
using namespace std;
int main(void){
    int N;
    pair<long int,long int> table[MAX];
    cin >> N; 
    for(int i=0;i<N;i++){
        cin >> table[i].second >> table[i].first;
    }
    sort(table,table+N);
    bool flag = true;
    long int now_time = 0;
    int job = 0;
    while(job < N){
        if(now_time + table[job].second > table[job].first){
            flag = false;
            break;
        }else{
            now_time += table[job].second;
            job++;
        }
    }
    if(flag){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
}