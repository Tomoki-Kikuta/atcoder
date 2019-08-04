#include<iostream>
#include<algorithm>
#define MAX 51
using namespace std;
int main(void){
    int N,p[MAX],copy_p[MAX];
    cin >> N;
    for(int i=0;i<N;i++){
        cin >>p[i];
        copy_p[i] = p[i];
    }
    sort(copy_p,copy_p+N);
    int count = 0;
    for(int i=0;i<N;i++){
        if(copy_p[i]!=p[i]){
            count +=1;
        }
    }
    if(count==2 || count==0){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
    return 0;
}