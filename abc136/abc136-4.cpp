#include<iostream>
#include<algorithm>
#include<string>
#define MAX 100005
using namespace std;
int main(void){
    string S;
    cin >> S;
    int stage[MAX] = {0};
    for(int i=0;i<S.size();i++){
        int count_A = 0;
        int count_B = 0;
        char a = S[i];
        int t = i;
        while(a == S[t]){
            t++;
            count_A ++;
        }
        int s = t;
        t -= 1;
        a = S[s];
        while(a == S[s]){
            s++;
            count_B ++;
        }
        s -= 1;
        i = s;
        if((count_A+count_B)%2==0){
            stage[t] = stage[t+1] = (count_A+count_B) / 2;
        }else{
            if((count_A > count_B && count_A%2==0) || (count_B > count_A && count_B % 2 !=0)){
                stage[t] = (count_A+count_B) / 2 ;
                stage[t+1] = (count_A+count_B) / 2 + 1;
            }else{
                stage[t] = (count_A+count_B) / 2 + 1;
                stage[t+1] = (count_A+count_B) / 2;
            }
        }
    }

    for(int i=0;i<S.size();i++){
        if(i > 0){
            cout << ' ';
        }
        cout << stage[i];
    }
    cout << endl;

    return 0;
}