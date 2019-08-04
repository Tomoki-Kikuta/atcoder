#include<iostream>
#include<algorithm>
#include<cmath>
#include <iomanip>
using namespace std;
int main(void){
    int N,K;
    double count = 0.000000000;
    cin >> N >> K;
    //cout << 1/(float)N << endl;
    for(int i=1;i<=N;i++){
        double A = 1/(double)N;
        if(i<=K-1){
            int score = i;
            while(score<=K-1){
                score *= 2;
                A *= 0.5;
            }
        }
        count += A;
    }
    cout <<setprecision(12) << count << endl;
    return 0;
}