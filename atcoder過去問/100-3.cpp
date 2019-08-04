#include<iostream>
#define MAX 10001
using namespace std;
int N;
long int a[MAX];
long int count(void){
    long int sum = 0;
    for(int i=0;i<N;i++){
        if(a[i]%2==0){
            while(a[i]%2==0){
                a[i] /= 2; 
                sum ++;
            }
        }
    }
    return sum;
}
int main(void){
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> a[i];
    }
    cout << count() << endl;
    return 0;
}