class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char &ch: s) {
            if (st.empty()) st.push(ch);
            else {
                char t = st.top();
                if ((t == '{' && ch == '}') or (t == '[' && ch == ']') or (t == '(' && ch == ')')) st.pop();
                else st.push(ch);
            }
        }

        return st.empty();
    }
};
