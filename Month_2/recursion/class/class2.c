#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool check(char x[100],char y)
{
    for (int i = 0; i < strlen(x); i++){
        if (x[i] == y)
            return true;
    }
    return false;
}

int count_char(char x[100],char y)
{
    int count = 0;
    for (int i = 0; i < strlen(x); i++){
        if (x[i] == y)
            count++;
    }
    return count;
}

int main()
{
    char str[1000] ,res[1000];
    int index = 0;
    printf("Enter string : ");
    fgets(str,100,stdin);
    str[strlen(str) - 1] = '\0';
    for (int i = 0; i < strlen(str); i++){
        if (check(res,str[i]) == false){
            res[index++] = str[i];
            printf("%c - dan %d ta bor!\n",str[i],count_char(str,str[i]));
        }
    }
}
