#include<iostream>
#include<algorithm>
#define MAX 100001
using namespace std;
int N,K,A[MAX];
int process(void){
    int c = 0;
    int a = A[0];
    int i = 1;
    while(i<N){
        if(A[i]!=a){
            c++;
            i += K - 1;
        }else{
            i++;
        }
    }
    return c;
}
int main(void){
    int count;
    cin >> N >> K;
    for(int i=0;i<N;i++){
        cin >> A[i];
    }
    sort(A,A+N);
    count = process();
    cout << count << endl;
    return 0;
}