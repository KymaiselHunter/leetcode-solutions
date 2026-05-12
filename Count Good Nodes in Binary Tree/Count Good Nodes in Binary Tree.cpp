/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int goodNodes(TreeNode* root) {
        return recur(root, -1);
    }

    int recur(TreeNode * it, int pMax){
        if(it == nullptr) return 0;

        bool add = true;
        if(it->val < pMax) add = false;

        return recur(it->left, max(it->val, pMax)) 
        + recur(it->right, max(it->val, pMax)) + add;
    }
};