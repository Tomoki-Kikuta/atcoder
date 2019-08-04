#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int A,B,count=0;
    cin >> A >> B;
    if(A >=6 && A<=12){
        count = B / 2;
    }else if(A<=5){
        count = 0;
    }else{
        count = B;
    }
    cout << count << endl;
    return 0;
}