#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main(void){
    long int N,A[5],person[6],now_time = 0;
    cin >> N;
    for(int i=0;i<6;i++){
        cin >> A[i];
    }
    for(int i=0;i<5;i++){
        if(A[i] * (now_time - i) > N){
            person[i] = 1;
        }else{
            person[i] = N - (A[i] * (now_time - i));
        }
        if(person[i]%A[i]==0){
            now_time += person[i] / A[i];
        }else{
            now_time += person[i] / A[i] + 1;
        }
    }
    cout << now_time << endl;
    return 0;
}