#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(void){
    string S;
    cin >> S;
    bool flag = true;
    for(int i=0;i<3;i++){
        if(S[i]==S[i+1]){
            flag = false;
            break;
        }
    }
    if(!flag){
        cout << "Bad" << endl;
    }else{
        cout << "Good" << endl;
    }
    return 0;
}