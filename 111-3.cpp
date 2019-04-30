#include<iostream>
#include<algorithm>
#define MAX 100001
using namespace std;
int main(void){
    int n,v[MAX],color_2[MAX]={0},color_1[MAX]={0},cost=0,count=0,max_1,max_2,max_3,max_4,id_1,id_2,id_3,id_4;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> v[i];
    }
    int u = 1;
    while(v[u]==v[0]){
        if(u==n-1 && v[u]==v[0]){
            cout << n/2 << endl;
            return 0;
        }else{
            u++;
        }
    }
    for(int i=0;i<n;i++){
        if(i%2==0){
            color_1[v[i]]++;
        }else{
            color_2[v[i]]++;
        }
    }
    id_1 = 1;
    id_2 = 1;
    id_3 = 2;
    id_4 = 2;
    max_1 = color_1[1];
    max_3 = color_1[2];
    max_2 = color_2[1];
    max_4 = color_2[2]; 
    if(max_1<max_3){
        swap(max_1,max_3);
        swap(id_1,id_3);
    }
    if(max_2<max_4){
        swap(max_2,max_4);
        swap(id_2,id_4);
    }
    for(int i=1;i<=MAX;i++){
        if(max_1<color_1[i]){
            max_3 = max_1;
            id_3 = id_1;
            max_1 = color_1[i];
            id_1 = i;
        }else if(max_3<color_1[i]){
            max_3 = color_1[i];
            id_3 = i;
        }
        if(max_2<color_2[i]){
            max_4 = max_2;
            id_4 = id_2;
            max_2 = color_2[i];
            id_2 = i;
        }else if(max_4<color_2[i]){
            max_4 = color_2[i];
            id_4 = i;
        }
    }
    if(id_1!=id_2){
        for(int i=0;i<n;i++){
            if(i%2==0 && v[i]!=id_1){
                cost++;
            }else if(i%2!=0 && v[i]!=id_2){
                cost++;
            }
        }
        cout << cost << endl;
    }else{
        for(int i=0;i<n;i++){
            if(i%2==0 && v[i]!=id_1){
                cost++;
            }else if(i%2!=0 && v[i]!=id_4){
                cost++;
            }
        }
        for(int i=0;i<n;i++){
            if(i%2==0 && v[i]!=id_3){
                count++;
            }else if(i%2!=0 && v[i]!=id_2){
                count++;
            }
        }
        if(count>cost){
            cout << cost << endl;
        }else{
            cout << count << endl;
        }
    }
    return 0;
}