#include<iostream>
#include<algorithm>
using namespace std;
int A,B,C,X,Y;
int count(void){
    int cost = 0;
    if(A+B>C*2){
        int num = min(X,Y);
        X -= num;
        Y -= num;
        cost += num * 2 * C;
        if(X==0){
            cost += min(B*Y,2*C*Y);
        }else{
            cost += min(A*X,2*C*X);
        }
    }else{
        cost += X * A;
        cost += Y * B;
    }
    return cost;
}
int main(void){
    cin >> A >> B >> C >> X >> Y;
    cout << count() << endl;
    return 0;
}
