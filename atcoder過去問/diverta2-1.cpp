#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int n,k,count=0;
    cin >> n >> k;
    if(k!=1){
        n -= k;
        count += n;
    }
    cout << count << endl;
    return 0;
}