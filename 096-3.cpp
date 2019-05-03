#include <iostream>
#define MAX 52
using namespace std;
int main() {
    int H,W;
    bool flag = true;
    char c[MAX][MAX];
	cin >> H >> W;
	for (int i=0;i<=H+1;i++) {
		for (int j=0;j<=W+1;j++){
            if(i==0 || j==0 || i==H+1 || j==W+1){
                c[i][j] = '.';
                continue;
            }
            cin >> c[i][j];
        }
	}
	for(int i=1;i<=H;i++) {
		for(int j=1; j<=W;j++) {
			if(c[i][j] == '#' && c[i][j - 1] != '#' && c[i - 1][j] != '#' && c[i][j + 1] != '#' && c[i + 1][j] != '#'){
                flag = false;
                break;
            }
		}
	}
	if (flag){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
	return 0;
}
