#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(void){
    string S;
    int count = 0;
    cin >> S;
    for(int i=0;i<S.length();i++){
        if(S[i]=='o'){
            count++;
        }
    }
    if(count>=8){
        cout << "YES" << endl;
    }else if(S.length()<15){
        if(15 - S.length() + count >= 8){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
    }else{
        cout << "NO" << endl;
    }
    return 0;
}