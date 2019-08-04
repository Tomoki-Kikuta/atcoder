#include<iostream>
#define MAX 101
using namespace std;
int N,h[MAX],height[MAX];
int count(void){
    int c = 0;
    while(true){
        int start,r,l;
        bool flag = true;
        for(int i=0;i<N;i++){
            if(h[i]!=height[i]){
                start = i;
                flag = false;
                break;
            }
        }
        if(flag){
            break;
        }
        c++;
        r = start;
        l = start+1;
        while(h[l]!=height[l]){
            l++;
            if(l==N){
                break;
            }
        }
        for(int j=r;j<l;j++){
            height[j]++;
        }
    }
    return c;
}
int main(void){
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> h[i];
        height[i] = 0;
    }
    cout << count() << endl;
    return 0;
}