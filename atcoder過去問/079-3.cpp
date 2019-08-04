#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int A,B,C,D;
    char a,b,c,x,y,z,r;
    cin >> x >> y >> z >> r;
    A = x - '0';
    B = y - '0';
    C = z - '0';
    D = r - '0';
    if(A+B+C+D==7){
        a = '+';
        b = '+';
        c = '+';
    }else if(A+B+C-D==7){
        a = '+';
        b = '+';
        c = '-';
    }else if(A+B-C+D==7){
        a = '+';
        b = '-';
        c = '+';
    }else if(A-B+C+D==7){
        a = '-';
        b = '+';
        c = '+';
    }else if(A-B-C+D==7){
        a = '-';
        b = '-';
        c = '+';
    }else if(A+B-C-D==7){
        a = '+';
        b = '-';
        c = '-';
    }else if(A-B+C-D==7){
        a = '-';
        b = '+';
        c = '-';
    }else{
        a = '-';
        b = '-';
        c = '-';
    }
    cout << A << a << B << b << C << c << D << '=' << 7 << endl;
    return 0;
}