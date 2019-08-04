#include<iostream>
#include<algorithm>
using namespace std;
int main(void){
    pair<pair<string,int>,int> key[101];
    int N;
    cin >> N;
    for(int i=0;i<N;i++){
        string s;
        int p,id;
        cin >> s >> p;
        id = i;
        key[i] = make_pair(make_pair(s,-p),id);
    }
    sort(key,key+N);
    for(int i=0;i<N;i++){
        cout << key[i].second + 1 << endl;
    }
    return 0;
}