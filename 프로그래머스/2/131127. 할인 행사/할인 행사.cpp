#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    
    unordered_map<string, int> wantMap;
    
    for (int i = 0; i < want.size(); i++) {
        wantMap[want[i]] = number[i];
    }
    
    for (int i = 0; i < discount.size() - 9; i++) {
        unordered_map<string, int> discountMap;
        
        for (int j = 0; j < 10; j++) {
            discountMap[discount[i + j]] += 1;
        }
        
        if (wantMap == discountMap) answer++;
    }
    
    return answer;
}