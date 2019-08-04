#include<iostream>
#include<algorithm>
#define MAX 200005
using namespace std;
int main(void){
    int N,A[MAX],max_1 = 0,max_2 = 0;
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> A[i];
        if(max_1 <= A[i]){
            max_2 = max_1;
            max_1 = A[i];
        }else if(max_2 < A[i]){
            max_2 = A[i];
        }
    }
    for(int i=0;i<N;i++){
        if(A[i]==max_1){
            cout << max_2 << endl;
        }else{
            cout << max_1 << endl;
        }
    }
    return 0;
}