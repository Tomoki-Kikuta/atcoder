#include<iostream>
#include<algorithm>
#include<string>
#include<stdio.h>
using namespace std;
int main(void){
    char S[4];
    string A,B;
    for(int i=0;i<4;i++){
        cin >> S[i];
        if(i<2){
            A += S[i];
        }else{
            B += S[i];
        }
    }
    int Y = atoi(A.c_str());
    int M = atoi(B.c_str());
    //cout << Y << ' ' << M << endl;
    if(Y>=1 && Y<=12 && M>=1 && M<=12){
        cout << "AMBIGUOUS" << endl;
    }else if(Y>=1 && Y<=12 && (M>12||M==0)){
        cout << "MMYY" << endl;
    }else if((Y>12 || Y==0) && M>=1 && M<=12){
        cout << "YYMM" << endl;
    }else{
        cout << "NA" << endl;
    }
    return 0;
}