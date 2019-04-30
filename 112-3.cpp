#include<iostream>
#define MAX 101
using namespace std;
struct Parcel{
    int x;
    int y;
    long int h;
};
Parcel A[MAX];
long int abs(int i,int x,int y){
    if(A[i].x-x>=0 && A[i].y-y>=0){
        return A[i].h + A[i].x-x + A[i].y - y;
    }else if(A[i].x-x<0 && A[i].y-y>=0){
        return A[i].h + x - A[i].x + A[i].y - y;
    }else if(A[i].x-x>=0 && A[i].y-y<0){
        return A[i].h + A[i].x - x + y - A[i].y;
    }else{
        return A[i].h + x - A[i].x  + y - A[i].y;
    }
}
int main(void){
    int n,Cx,Cy;
    long int H;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> A[i].x >> A[i].y >> A[i].h;
    }
    for(int x=0;x<MAX;x++){
        bool flag;
        for(int y=0;y<MAX;y++){
            long int a,b;
            flag = true;
            int t = 0;
            while(true){
                if(A[t].h==0){
                    t++;
                    if(t>=n){
                        break;
                    }
                }else{
                    a = abs(t,x,y);
                    break;
                }
            }
            for(int s=0;s<n;s++){
                if(A[s].h==0){
                    continue;
                }else{
                    b = abs(s,x,y);
                }
                if(a!=b){
                    flag = false;
                    break;
                }
            }
            if(flag){
                H = a;
                Cx = x;
                Cy = y;
                break;
            }
        }
        if(flag){
            break;
        }
    }
    cout << Cx << ' ' << Cy << ' ' << H << endl;
    return 0;
}