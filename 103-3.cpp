#include<iostream>
#define MAX 3001
using namespace std;
int main(void){
    int N,a[MAX];
    long int score = 0;
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> a[i];
        score += a[i] - 1;
    }
    cout << score << endl;
    return 0;
}