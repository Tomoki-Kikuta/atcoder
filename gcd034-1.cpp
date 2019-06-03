#include<iostream>
#include<algorithm>
#include<string>
#define MAX 200005
using namespace std;

string S;

bool ok(int start,int end){
    bool ok = true;
    for(int i = start;i < end;i++){
        if(S[i] == '#' && S[i+1] == '#'){
            ok = false;
            break;
        }
    }
    return ok;
}

void print(bool flag){
    if(flag){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}

int main(void){
    int N,A,B,C,D;
    bool flag = true;
    cin >> N >> A >> B >> C >> D >> S;
    A--;B--;C--;D--;
    if(!ok(A,C) || !ok(B,D)){
        flag = false;
        // 岩が並んでいないか
    }
    if(C > D){
        bool can_over = false;
        for(int i = B;i<=D;i++){
            if(S[i-1] == '.' &&  S[i] == '.' && S[i+1] == '.'){
                can_over = true;
            }
        }
        if(!can_over){
            // 追い抜けない時
            flag = false;
        }
    }
    print(flag);
    return 0;
}