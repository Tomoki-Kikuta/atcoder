#include<iostream>
#include<algorithm>
#define MAX 100001
using namespace std;
int main(void){
    int N,A[MAX]={0};
    long int count = 0;
    cin >> N;
    for(int i=0;i<N;i++){
        long int a;
        cin >> a;
        if(a>N){
            count++;
        }else{
            A[a]++;
        }
    }
    for(int i=1;i<=N;i++){
        //cout << i << ' ' << A[i] << endl;
        if(A[i]<i){
            count += A[i];
        }else if(A[i]>i){
            count += A[i] - i;
        }
    }
    cout << count << endl;
    return 0;
}