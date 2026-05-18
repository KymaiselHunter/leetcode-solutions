class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> s;

        for(int i = 0; i < asteroids.size(); i++)
        {
            int curr = asteroids[i];
            if(curr > 0 || s.empty())
            {
                s.push(curr);
                continue;
            }
            while(!s.empty())
            {
                int top = s.top();
                if(top < 0)
                {
                    s.push(curr);
                    break;
                }
                if(top > abs(curr)) break;
                s.pop();
                if(top == abs(curr)) break;
                if(s.empty())
                {
                    s.push(curr);
                    break;
                }
            }
        }
        vector<int> output;

        while(!s.empty())
        {
            output.insert(output.begin(), s.top());
            s.pop();
        }
        return output;
    }
};