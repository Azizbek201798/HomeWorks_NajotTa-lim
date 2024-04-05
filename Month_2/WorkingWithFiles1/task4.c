// ***topshiriq4***
// Fayldagi char seriyasida lotin harflar(26ta) alfavitdagi barcha kichik harflar berilgan va tushirilib qoldirilgan harflarni toping.
// Input: text[]="qzwsxedcvfrtgbnyujmkiolp"
// Output: h harfi qolib ketgan

#include <stdio.h>
#include <ctype.h>
int main()
{
    system("clear");
    FILE *mine;
    mine = fopen("task4.txt","r");
    if (mine == NULL)
    {
        printf("Error while reading file!\n");
        return 0;
    }     
    char content[100];
    fgets(content,100,mine);
    int num[26];
    for (int i = 0; content[i] != '\0'; i++)
    {
        if (islower(content[i]))
        {
            num[content[i] - 'a'] = 1;
        }
    }
    for (int i = 0; i < 26; i++)
    {
        if (num[i] == 0)
            printf("%c | ",i + 97);        
    }
    puts("");
    fclose(mine);
}