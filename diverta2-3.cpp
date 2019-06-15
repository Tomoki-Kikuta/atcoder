#include<iostream>
#include<algorithm>
#include<vector>
#define MAX 100005
using namespace std;
int main(void){
    int n,A[MAX],count,minus=0;
    vector<pair<int,int> > combination;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> A[i];
    }
    sort(A,A+n);
    count = A[n-1];
    for(int i=n-2;i>=0;i--){
        if(A[i]<0){
            combination.push_back(make_pair(count,A[i]));
            count -= A[i];
        }else if(A[i]>=0 && i!=0){
            combination.push_back(make_pair(A[0],A[i]));
            A[0] -= A[i];
        }else{
            combination.push_back(make_pair(count,A[i]));
            count -= A[0];
        }
    }
    cout << count << endl;
    count = A[n-1];
    for(int i=0;i<combination.size();i++){
        cout << combination[i].first << ' ' << combination[i].second << endl;
    }
    return 0;
}