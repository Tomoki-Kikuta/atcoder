#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int N;
long int alfa[5]={0};
long int count(void){
    long int count = 0;
    for(int i=0;i<3;i++){
        for(int j=i+1;j<4;j++){
            for(int u=j+1;u<5;u++){
                count += alfa[i] * alfa[j] * alfa[u];
            }
        }
    }
    return count;
}
int main(void){
    cin >> N;
    for(int i=0;i<N;i++){
        string name;
        cin >> name;
        if(name[0]=='M'){
            alfa[0]++;
        }else if(name[0]=='A'){
            alfa[1]++;
        }else if(name[0]=='R'){
            alfa[2]++;
        }else if(name[0]=='C'){
            alfa[3]++;
        }else{
            alfa[4]++;
        }
    }
    cout << count() << endl;
    return 0;
}