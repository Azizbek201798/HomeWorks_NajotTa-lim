// ***topshiriq8***
// Faylda Berilgan satrdagi undosh harflar sonini unli harflar soniga nisbatini chiqaruvchi funksiya yarating?
// Input: Salom BolAlaR
// Output:  8 /  4

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
int main()
{
    system("clear");
    FILE *abs;
    abs = fopen("task8.txt","r");
    if (abs == NULL)
    {
        printf("Error while read file!\n");
        return 0;
    }
    char str[100];
    int count_unli = 0,count_undosh = 0,total = 0;
    fgets(str,100,abs);
    int i = 0;
    while(str[i] != '\0'){
        str[i] = tolower(str[i]);
        i++;
    }
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (isalpha(str[i]))
            total += 1;
    }
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == 'a' || str[i] == 'e' ||str[i] == 'u' ||str[i] == 'o' ||str[i] == 'i')
            count_unli += 1;
    }
    count_undosh = total - count_unli;
    printf("Unli harflar soni: %d\n",count_unli);
    printf("Undosh harflar soni: %d\n",count_undosh);
    printf("Unli harflar va undosh harflar nisbati: %d\n",count_undosh/count_unli);
    fclose(abs);
}