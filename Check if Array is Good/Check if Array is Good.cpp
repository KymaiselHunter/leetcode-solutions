class Solution {
public:
    bool isGood(vector<int>& nums) {
        int biggest = nums.size()-1;
        int bigs = 0;

        unordered_set<int> found;

        for(int i = 0; i < nums.size(); i++)
        {
            int curr = nums[i];

            if(curr < 1 || curr > biggest) return false;

            if(curr != biggest)
            {
                if(found.count(curr) > 0) return false;
                found.insert(curr);
                continue;
            }
            bigs += 1;

            if(bigs > 2) return false;
        }

        return true;
    }
};