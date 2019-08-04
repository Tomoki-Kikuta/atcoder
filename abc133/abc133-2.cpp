#include<iostream>
#include<algorithm>
#include<math.h>
#include<cmath>
#define MAX 11
using namespace std;
int main(void){
    int N, D,A[MAX][MAX],count=0;
    cin >> N >> D;
    for(int i=0;i<N;i++){
        for(int j=0;j<D;j++){
            cin >> A[i][j];
        }
    }
    for(int i=0;i<N;i++){
        for(int j=i+1;j<N;j++){
            double distance = 0;
            for(int t=0;t<D;t++){
                distance += abs(A[i][t] - A[j][t]) * abs(A[i][t] - A[j][t]);
            }
            distance = sqrt(distance);
            if(lround(distance)==distance){
                count += 1;
            }
        }
    }
    cout << count << endl;
    return 0;
}