class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> cache;

        for(int i = 0; i < nums.size(); i++)
        {
            if(cache.contains(target-nums[i]))
            {
                return {cache[target-nums[i]], i};
            }
            cache[nums[i]] = i;
        }
        return {-1,-1};
    }
};