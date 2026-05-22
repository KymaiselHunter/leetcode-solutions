class Solution {
public:
    string reverseWords(string s) {
        string output = "";
        string hold;
        for(int i = 0; i < s.size(); i++)
        {
            // cout << i << " " << s[i] << " h:" << hold  << " o:" << output << endl;
            if(hold.empty() && s[i] == ' ') 
            {
                continue;
            }

            if(s[i] != ' ')
            {
                hold += s[i];
                continue;
            }

            if(!output.empty()) hold += ' ';
            output = hold + output;
            hold = "";
        }
        if(hold.empty()) return output;

        if(!output.empty()) hold += ' ';
        output = hold + output;

        return output;
    }
};