#include<iostream>
#include<algorithm>
#include<vector>
#define MAX 100001
using namespace std;
struct Change_candidate{
    int B;
    long int C;
    Change_candidate(int inputted_B, long int inputted_C)
    {
        B = inputted_B;
        C = inputted_C;
    }
    bool operator< (const Change_candidate &another) const
    {
        return C < another.C;
    };
};
int main(void){
    int N,M;
    long int count = 0;
    vector<long int>  A;
    vector<Change_candidate> T;
    cin >> N >> M;
    for(int i=0;i<N;i++){
        long int a;
        cin >> a;
        A.push_back(a);
    }
    sort(A.begin(),A.end());
    for(int i=0;i<M;i++){
        int t;
        long int s;
        cin >> t >> s;
        T.push_back(Change_candidate(t,s));
    }
    sort(T.begin(),T.end());
    int j = M - 1;
    for(int i=0;i<N;i++){
        if(A[i]<T[j].C){
            if(T[j].B!=0){
                A[i] = T[j].C;
                T[j].B--;
                if(T[j].B==0){
                    j--;
                    if(j==-1){
                        break;
                    }
                }
            }
        }else{
            break;
        }
    }
    for(int i=0;i<N;i++){
        count += A[i];
    }
    cout << count << endl;
    return 0;
}