#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    long int X,Y,max_length=1;
    cin >> X >> Y;
    while(X*2<=Y){
        X *= 2;
        max_length++;
    }
    cout << max_length << endl;
    return 0;
}