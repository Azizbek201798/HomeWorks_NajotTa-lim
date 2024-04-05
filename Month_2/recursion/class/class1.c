#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    int index = 0, sum;
    char ifoda[1000],str[1000];
    printf("Enter Ifoda : ");
    fgets(ifoda,1000,stdin);
    strcpy(str,ifoda);
    char *tok = strtok(ifoda,"+-");
    sum = atoi(tok);

    while (1)
    {
        index += strlen(tok);
        tok = strtok(NULL,"+-");
        if (tok == NULL)
            break;
        if (str[index] == '+')
        {
            sum += atoi(tok);
        } else if (str[index] == '-'){
            sum -= atoi(tok);
        }
        index ++;
    }
    printf("Summa = %d\n",sum);
}


