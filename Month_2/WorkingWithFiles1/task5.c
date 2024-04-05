// ***topshiriq5***
// Faylda Berilgan satrdagi katta harflar sonini chiqaruvchi funksiya yarating?
// Input: Salom boLaliK
// Output: 3

#include <stdio.h>
#include <ctype.h>

int main()
{
    FILE *k;
    k = fopen("task5.txt","r");
    if (k == NULL)
    {
        printf("Error while reading file!\n");
        return 0;
    }
    char str[100];
    fgets(str,100,k);
    int count = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (isupper(str[i]))
            count++;
    }
    printf("Katta harflar soni : %d\n",count);
    fclose(k);
}