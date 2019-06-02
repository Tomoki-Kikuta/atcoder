#include<iostream>
#include<algorithm>
#include<vector>
#define MAX 1000
using namespace std;
int main(void){
    int X,Y,Z,K,k;
    vector<long int> A,B,C,D,E;
    cin >> X >> Y >> Z >> K;
    for(int i=0;i<X;i++){
        long int a;
        cin >> a;
        A.push_back(a);
    }
    for(int i=0;i<Y;i++){
        long int b;
        cin >> b;
        B.push_back(b);
    }
    for(int i=0;i<Z;i++){
        long int c;
        cin >> c;
        C.push_back(c);
    }
    for(int i=0;i<X;i++){
        for(int j=0;j<Y;j++){
            long int d = A[i] + B[j];
            D.push_back(d);
        }
    }
    sort(D.begin(),D.end(),greater<long int>());
    if(D.size()<K){
        k = D.size();
    }else{
        k = K;
    }
    for(int i=0;i<k;i++){
        for(int j=0;j<Z;j++){
            long int d = D[i] + C[j];
            E.push_back(d);
        }
    }
    sort(E.begin(),E.end(),greater<long int>());
    for(int i=0;i<K;i++){
        cout << E[i] << endl;
    }
    return 0;
}