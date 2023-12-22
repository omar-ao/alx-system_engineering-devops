#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		printf("Zombie process created, PID: %d\n", pid);
		if (pid == 0)
			exit(1);
	}
}
