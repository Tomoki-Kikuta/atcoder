#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int A,P,count=0;
    cin >> A >> P;
    count += P + A * 3;
    cout << count / 2 << endl;
    return 0;
}