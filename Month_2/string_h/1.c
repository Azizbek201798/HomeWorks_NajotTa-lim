#include <stdio.h>
#include <string.h>

int main()
{
    char str1[100] = "Havo ifloslanmoqda ",str2[100] = "nega?";
    strcat(str1,str2);
    printf("Result : %s\n",str1);
}