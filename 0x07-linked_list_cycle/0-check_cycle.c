#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);
	slow = list;
	fast = list;

	while (slow->next && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (!fast)
			return (0);
		if (slow == fast)
			return (1);
	}
	return (0);
}
