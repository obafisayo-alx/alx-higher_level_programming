#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - insert a next_node.
* @head: head of the list
* @number: number to add
* Return:  the address of the new next_node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *next_node;
	listint_t *new_next_node;

	new_next_node = malloc(sizeof(listint_t));
	if (!head || !(*head))
	{
		new_next_node->n = number;
		new_next_node->next = NULL;
		*head = new_next_node;
		return (new_next_node);
	}
	next_node = *head;
	if (!new_next_node)
	{
		free(new_next_node);
		return (NULL);
	}
	if (number <= next_node->n)
	{
		new_next_node->n = number;
		new_next_node->next = next_node;
		next_node = new_next_node->next;
		*head = new_next_node;
		return (new_next_node);
	}
	while (next_node)
	{
		if (!next_node->next)
			return (add_nodeint_end(head, number));
		if ((number > next_node->n) && (number <= (next_node->next)->n))
		{
			new_next_node->n = number;
			new_next_node->next = next_node->next;
			next_node->next = new_next_node;
			return (new_next_node);
		}
		next_node = next_node->next;
	}
	free(new_next_node);
	return (NULL);
}
