class MyQueue {
public:
    stack<int> q;

    MyQueue(): q() {}
    
    void push(int x) {
        q.push(x);
    }
    
    int pop() {
        vector<int> temp;
        while(q.size() != 1) {
            temp.push_back(q.top());
            q.pop();
        }

        int k = q.top();
        q.pop();

        for(int i = temp.size() - 1; i >= 0; i --) q.push(temp[i]);

        return k;
    }
    
    int peek() {
        vector<int> temp;
        while (q.size() > 1) {
            temp.push_back(q.top());
            q.pop();
        }
        int k = q.top();
        temp.push_back(k);
        q.pop();

        for(int i = temp.size() - 1; i >= 0; i --) q.push(temp[i]);
        return k;

    }
    
    bool empty() {
        return q.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */