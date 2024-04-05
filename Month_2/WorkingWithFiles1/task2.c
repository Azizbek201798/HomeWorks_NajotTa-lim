// ***topshiriq2***
// Faylda char seriyasi berilgan va ushbu char seriyasidagi so'zlarni chiqaruvchi dastur tuzing.
// Input: matn[]="This is a book. It is very intresting!"
// Output:
// This
// is
// a
// book
// It
// is
// very
// intresting

#include <stdio.h>
#include <string.h>

int main()
{
    FILE *my;
    my = fopen("task2.txt","r");
    if (my == NULL)
    {
        printf("Error while reading file!\n");
        return 0;
    }
    char content[100];
    fgets(content,100,my);
    char * ptr = strtok(content," ");
    while (ptr != NULL)
    {
        printf("%s\n",ptr);
        ptr = strtok(NULL," ");
    }
    fclose(my);
}