#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(void){
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        int count = 0;
        string word;
        cin >> word;
        if(word.length()>=5){
            int j = 0;
            while(j<=word.length()-5){
                if(word[j]=='t' && word[j+1]=='o' && word[j+2]=='k' && word[j+3]=='y' && word[j+4]=='o'){
                    count++;
                    j += 4;
                }else if(word[j]=='k' && word[j+1]=='y' && word[j+2]=='o' && word[j+3]=='t' && word[j+4]=='o'){
                    count++;
                    j += 4;
                }
                j++;
            }
        }
        cout << count << endl;
    }
    return 0;
}