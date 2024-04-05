#include <stdio.h>
#include <ctype.h>

void change(char x[100], char y[50])
{
	for (int j = 0; y[j] != '\n'; j++){
	        for (int i = 0; x[i] != '\0'; i++){
			if (ispunct(x[i])){
				x[i] = y[j];
			}
		}
	}
	printf("Result : %s\n",x);
}

int main()
{
	char str[100],key[50];
	printf("Enter string : ");
	fgets(str,100,stdin);
	printf("Enter key : ");
	fgets(key,50,stdin);
	change(str,key);
}
