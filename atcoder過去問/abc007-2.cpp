#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(void){
    string s;
    cin >> s;
    if(s=="a"){
       cout << -1 << endl; 
    }else if(s.length()==1){
        cout << 'a' << endl;
    }else{
        cout << s[0] << endl;
    }
    return 0;
}