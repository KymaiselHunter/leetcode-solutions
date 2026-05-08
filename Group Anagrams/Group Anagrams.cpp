class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;

        for(string s : strs)
        {
            string key = s;
            sort(key.begin(), key.end());

            mp[key].push_back(s);
        }

        vector<vector<string>> output;

        for(auto pair : mp)
        {
            output.push_back(pair.second);
        }
        return output;
    }
};