#include<iostream>
#include<algorithm>
#define MAX 1000000001
using namespace std;
int main(void){
    long int N,M,count;
    cin >> N >> M;
    if(N>=2 && M>=2){
        count = (N-2) * (M-2);
    }else if(N==1 && M>=2){
        count = M - 2;
    }else if(N>=2 && M==1){
        count = N - 2;
    }else{
        count = 1;
    }
    cout << count << endl;
    return 0;
}