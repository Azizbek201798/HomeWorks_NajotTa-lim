#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void getRandPassword(int n)
{
	char s[100],d;
	int index = 0;
	for (int i = 0; index < n; i++){
	        d = rand()%(122 - 48 + 1) + 48;
		if (d >= 48 && d <= 57 || d >= 65 && d <= 90 || d >= 97 || d <= 122){
			s[index] = d;
			index++;
		} else {
			continue;
		}
	}
	s[index] = '\0';
	puts(s);
}

int main()
{
	srand(time(NULL));
	int size;
	printf("Password chegarasini kiriting : ");
	scanf("%d",&size);
	getRandPassword(size);
	return 0;
}
