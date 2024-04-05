// ***topshiriq_1***
//  Binar faylga char seriyasini kiriting va ushbu fayldagi 2-so'zni 2marta chiqaring.
// Input (Binar faylning ichida): Salom Ishyoqmas Bekorchi grajdanlar
// Output: 
// Ishyoqmas
// Ishyoqmas

#include <stdio.h>
#include <string.h>
#include <ctype.h>
// DONE;
int main()
{
    system("clear");
    FILE *k = fopen("HomeWork/task1.Bin","wb+");
    if (k == NULL)
    {
        printf("Error while reading file!\n");
        return 0;
    }
    char str[100];
    printf("Ma'lumot kiriting : ");
    fgets(str,100,stdin);
    str[strlen(str) - 1] = '\0';
    fwrite(str,1,100,k);
    char x[strlen(str)];
    rewind(k);
    fread(&x,1,strlen(str),k);
    char *y = strtok(str," ");
    y = strtok(NULL," ");
    if (y != NULL)
    {
        printf("%s\n%s\n",y,y);
    } else {
        printf("Second word does't have!\n");
    }
    fclose(k);
}