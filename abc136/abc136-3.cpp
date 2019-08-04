#include<iostream>
#include<algorithm>
#define MAX 100005
using namespace std;
int main(void){
    int N;
    long int H[MAX];
    bool flag[MAX] = {0};
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> H[i];
    }
    for(int i=0;i<N-1;i++){
        if(H[i+1] - H[i] < 0 && flag[i] == false){
            H[i] -= 1;
            flag[i] = true;
        }else if(H[i+1] - H[i] > 0 && flag[i+1] == false){
            H[i+1] -= 1;
            flag[i+1] = true;
        }else{
            flag[i] = true;
            flag[i+1] = true;
        }
        if(H[i+1] < H[i]){
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
    return 0;
}