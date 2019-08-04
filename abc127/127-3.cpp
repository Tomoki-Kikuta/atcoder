#include<iostream>
#include<algorithm>
#define MAX 100001
using namespace std;
int main(void){
    int N,M,count =0,max_L= 0,min_R = MAX;
    cin >> N >> M;
    for(int i=0;i<M;i++){
        int L,R;
        cin >> L >> R;
        if(max_L < L){
            max_L = L;
        }
        if(min_R > R){
            min_R = R;
        }
    }
    //cout << max_L << ' ' << min_R << endl;
    for(int i=1;i<=N;i++){
        if(i>=max_L && min_R>=i){
            count++;
        }
    }
    cout << count << endl;
    return 0;
}