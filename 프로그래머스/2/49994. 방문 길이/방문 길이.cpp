#include <string>

using namespace std;

int solution(string dirs) {
    int answer = 0;
    
    int dx[] = {1, -1, 0, 0};
    int dy[] = {0, 0, -1, 1};
    
    // 좌표 평면 그리기
    bool board[11][11][4] = {false, };
    
    // 초기값
    int x = 5;
    int y = 5;
    
    // dirs만큼 for
    for (char d : dirs) {
        int direction;
        // d값으로 nx, ny 구하기
        if (d == 'U') {
            direction = 0;
        } else if (d == 'D') {
            direction = 1;
        } else if (d == 'L') {
            direction = 2;
        } else if (d == 'R') {
            direction = 3;
        }
        
        int nx = x + dx[direction];
        int ny = y + dy[direction];
        
        // 범위를 벗어난 경우
        if (nx < 0 or nx > 10 or ny < 0 or ny > 10) continue;
        
        // 반대 방향 계산
        int opposite_direction;
        if (d == 'U') {
            opposite_direction = 1;
        } else if (d == 'D') {
            opposite_direction = 0;
        } else if (d == 'L') {
            opposite_direction = 3;
        } else if (d == 'R') {
            opposite_direction = 2;
        }
        
        // 이미 지나온 길
        if (board[x][y][direction] == true || board[nx][ny][opposite_direction] == true) {
            x = nx;
            y = ny;
            continue;
        }
        
        board[x][y][direction] = true;
        board[nx][ny][opposite_direction] = true;

        x = nx;
        y = ny;
        answer += 1;
    }
    
    return answer;
}