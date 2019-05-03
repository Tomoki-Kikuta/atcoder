#include<iostream>
#include<algorithm>
#define MAX 100001
using namespace std;
int N;
long int A[MAX];
long int count(void){
    long int count = 0;
    long int sum = 0;
    long int min_A = 1000000000;
    for(int i=0;i<N;i++){
        if(A[i]<0){
            sum++;
        }
        min_A = min(min_A,abs(A[i]));
        count += abs(A[i]);
    }
    if(sum%2!=0){
        count -= min_A * 2;
    }
    return count;
}
int main(void){
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> A[i];
    }
    cout << count() << endl;
    return 0;
}