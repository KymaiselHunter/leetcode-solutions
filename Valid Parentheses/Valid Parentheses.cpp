class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> mp
        {
            {'(',')'},
            {'[',']'},
            {'{','}'}
        };

        for(int i = 0; i < s.length(); i++)
        {
            char curr = s[i];
            // if current is a key
            if(mp.count(curr) > 0)
            {
                st.push(curr);
                continue;
            }
            // not a key, check for pop
            if(st.size() <= 0) return false;
            char top = st.top();
            st.pop();

            if(mp[top] != curr) return false;
        }

        if(st.size() > 0) return false;
        return true;
    }
};