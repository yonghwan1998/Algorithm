#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> umap;
    
    for (int i = 0; i < participant.size(); i++) {
        if (umap.count(participant[i]) > 0) {
            umap[participant[i]]++;
        } else {
            umap[participant[i]] = 1;
        }
    }
    
    for (int j = 0; j < completion.size(); j++) {
        if (umap[completion[j]] > 0) {
            umap[completion[j]]--;
        }
    }
    
    for (const auto& [k, v] : umap) {
        if (v == 1) {
            answer = k;
            break;
        }
    }
    
    return answer;
}