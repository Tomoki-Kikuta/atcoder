#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;
int main(void){
    int N,K,max_sequence=0;
    vector<int> max_candidate;
    vector<char> id;
    string S;
    cin >> N >> K >> S;
    int count = 0;
    max_candidate.push_back(count);
    id.push_back('9');
    for(int i=0;i<N;i++){
        char A = S[i];
        while(S[i]==A){
            count++;
            i++;
            if(i==N){
                break;
            }
        }
        i--;
        id.push_back(A);
        max_candidate.push_back(count);
    }
    for(int i=1;i<id.size();i++){
        int c;
        //cout << id[i] << ' ';
        //cout << max_candidate[i] << endl;
        if(id[i]=='0'){
            if(K * 2 - 1 + i < max_candidate.size()){
                if(i>=2){
                    c = max_candidate[K * 2 - 1 + i] - max_candidate[i-2];
                }else{
                    c = max_candidate[K * 2 - 1 + i] - max_candidate[i-1];
                }
            }else{
                if(i>=2){
                    c = max_candidate.back() - max_candidate[i-2];
                }else{
                    c = max_candidate.back() - max_candidate[i-1];
                }
            }
        }else{
            if( K * 2 + i  < max_candidate.size()){
                c = max_candidate[K * 2 + i] - max_candidate[i-1];
            }else{
                c = max_candidate.back() - max_candidate[i-1];
            }
        }
        //cout << c  << endl;
        max_sequence = max(max_sequence,c);
    }
    cout << max_sequence << endl;
    return 0;
}