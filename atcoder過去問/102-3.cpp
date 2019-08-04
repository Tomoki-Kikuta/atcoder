#include<iostream>
#include<algorithm>
#define MAX 2 * 100001 + 1
using namespace std;
int N;
long int A[MAX];
long int process(void){
    long int min_sum = 0;
    long int b;
    sort(A,A+N);
    if(N%2==0){
        b = (A[N/2] + A[N/2-1]) / 2;
    }else{
        b = A[N/2];
    }
    for(int i=0;i<N;i++){
        //cout << abs(A[i]-b) << endl;
        min_sum += abs(A[i]-b);
    }
    return min_sum;
}
int main(void){
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> A[i];
        A[i] -= i+1;
    }
    cout << process() << endl;
    return 0;
}