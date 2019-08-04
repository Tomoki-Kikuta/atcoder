#include<iostream>
#include<algorithm>
#define MAX 100004
using namespace std;
int main(void){
    int n;
    long int count = 0,K,A[MAX];
    cin >> n >> K;
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        if(i!=0){
            A[i] = A[i-1] + a;
        }else{
            A[i] = a;
        }
    }
    int now_id = 0;
    long int now = 0;
    for(int j=0;j<n;j++){
        if(A[j] - now >=K){
            count += n - j;
            now = A[now_id];
            now_id++;
            j--;
        }
    }
    cout << count << endl;
    return 0;
}