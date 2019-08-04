#include<iostream>
#include<algorithm>
#define MAX 100005
#define MAX_A 1000000000
using namespace std;

bool check(long int left, int mid,int right){
    int count_left = 0;
    int count_mid = 0;
    int count_right = 0;
     while(left !=0){
        left /= 2;
        count_left +=1;
    }
}
int main(void){
    int N;
    long int a[MAX],count_zero=0;
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> a[i];
    }
    count_zero = check_zero(a);
    sort(a,a+N);
    for(int i=0;i<N;i++){
        bool flag;
        if(i==0){
            flag = check(a[i],a[i+1],a[N-1]);
        }else if(i==N-1){
            flag = check(a[i],a[i-1],a[0]);
        }else{
            flag = check(a[i],a[i-1],a[i+1]);
        }
        if(!flag){
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
    return 0;
}