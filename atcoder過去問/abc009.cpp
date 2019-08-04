#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(void){
    int n,k,count=0,change=0,color[100]={0};
    string S;
    cin >> n >> k >> S;
    while(count < n){
        int min_a = 1000000000;
        int min_b = 1000000000;
        int min_id;
        int min_index;
        for(int i=count;i<n;i++){
            int a = S[i] - '0';
            if(a < min_a){
                    min_a = a;
                    min_id = i;
                }
            if(color[i]==1){
                if(a < min_b){
                    min_b = a;
                    min_index = i;
                }
            }
        }
        if(count!=min_id){
            if(color[min_id]==0 && color[count]==0 && change < k - 1){
                change += 2;
                swap(S[min_id],S[count]);
                color[min_id] = 1;
                color[count] = 1;
            }else if(color[min_id]==0 && color[count]==0 && change == k - 1){
                change++;
                swap(S[count],S[min_index]);
                color[min_index] = 1;
                color[count] = 1;
            }else if(((color[min_id]==1 && color[count]== 0) || (color[min_id]==0 && color[count]==1)) && change < k){
                change ++;
                swap(S[min_id],S[count]);
                color[min_id] = 1;
                color[count] = 1;
            }else if(color[min_id]==0 && color[count]==1 && change >=k){
                swap(S[count],S[min_index]);
            }
            else if(color[min_id]==1 && color[count]== 1){
                swap(S[min_id],S[count]);
            }
        }
        // cout << change << " " << S << endl;
        count++;
    }
    cout << S << endl;
    return 0;
}
