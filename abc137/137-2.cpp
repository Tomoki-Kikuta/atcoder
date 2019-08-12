#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int K,X;
    cin >> K >> X;
    for(int i=X-K+1;i<=X+K-1;i++){
        if(i > X - K + 1 ){
            cout << ' ';
        }
        cout << i;
    }
        cout << endl;
    return 0;
}