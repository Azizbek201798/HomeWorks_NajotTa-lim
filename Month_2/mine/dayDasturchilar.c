#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
    system("clear");
    char date[8];
    printf("Sanani kiriting : ");
    scanf("%s",date);
    int dayParty = 255;
    char day[2], month[2], year[4];
    strcpy(day,date[0,1]);
    printf("%d",atoi(day));
}