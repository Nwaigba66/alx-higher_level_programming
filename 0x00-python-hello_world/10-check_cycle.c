#include <stddef.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int check_cycle(struct ListNode *list)
{
    struct ListNode *slow = list;
    struct ListNode *fast = list;
    
    while (fast != NULL && fast->next != NULL)
	{
        slow = slow->next;
        fast = fast->next->next;
        
        if (slow == fast) {
            return 1;
        }
    }
    
    return 0;
}

