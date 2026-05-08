class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sMp;
        unordered_map<char, int> tMp;

        if(s.size() != t.size()) return false;

        for(int i = 0; i < s.length(); i++)
        {
            sMp[s[i]]++;
            tMp[t[i]]++;
        }

        if(sMp != tMp) return false;
        return true;
    }
};