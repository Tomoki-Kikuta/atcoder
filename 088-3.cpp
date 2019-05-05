#include<iostream>
#include<algorithm>
#define MAX 101
using namespace std;
int main(void){
    int c[3][3],a[3],b[3];
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            cin >> c[i][j];
        }
    }
    bool flag = true;
    a[0] = 0;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(i==0){
                b[j] = c[i][j];
            }else{
                if(j==0){
                    a[i] = c[i][j] - b[j];
                }else{
                    if(a[i]+b[j]!=c[i][j]){
                        flag = false;
                        break;
                    }
                }
            }
        }
        if(!flag){
            break;
        }
    }
    if(flag){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
}