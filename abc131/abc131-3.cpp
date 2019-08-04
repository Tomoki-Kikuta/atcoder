#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    long int A,B,C,D;
    long int A__C,A__D,A__CD,B__C,B__D,B__CD;
    cin >> A >> B >> C >> D;
    if(C < D){
        swap(C,D);
    }
    long int c = C;
    long int d = D;
    long int u = C * D;
    long int r = C % D;
    while(r!=0){
        c = d;
        d = r;
        r = c % d;
    }
    long int gcd = u/d;
    A__C = (A-1) / C;
    A__D = (A-1) / D;
    A__CD = (A-1) / gcd;
    B__C = B / C;
    B__D = B / D;
    B__CD = B / gcd;
    //cout << ((B__C + B__D - B__CD) - (A__C + A__D - A__CD)) << endl;
    long answer = (B - A + 1) - ((B__C + B__D - B__CD) - (A__C + A__D - A__CD));
    cout << answer << endl;
    return 0;
}