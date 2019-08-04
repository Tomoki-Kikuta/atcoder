#include<iostream>
#include<algorithm>
#define MAX 101
using namespace std;
struct Parcel{
    int x;
    int y;
};
int N;
Parcel red[MAX];
Parcel blue[MAX];
int count(void){
    int count = 0;
    return count;
}
int main(void){
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> red[i].x >> red[i].y;
    }
    for(int i=0;i<N;i++){
        cin >> blue[i].x >> blue[i].y;
    }
    cout << count() << endl;
    return 0;
}