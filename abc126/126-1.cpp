#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(void){
    int N,K;
    string S;
    cin >> N >> K >> S;
    K--;
    S[K] = S[K] + 32;
    cout << S << endl;
    return 0;
}