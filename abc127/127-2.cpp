#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int r,D,x;
    cin >> r >> D >> x;
    for(int i=0;i<10;i++){
        cout << x*r - D << endl;
        x = x*r - D;
    }
    return 0;
}