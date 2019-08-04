#include<iostream>
#include<algorithm>
#define MAX 200001
using namespace std;
int main(void){
    int N,K,A[MAX]={0},count=0;
    cin >> N >> K;
    for(int i=0;i<N;i++){
        int a;
        cin >> a;
        A[a]++;
    }
    sort(A,A+MAX);
    int number = 0;
    for(int i=MAX-1;i>=0;i--){
        if(A[i]!=0){
            //cout << A[i] << endl;
            if(number!=K){
                number++;
            }else{
                count += A[i];
            }
        }else if(number==K && A[i]==0){
            break;
        }
    }
    cout << count << endl;
    return 0;
}