#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

/**
 * infinite_while - an infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (true)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates the zombie processes
 * Return: 0
 */
int main(void)
{
	int i;
	int zombie_pid;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (!zombie_pid)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie_pid);
	}

	infinite_while();
	return (0);
}

