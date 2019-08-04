#include<iostream>
#include<vector>
#define INF 1<<21
using namespace std;
int N,A,B,C,l[8];
vector<int> min_mp;
void process(int i,int mp,int a,int b,int c){
    if(i<N){
        process(i+1,mp,a,b,c);
        mp += 10;
        process(i+1,mp,a+l[i],b,c);
        process(i+1,mp,a,b+l[i],c);
        process(i+1,mp,a,b,c+l[i]);
    }else{
        if(a!=0 && b!=0 && c!=0){
            mp += abs(A-a);
            mp += abs(B-b);
            mp += abs(C-c);
            min_mp.push_back(mp);
        }
    }
}
int count(void){
    int min = INF;
    for(int i=0;i<min_mp.size();i++){
        if(min>min_mp[i]){
            min = min_mp[i];
        }
    }
    return min - 30;
}
int main(void){
    cin >> N >> A >> B >> C;
    for(int i=0;i<N;i++){
        cin >> l[i];
    }
    process(0,0,0,0,0);
    cout << count() << endl;
    return 0;
}