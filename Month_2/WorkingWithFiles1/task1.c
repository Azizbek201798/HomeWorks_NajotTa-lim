// ***topshiriq1***
// Faylda Berilgan satrdagi eng uzun so'zni chiqaring?
// input: satr[]="Yaralangan qush hamon uchmoqda"
// output: Yaralangan
#include <stdio.h>
#include <string.h>

int main()
{
    system("clear");
    FILE *News;
    News = fopen("task1.txt","w");
    if (News == NULL)
    {
        printf("Error while reading file!\n");
        return 0;
    }
    char content[100], *longest_word = NULL;
    printf("Hohlasan satringizni kiriting : ");
    fgets(content,100,stdin);
    fputs(content,News);
    char *ptr = strtok(content," ");
    while (ptr != NULL)
    {
        if (longest_word == NULL || strlen(ptr) > strlen(longest_word))
        {
            longest_word = ptr;
        }  
        ptr = strtok(NULL," ");
    }
    printf("Eng uzun so'z => %s\n",longest_word);
    fclose(News);
}

