#include<iostream>
#include<algorithm>
#include<stack>
#define MAX 505
#define ROAD 0
#define WALL -1
using namespace std;

bool can(int height,int widge,int maze[MAX][MAX],int start_x,int start_y,int goal_x,int goal_y){
    int color = 1;
    stack<pair<int,int> > go;
    go.push(make_pair(start_x,start_y));
    while(!go.empty()){
        int now_x = go.top().first;
        int now_y = go.top().second;
        go.pop();
        maze[now_x][now_y] = color;
        if(now_x == goal_x && now_y == goal_y){
            break;
        }
        for(int x=-1;x<=1;x++){
            for(int y=-1;y<=1;y++){
                if((x+y)%2==0){
                    continue;
                }
                int next_x = now_x + x;
                int next_y = now_y + y;
                if(maze[next_x][next_y]==ROAD){
                    go.push(make_pair(next_x,next_y));
                }
            }
        }
    }
    return maze[goal_x][goal_y];
}
int main(void){
    int height,widge,maze[MAX][MAX],start_x,start_y,goal_x,goal_y;
    cin >> height >> widge;
    for(int i=0;i<=height+1;i++){
        maze[i][0] = WALL;
        maze[i][widge + 1] = WALL;
    }
    for(int i=0;i<=widge+1;i++){
        maze[0][i] = WALL;
        maze[height+1][i] = WALL;
    }
    for(int i=1;i<=height;i++){
        for(int j=1;j<=widge;j++){
            char a;
            cin >> a;
            if(a=='s'){
                start_x = i;
                start_y = j;
            }else if(a=='g'){
                goal_x = i;
                goal_y = j;
            }else if(a=='#'){
                maze[i][j] = WALL;
            }else{
                maze[i][j] = ROAD;
            }
        }
    }
    if(can(height,widge,maze,start_x,start_y,goal_x,goal_y)){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
}