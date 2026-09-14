#include<string>
#include <stack>

using namespace std;

bool solution(string s)
{
    stack<char> stack_temp;
    
    for (char c : s) {
        if (c == '(' || c == '{') {
            stack_temp.push(c);
        } else {
          if (stack_temp.empty()) return false;
            
          if (c == ')' && stack_temp.top() == '(') {
            stack_temp.pop();
          } else if (c == '}' && stack_temp.top() == '{') {
            stack_temp.pop();
          } else {
            return false;
          }
        }
    }

    return stack_temp.empty();
}