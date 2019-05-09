#include<iostream>
#include<algorithm>
#include<vector>
#define MAX 101
using namespace std;
int N,A[2][MAX];
vector<int> Maximum_candidate;
void process(int y,int x,int c){
    //cout << y << ' ' << x << endl;
    if(y<2 && x<N){
        c += A[y][x];
        //cout << c << endl;
        if(y==0){
            //右に行く
            process(y,x+1,c);
            //下に行く
            process(y+1,x,c);
        }else{
            //右に行く
            process(y,x+1,c);
        }
    }else{
        if(x==N && y==1){
            Maximum_candidate.push_back(c);
        }
    }
}
int count(void){
    int count = 0;
    process(0,0,count);
    for(int i=0;i<Maximum_candidate.size();i++){
        count = max(count,Maximum_candidate[i]);
    }
    return count;
}
int main(void){
    cin >> N;
    for(int i=0;i<2;i++){
        for(int j=0;j<N;j++){
            cin >> A[i][j];
        }
    }
    cout << count() << endl;
    return 0;
}