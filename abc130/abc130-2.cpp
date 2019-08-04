#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int n,x,L[101],count=1;
    cin >> n >> x;
    for(int i=0;i<n;i++){
        cin >> L[i];
    }
    int D;
    int d = 0;
    for(int i=1;i<n+1;i++){
        D = d + L[i-1];
        d = D;
        if(D<=x){
            count++;
        }
    }
    cout << count << endl;
    return 0;
}