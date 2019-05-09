#include<iostream>
#include<algorithm>
#define MAX 100001
using namespace std;
struct Schedule{
    int t;
    int x;
    int y;
};
int N;
Schedule table[MAX];
bool fla;
void process(int x,int y,int t,int i){
    if(table[i].t==t){
        if(table[i].x==x && table[i].y==y){
            fla = true;
        }
    }else{
        if(table[i].x>x){
            process(x+1,y,t+1,i);
        }else if(table[i].x<x){
            process(x-1,y,t+1,i);
        }else{
            if(table[i].y<y){
                process(x,y-1,t+1,i);
            }else if(table[i].y>y){
                process(x,y+1,t+1,i);
            }else{
                if((table[i].t-t)%2==0){
                    fla = true;
                }
            }
        }
    }
}
void flag(void){
    int x = 0,y = 0,t = 0;
    for(int i=0;i<N;i++){
        //cout << i << "回目" << endl;
        fla = false;
        process(x,y,t,i);
        if(!fla){
            break;
        }
        x = table[i].x;
        y = table[i].y;
        t = table[i].t;
    }
}
int main(void){
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> table[i].t >> table[i].x >> table[i].y;
    }
    flag();
    if(fla){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
}