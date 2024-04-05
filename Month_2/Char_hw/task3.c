#include <stdio.h>
#include <ctype.h>
#include <limits.h> 

int count(char x[100])
{
	int count = 0;
	int min = INT_MAX;
	for (int i = 0; x[i] != '\0'; i++)
	{
		if (isalpha(x[i])){	
			count++;
			continue;
		} else {
			if (min > count && count != 0){
				min = count;
			}
			count = 0;
		}
		
	}
	printf("Eng kalta so'z: %d\n",min);
}

int main()
{
	char str[100];
	printf("Enter str : ");
	fgets(str,100,stdin);
	count(str);
}
