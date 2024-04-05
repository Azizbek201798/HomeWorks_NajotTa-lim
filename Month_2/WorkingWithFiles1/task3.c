// ***topshiriq3***
// Faylda berilgan satrni harf, raqam va probellardan boshqa belgilar soni nechtaligini aniqlang.
// Input: text[]="qwerty @#$%Hello world%^&"
// Output: 7ta

#include <stdio.h>
#include <ctype.h>

int main()
{
    system("clear");
    FILE *own;
    own = fopen("task3.txt","r");
    if (own == NULL)
    {
        printf("Error while reading file!\n");
        return 0;
    }
    char content[100];
    fgets(content,100,own);
    int count = 0;
    for (int i = 0; content[i] != '\0'; i++)
    {
        if (ispunct(content[i]))
            count++;
    }
    printf("Elementlar soni : %d\n",count);
    fclose(own); 
}