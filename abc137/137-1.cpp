#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int A,B;
    cin >> A >> B;
    int max_ = A + B;
    max_ = max(max_,A-B);
    max_ = max(max_,A*B);
    cout << max_ << endl;
    return 0;
}