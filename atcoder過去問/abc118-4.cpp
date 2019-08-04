#include<iostream>
#include<algorithm>
#define MAX 10
using namespace std;

int match_number(int number){
    if(number==1){
        return 2;
    }else if(number==2){
        return 5;
    }else if(number==3){
        return 5;
    }else if(number==4){
        return 4;
    }else if(number==5){
        return 5;
    }else if(number==6){
        return 6;
    }else if(number==7){
        return 3;
    }else if(number==8){
        return 7;
    }else{
        return 6;
    }
}

int match_rule(int A[MAX], int M){
    int min_number = A[0];
    int min_match_number = match_number(A[0]);
    for(int i=1;i<M;i++){
        int now_match_number = match_number(A[i]);
        if(now_match_number < min_match_number || (now_match_number == min_match_number && min_number < A[i])){
            min_number = A[i];
            min_match_number = now_match_number;
        }
    }
    return min_number;
}

string cal_digit(int number, int N){
    string digit = "";
    int use_match = match_number(number);
    while(N - use_match >= 0){
        digit += number;
        N -= use_match;
    }
    return digit;
}

int main(void){
    int N,M,A[MAX];
    cin >> N >> M;
    for(int i = 0;i<M;i++){
        cin >> A[i];
    }
    int min_num = match_rule(A,M);
    string num_digit = cal_digit(min_num,N);
    cout << num_digit.c_str() << endl;
    return 0;
}