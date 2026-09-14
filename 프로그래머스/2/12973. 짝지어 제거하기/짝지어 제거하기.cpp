#include <string>
#include <stack>

using namespace std;

int solution(string s)
{
    int answer = -1;
    stack<char> stack_char;
    
    for (char c : s) {
        if (!stack_char.empty()) {
            char stack_top = stack_char.top();
            
            if (stack_top == c) {
                stack_char.pop();
            } else {
                stack_char.push(c);
            }
        } else {
            stack_char.push(c);
        }
    }
    
    if (stack_char.empty()) {
        answer = 1;
    } else {
        answer = 0;
    }

    return answer;
}