#include<iostream>
#include<algorithm>
using namespace std;
int N;
long int count(void){
    int min = N;
    for(int i=0;i<=N;i++){
        int sum = 0;
        int a = i;
        while(a>0){
            sum += a % 6;
            a /= 6; 
        }
        a = N - i;
        while(a>0){
            sum += a % 9;
            a /= 9;
        }
        if(sum<min){
            min = sum;
        }
    }
    return min;
}
int main(void){
    cin >> N;
    cout << count() << endl;
    return 0;
}