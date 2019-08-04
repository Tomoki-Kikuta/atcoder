#include<iostream>
#include<algorithm>
#define MAX 101
using namespace std;
int main(void){
    int n,weight[MAX],sum = 0,min_sum = 10000000;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> weight[i];
        sum += weight[i];
    }
    int a = 0;
    for(int i=0;i<n;i++){
        int b;
        a += weight[i];
        b = sum - a; 
        if(abs(a-b)< min_sum){
            min_sum = abs(a-b);
        }
    }
    cout << min_sum << endl;
    return 0;
}