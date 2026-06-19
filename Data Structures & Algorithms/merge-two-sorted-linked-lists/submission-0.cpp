/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *res = NULL, *h = NULL;

        while (list1 != NULL && list2 != NULL) {
            if (list1->val <= list2->val) {
                if (res == NULL) {
                    res = new ListNode(list1->val);
                    h = res;
                } else {
                    res->next = new ListNode(list1->val);
                    res = res->next;
                }
                list1 = list1->next;
            } else {
                if (res == NULL) {
                    res = new ListNode(list2->val);
                    h = res;
                } else {
                    res->next = new ListNode(list2->val);
                    res = res->next;
                }

                list2 = list2->next;
            }
        }

        while (list1 != NULL) {
            if (res == NULL) {
                    res = new ListNode(list1->val);
                    h = res;
                } else {
                    res->next = new ListNode(list1->val);
                    res = res->next;
            }
            list1 = list1->next;
        }

        while (list2 != NULL) {
            if (res == NULL) {
                    res = new ListNode(list2->val);
                    h = res;
                } else {
                    res->next = new ListNode(list2->val);
                    res = res->next;
            }
            list2 = list2->next;
        }

        return h;
    }
};
