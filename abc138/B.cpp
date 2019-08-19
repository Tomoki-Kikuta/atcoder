#include<iostream>
#include<algorithm>
#include<iomanip>
#define MAX 101
using namespace std;
int main(void){
    int N;
    double count = 0;
    cin >> N;
    for(int i=0;i<N;i++){
        double a;
        cin >> a;
        double b = 1 / a;
        count += b;
    }
    cout << setprecision(30) <<  1 / count << endl;
    return 0;
}