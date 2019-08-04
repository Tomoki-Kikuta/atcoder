#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int p,q,r,count=0;
    cin >> p >> q >> r;
    count = p + q;
    if(count > r + q){
        count = r + q;
    }
    if(p + r < count){
        count = p + r;
    }
    if(p + q < count){
        count = p + q;
    }
    cout << count << endl;
    return 0;
}