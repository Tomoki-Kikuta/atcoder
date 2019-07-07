#include<iostream>
#include<algorithm>
#define MOD 2019
using namespace std;
int main(void){
    long int L,R;
    cin >> L >> R;
    if(L/MOD == R/MOD){
        L %= MOD;
        R %= MOD;
        int count = 2020;
        for(int i=L;i<=R-1;i++){
            for(int j=i+1;j<=R;j++){
                int t = i * j;
                if(i*j>=MOD){
                    t %= MOD;
                }
                count = min(t,count);
            }
        }
        cout << count << endl;
    }else{
        cout << 0 << endl;
    }
    return 0;
}