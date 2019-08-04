#include<iostream>
#include<algorithm>
#include<vector>
#define MAX 100001
using namespace std;
long int gcd(long int a,long int b){
    if(a<b){ 
        swap(a,b);
    }
    if(b<1){
        return -1;
    }
    if(a%b==0){
        return b;
    }
    return gcd(b,a%b);
}
int main(void){
    int n;
    long int X,D,x[MAX];
    vector<long int> gc;
    cin >> n >> X;
    for(int i=0;i<n;i++){
        cin >> x[i];
    }
    x[n] = X;
    sort(x,x+n+1);
    for(int i=0;i<n;i++){
        gc.push_back(x[i+1]-x[i]);
    } 
    D = gc[0];
    for(int i=1;i<gc.size();i++){
        D = gcd(D,gc[i]);
    }
    cout << D << endl;
    return 0;
}
