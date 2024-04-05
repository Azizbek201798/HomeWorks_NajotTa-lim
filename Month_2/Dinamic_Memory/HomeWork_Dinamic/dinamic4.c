// 4-masala. Familiya ism sharifingizni va tug'ilgan sananggizni alohida qatorda  yozing.
// Input(kiruvchi ma'lumot):
// Eshmirzayev Akobir Shodiyorovich 11.11.2021
// Output(Chiquvchi ma'lumot):
// Eshmirzayev
// Akobir
// Shodiyorovich
// 11.11.2021
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    system("clear");
    char info[100];
    printf("Ma'lumotlaringizni kiriting : ");
    fgets(info,100,stdin);
    char *ptr; 
    ptr = strtok(info," ");
    char *arr;
    arr = strcpy(arr,ptr); 
    while(ptr != NULL)
    {
        printf("%s\n",ptr);
        ptr = strtok(NULL," ");
    }

}