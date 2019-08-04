#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#define MAX 5001
using namespace std;
string s;
int K;
vector<string> S;
void process(void){
    int mi;
    if(s.length()<K){
        mi = s.length();
    }else{
        mi = K;
    }
    for(int i=1;i<=mi;i++){
        int j = 0;
        while(j+i<=s.size()){
            string word;
            int t = j;
            while(word.length()!=i){
                word += s[t];
                t++;
            }   
            //cout << word << endl;
            bool ok = true;
            for(int t=0;t<S.size();t++){
                if(S[t]==word){
                    ok = false;
                    break;
                }
            }
            if(ok){
                S.push_back(word);
            }
            j++;
        }
    }
}
string count(void){
    sort(S.begin(),S.end());
    return S[K-1];
}
int main(void){
    cin >> s >> K;
    process();
    cout << count() << endl;
    return 0;
}