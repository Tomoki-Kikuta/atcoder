#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    long int A,B;
    cin >> A >> B;
    if((A - B) % 2 !=0){
        cout << "IMPOSSIBLE" << endl;
    }else{
        cout << (A + B) / 2 << endl; 
    }
    return 0;

}