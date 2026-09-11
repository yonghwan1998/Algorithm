#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> cnt(3);
    
    // 1번 수포자
    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == i % 5 + 1) {
            cnt[0]++;
        }
    }
    
    // 2번 수포자
    for (int j = 0; j < answers.size(); j++) {
        // 0,2,4,6 => 2
        // 1 => 1
        // 3 => 3
        // 5 => 4
        // 7 => 5
        if (j % 2 == 0 && answers[j] == 2) {
            cnt[1]++;
        } else if (j % 8 == 1 && answers[j] == 1) {
            cnt[1]++;
        } else if (j % 8 == 3 && answers[j] == 3) {
            cnt[1]++;
        } else if (j % 8 == 5 && answers[j] == 4) {
            cnt[1]++;
        } else if (j % 8 == 7 && answers[j] == 5) {
            cnt[1]++;
        }
    }
    
    // 3번 수포자
    for (int k = 0; k < answers.size(); k++) {
        // 0,1 => 3
        // 2,3 => 1
        // 4,5 => 2
        // 6,7 => 4
        // 8,9 => 5
        if ((k % 10 == 0 || k % 10 == 1) && answers[k] == 3) {
            cnt[2]++;
        } else if ((k % 10 == 2 || k % 10 == 3) && answers[k] == 1) {
            cnt[2]++;
        } else if ((k % 10 == 4 || k % 10 == 5) && answers[k] == 2) {
            cnt[2]++;
        } else if ((k % 10 == 6 || k % 10 == 7) && answers[k] == 4) {
            cnt[2]++;
        } else if ((k % 10 == 8 || k % 10 == 9) && answers[k] == 5) {
            cnt[2]++;
        }
    }
    
    int max_cnt = *max_element(cnt.begin(), cnt.end());

    int index = 1;
    for (int n : cnt) {
        if (n == max_cnt) {
            answer.push_back(index);
        }
        index++;
    }
    
    return answer;
}