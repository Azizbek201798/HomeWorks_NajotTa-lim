#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

int countNumber(char x[100])
{
	bool raqam = false;
	int count = 0;
	for (int i = 0; x[i] != '\n'; i++){
		if (isdigit(x[i])){
			raqam = true;
			continue;
		} else {
			if (raqam == true){
				count ++;
				raqam = false;
			}
		}
	}
	return ++count;
}
// Azizbek bugungi sana 18.02.2017 demak 200 top;

int main()
{
	char str[100];
	printf("Enter string: ");
	fgets(str,100,stdin);
	printf("%d - ta son mavjud!\n",countNumber(str));
}

