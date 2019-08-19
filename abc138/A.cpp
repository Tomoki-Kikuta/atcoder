#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(void){
    int a;
    string s;
    cin >> a >> s;
    if(a>=3200){
        cout << s.c_str() << endl;
    }else{
        cout << "red" << endl;
    }
    return 0;
}