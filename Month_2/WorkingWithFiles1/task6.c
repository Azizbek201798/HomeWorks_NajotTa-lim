// ***topshiriq6***
// Faylda Berilgan satrdagi kichik harflar sonini chiqaruvchi funksiya yarating?
// Input: Salom boLaliK
// Output: 9

#include <stdio.h>
#include <ctype.h>

int main()
{
    FILE *abs;
    abs = fopen("task6.txt","r");
    if (abs == NULL)
    {
        printf("Error while reading files!\n");
        return 0;
    }
    char str[100];
    int count = 0;
    fgets(str,100,abs);
    for (int i = 0; str[i] != '\0'; i++){
        if (islower(str[i])){
            count ++;
        }
    }
    printf("%d\n",count);

}