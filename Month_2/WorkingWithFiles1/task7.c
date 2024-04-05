// ***topshiriq7***
// Faylda Berilgan satrdagi unli harflar sonini chiqaruvchi funksiya yarating?
// Input: Uzbekistan kelajagi buyuk davlat
// Output: 12

#include <stdio.h>

int main()
{
    FILE *abs;
    abs = fopen("task7.txt","r");
    if (abs == NULL)
    {
        printf("Error while read file!\n");
        return 0;
    }
    char str[100];
    int count = 0;
    fgets(str,100,abs);
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == 'a' || str[i] == 'e' ||str[i] == 'u' ||str[i] == 'o' ||str[i] == 'i')
            count += 1;
    }
    printf("Unli harflar soni : %d\n",count);
    fclose(abs);
}