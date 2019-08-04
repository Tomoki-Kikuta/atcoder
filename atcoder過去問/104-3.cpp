#include<iostream>
#include<vector>
#define INF 1<<21
using namespace std;
struct  Table{
    int p;
    int c;
    int s;
};
int D;
long int G;;
Table table[10];
bool yn[10] = {0};
vector<int> count_N;
void process(int i,long int score,int count){
    if(i<D){
        process(i+1,score,count);
        score += table[i].c + table[i].s * table[i].p;
        count += table[i].p;
        yn[i] = true;
        process(i+1,score,count);
    }else{
        int sum = 0,bigest_id;
        bool flag = true;
        for(int j=D-1;j>=0;j--){
            if(!yn[j]){
                bigest_id = j;
                break;
            }else{
                yn[j] = false;
            }
        }
        while(score<G){
            score += table[bigest_id].s;
            sum++;
            if(sum>table[bigest_id].p-1){
                flag = false;
                break;
            }
        }
        if(flag){
            count += sum;
            count_N.push_back(count);
        }
    }
}
int min(void){
    int min = INF;
    for(int i=0;i<count_N.size();i++){
        if(min>count_N[i]){
            min = count_N[i];
        }
    }
    return min;
}
int main(void){
    cin >> D >> G;
    for(int i=0;i<D;i++){
        cin >> table[i].p >> table[i].c;
        table[i].s = 100 * (i+1);
    }
    process(0,0,0);
    cout << min() << endl;
    return 0;
}