#include "lists.h"

/**
 * check_cycle - checks if a lined list is circular
 * @list: linked list to check
 * Return: 1 if list is circular, 0  if no lopp
 */

int check_cycle(listint_t *list)
{
	listint_t *s1 = list, *s2 = list;

	while (s1 && s2 && (*s2).next)
	{
		s1 = (*s1).next;
		s2 = (*(*s2).next).next;
		if (s1 == s2)
			return (1);
	}
	return (0);
}
