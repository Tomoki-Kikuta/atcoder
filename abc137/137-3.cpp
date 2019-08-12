#include<iostream>
#include<algorithm>
#include<string>
#define MAX 100005
using namespace std;
int main(void){
    int N;
    long int count = 0;
    string s[MAX];
    cin >> N;
    for(int i=0;i<N;i++){
        string a;
        cin >> a;
        sort(a.begin(),a.end());
        s[i] = a;
    }
    sort(s,s+N);
    for(int i=0;i<N;i++){
        long int c = 0;
        int u = i;
        while(s[i]==s[u]){
            c++;
            u++;
        }
        count += ( c * (c - 1) ) / 2;
        i = u - 1; 
    }
    cout << count << endl;
    return 0;
}