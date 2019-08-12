#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int A,B;
    cin >> A >> B;
    int max_a = A + B;
    if(A - B > max_a){
        max_a = A - B;
    }
    if(A * B > max_a){
        max_a = A * B;
    }
    cout << max_a << endl;
    return 0;
}