#include <string>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;
    
    for (int i = 0; i < progresses.size(); i++) {
        q.push(ceil((100.0 - progresses[i]) / speeds[i]));
    }
    
    while (!q.empty()) {
        int deployDay = q.front();
        q.pop();
        
        int cnt = 1;
        
        while (!q.empty() && q.front() <= deployDay) {
            q.pop();
            cnt++;
        }
        
        answer.push_back(cnt);
    }
    
    return answer;
}