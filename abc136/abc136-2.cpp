#include<iostream>
#include<algorithm>
#include<string>
#include<cstdio>
#include<limits>
#include<sstream>
using namespace std;
int main(void){
    int N,count=0;
    cin >> N;
    for(int i=1;i<=N;i++){
        stringstream a;
        a << i;
        string aa = a.str();
        if(aa.size()%2==1){
            count += 1;
        }
    }
    cout << count << endl;
    return 0;
}