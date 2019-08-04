#include<iostream>
#include<algorithm>
#define MAX 100005
using namespace std;
int main(void){
    int N;
    long int A[MAX],B[MAX],count = 0;
    cin >> N;
    A[N+1] = 1000000000;
    for(int i=0;i<=N;i++){
        cin >> A[i];
    }
    for(int i=0;i<N;i++){
        cin >> B[i];
    }
    for(int i=0;i<N;i++){
        if(A[i] < B[i]){
            count += A[i];
            if(A[i+1] - (B[i] - A[i]) > 0){
                count += (B[i] - A[i]);
                A[i+1] -= (B[i] - A[i]);
            }else{
                count += A[i+1];
                A[i+1] = 0;
            }
        }else{
            count += B[i];
        }
    }
    cout << count << endl;
    return 0;
}