#include<iostream>
#include<algorithm>
#define MAX 200001
using namespace std;
int main(void){
    int N;
    long int X[MAX],Y[MAX];
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> X[i];
        Y[i] = X[i];
    }
    sort(Y,Y+N);
    for(int i=0;i<N;i++){
        if(X[i]<=Y[N/2-1]){
            cout << Y[N/2] << endl;
        }else{
            cout << Y[N/2-1] << endl;
        }
    }
    return 0;
}