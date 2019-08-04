#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int N,L,sum=0,minus;
    bool flag = true;
    cin >> N >> L;
    minus = 500;
    for(int i=1;i<=N;i++){
        sum += L + i  - 1;
        int a = L + i  - 1;
        minus = min(minus,abs(a));
    }
    if(sum>=0){
        cout << sum -minus << endl;
    }else{
        cout << sum + minus << endl;
    }
    return 0;
}