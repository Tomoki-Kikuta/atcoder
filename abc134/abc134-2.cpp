#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int N,D,count=0;
    cin >> N >> D;
    for(int i=1;i<=N;i++){
        i +=  2 * D;
        count +=1;
    }
    cout << count << endl;
    return 0;
}