#include <iostream>
using namespace std;
int main()
{
    int N,A;
    cin >> N;
    A = N;
    int s[1000] = {0},l = 0;
    if(N == 0){
        cout << 0 << endl;
    }else{
        while(A!=0){
        int r = A % -2;
        A /= -2;
        if(r < 0){
            r += 2;
            A += 1;
        }
        s[l] = r;
        l++;
    } 
    for(int i = l-1; i >= 0; --i){
        cout << s[i];
    }
    cout << endl;
    }
    return 0;
}
