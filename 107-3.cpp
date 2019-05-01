#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main(void){
    string S;
    long long K;
    cin >> S >> K;
    int A = 1,n;
    if(K>S.size()){
        n = S.size();
    }else{
        n = K;
    }
    for(int i=0;i<n;i++){
        int a = S[i] - '0';
        //cout << a << endl;
        if(a!=1){
            A = a;
            break;
        }
    }
    cout << A << endl;
    return 0;
}