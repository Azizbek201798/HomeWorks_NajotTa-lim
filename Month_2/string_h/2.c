#include <stdio.h>
#include <string.h>

int main()
{
    char str[100] = "Day after tomorrow";
    for (int i = strlen(str) - 1; i >= 0; i--){
        printf("%c",str[i]);
    }    
    puts("");
}