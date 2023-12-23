#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - Infinite loop
 * Return: zero
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Entry point
 *
 * Return: Always zero on succes
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
			exit(1);

		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
