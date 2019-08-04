#include<iostream>
#include<algorithm>
#define ten_thousand 10000
#define five_thousand 5000
#define thousand 1000
using namespace std;
int main(void){
int N,A,B,C;
long int Y;
bool flag = false;
    cin >> N >> Y;
    for(int i=0;i<=N;i++){
        for(int j=0;j<=N;j++){
            if(i+j>N){
                continue;
            }
            if((i*ten_thousand + j*five_thousand + (N-i-j)*thousand)==Y){
                A = i;
                B = j;
                C = N - i - j;
                flag = true;
                break;
            }
        }
        if(flag){
            break;
        }
    }
    if(flag){
        cout << A << ' ' << B << ' ' << C << endl;
    }else{
        cout << -1 << ' ' << -1 << ' ' << -1 << endl;
    }
    return 0;
}