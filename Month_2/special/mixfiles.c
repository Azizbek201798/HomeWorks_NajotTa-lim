#include <stdio.h>

int main()
{
    system("clear");
    FILE *file1 = fopen("special/first1.txt","r");
    FILE *file2 = fopen("special/first2.txt","r");
    FILE *file3 = fopen("special/first3.txt","w");
    char str1[100];
    char str2[100];
    while (fgets(str1,100,file1))
    {
        fprintf(file3,"%s",str1);
    }
    while (fgets(str2,100,file2))
    {
        fprintf(file3,"%s",str2);
    }
    fclose(file1);
    fclose(file2);
    fclose(file3);
}