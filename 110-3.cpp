#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main(void){
    string S,T;
    cin >> S >> T;
    int alpa_S[26],alpa_T[26];
    for(int i=0;i<26;i++){
        alpa_S[i] = alpa_T[i] = -1;
    }
    for(int i=0;i<S.length();i++){
        int a = S[i] - 'a';
        int b = T[i] - 'a';
        if(alpa_S[a]!=-1 || alpa_T[b]!=-1){
            if(alpa_S[a]!=b || alpa_T[b]!=a){
                cout << "No" << endl;
                return 0;
            }
        }else{
            alpa_S[a] = b;
            alpa_T[b] = a;
        }
    }
    cout << "Yes" << endl;
    return 0;
}