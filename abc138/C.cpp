#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#define MAX 55
using namespace std;
int main(void){
    int N,v[MAX];
    priority_queue<double> pri;
    cin >> N;
    for(int i=0;i<N;i++){
        int a;
        cin >> a;
        pri.push(a * -1);
    }
    for(int i=0;i<N-1;i++){
        double a = pri.top();
        pri.pop();
        double b = pri.top();
        pri.pop();
        pri.push((a+b)/2);
    }
    cout << pri.top()* -1 << endl;
    return 0;
}