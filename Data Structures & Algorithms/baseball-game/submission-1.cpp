class Solution {
public:
    int calPoints(vector<string>& operations) {
        int res = 0;
        stack<int> st;

        for (auto &o: operations) {
            if (o == "+") {
                int f = st.top();
                st.pop();

                int s = st.top();
                st.push(f);

                res += (f + s);
                st.push(f+s);
            } else if (o == "C") {
                res -= st.top();
                st.pop();

            } else if (o == "D") {
                int d = 2 * st.top();
                res += d;
                st.push(d);
            } else {
                int n = stoi(o);
                res += n;
                st.push(n);
            }

            if(!st.empty())
            cout << "top=" << st.top() << " ";
        }


        return res;
    }
};