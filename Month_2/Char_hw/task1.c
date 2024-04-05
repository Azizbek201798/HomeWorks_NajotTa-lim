#include <stdio.h>
#include <ctype.h>

void DigitsSum(char x[100])
{
	int sum = 0;
	for (int i = 0; x[i] != '\0'; i++){
		if(isdigit(x[i])){
			sum += x[i] - '0';
		}
	}
	printf("Sum of digits : %d\n",sum);
}

int main()
{
	char str[100];
	printf("Enter string : ");
	fgets(str,sizeof(str),stdin);
	DigitsSum(str);
}
