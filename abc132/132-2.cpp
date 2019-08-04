#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    int n,p[21];
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> p[i];
    }
    int count = 0;
    for(int i=1;i<n-1;i++){
        if(p[i-1]<p[i] && p[i]<p[i+1]){
            count += 1;
        }
        else if(p[i-1]>p[i] && p[i]>p[i+1]){
            count += 1;
        }
    }
    cout << count << endl;
    return 0;
}