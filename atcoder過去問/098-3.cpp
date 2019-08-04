#include<iostream>
#include<string>
using namespace std;
int N;
string S;
int count(void){
    int count = 0;
    for(int i=1;i<N;i++){
        if(S[i]=='E'){
            count++;
        }
    }
    int min = count;
    for(int i=1;i<N;i++){
        int a = count;
        if(S[i]=='E'){
            a--;
        }
        if(S[i-1]=='W'){
            a++;
        }
        count = a;
        if(min > a){
            min = a;
        }
    }
    return min;
}
int main(void){
    cin >> N >> S;
    cout << count() << endl;
    return 0;
}