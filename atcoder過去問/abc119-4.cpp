#include<iostream>
#include<algorithm>
#include<vector>
#define MAX 100005
#define INF 1<<21
using namespace std;
int main(void){
    int A,B,Q;
    vector<long int> s;
    vector<long int> t;
    cin >> A >> B >> Q;
    for(int i=0;i<A;i++){
        long int S;
        cin >> S;
        s.push_back(S);
    }
    for(int i=0;i<B;i++){
        long int T;
        cin >> T;
        t.push_back(T);
    }
    for(int i=0;i<Q;i++){
        long int answer,x;
        cin >> x;
        answer = INF;
        vector<long int> ::iterator a = lower_bound(s.begin(),s.end(),x);
        vector<long int> ::iterator b = upper_bound(s.begin(),s.end(),x);
        vector<long int> ::iterator c = lower_bound(t.begin(),t.end(),x);
        vector<long int> ::iterator d = upper_bound(t.begin(),t.end(),x); 
        long int A[] = {*a,*b};
        long int B[] = {t[*c],t[*d]};
        cout << a << ' ' << b << endl;
        for(long int S=0;S<=1;S++){
            for(long int T=0;T<=1;T++){
                long int d_1 = abs(A[S] - x) + abs(B[T] - A[S]);
                long int d_2 = abs(B[T] - x) + abs(A[S] - B[T]);
                long int d = min(d_1,d_2);
                answer = min(answer,d);
            }
        }
        cout << answer << endl;
    }
    return 0;
}