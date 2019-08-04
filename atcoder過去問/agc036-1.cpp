#include<iostream>
#include<algorithm>
#define MAX_X_Y 1000000000
using namespace std;
long int binary_search(long int right, long int left,long int S){
    long int mid = (right + left) / 2;
    if(mid * mid > S){
        mid = binary_search(right,mid,S);
    }else if(mid*mid==S){
        return mid;
    }else{
        mid = binary_search(mid,right,S);
    }
    return mid;
}
int main(void){
    long int S;
    pair<long int,long int> X_Y[3];
    cin >> S;
    X_Y[0].first = X_Y[0].second = 0;
    long int A = binary_search(0,MAX_X_Y,S);
    if(S%2==0){
        X_Y[1].first = 0;
        X_Y[2].second = 0; 
    }else{
        X_Y[1].first = 1;
        X_Y[2].second = 1;
        S += 1;
    }
    long int A = S;
    long int B = 1;
    while(A>MAX_X_Y){
        for(long int i=2;i<=A;i++){
            if(A % i == 0){
                A /= i;
                B *= i;
                break; 
            }
        }  
    }
    X_Y[1].second = A;
    X_Y[2].first = B;
    for(int i=0;i<3;i++){
        if(i>0){
            cout << ' ';
        }
        cout << X_Y[i].first << ' ' << X_Y[i].second;
    }
    cout << endl;
    return 0;
}