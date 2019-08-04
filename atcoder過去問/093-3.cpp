#include<iostream>
#include<algorithm>
using namespace std;
int A[3];
int count(void){
    int count = 0;
    count += A[2] - A[1];
    A[0] += A[2] - A[1];
    A[1] = A[2];
    if((A[2]-A[0])%2!=0){
        count++;
        A[2]++;
    }
    count += (A[2]-A[0]) / 2;
    return count;
}
int main(void){
    cin >> A[0] >> A[1] >> A[2];
    sort(A,A+3);
    cout << count() << endl;
    return 0;
}