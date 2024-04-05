#include <stdio.h>
#include <ctype.h>

void countChar(char x[100])
{
	int count = 0;
	for (int i = 0; x[i] != 0; i++){
		if (isalpha(x[i])){
			count++;
		}
	}
	printf("%d ta harf mavjud!\n",count);
}

int main()
{
	char str[100];
	printf("Enter str : ");
	fgets(str,100,stdin);
	countChar(str);
}
