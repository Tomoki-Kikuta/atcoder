#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    long double W,H,x,y;
    cin >> W >> H >> x >> y;
    cout << H * W /2 << ' ';
    if(x==W/2 && y==H/2){
        cout << 1 << endl;
    }else{
        cout << 0 << endl;
    }
    return 0;
}