#include<iostream>
#include<algorithm>
#define MAX 100005
using namespace std;
int main(void){
    int N,d[MAX];
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> d[i];
    }
    sort(d,d+N);
    int mid = N/2;
    cout << d[mid] - d[mid-1] << endl;
    return 0;
}