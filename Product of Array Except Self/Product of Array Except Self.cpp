class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> pre(len, 1);
        vector<int> po(len, 1);

        int prev = 1;
        int pov = 1;
        
        for(int i = 0; i < len; i++)
        {
            pre[i] *= nums[i] * prev;
            po[len - i - 1] *= nums[len - i - 1] * pov;

            prev = pre[i];
            pov = po[len - i - 1];
        }


        for(int i = 0; i < len; i++)
        {
            nums[i] = 1;
            
            if(i > 0) nums[i] *= pre[i-1];
            if(i < len-1) nums[i] *= po[i+1];
        }

        return nums;
    }
};