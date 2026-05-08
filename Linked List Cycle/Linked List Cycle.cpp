/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (!head || !head->next)
        {
            return false;
        }
        ListNode * it = head->next;

        while (head && it)
        {
            if(head == it) return true;
            head = head->next;
            it = it->next;
            if(!it) return false;
            it = it->next;
        }
        return false;
    }
};