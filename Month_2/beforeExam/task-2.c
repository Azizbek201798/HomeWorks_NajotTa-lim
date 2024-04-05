// ***topshiriq2***
// Matn faylda berilgan satrdagi eng koâ€™p qatnashgan harfni 
// topuvchi dastur tuzing.
// >>> M: Mana  senga  olam  olam  gul! Havo yaxshi. 
// <<< Natija: 7 a

#include <string.h>
#include <stdio.h>

// DONE!

int check( char mas[] , char c  )
{
    int n = 0;
    for (int i = 0 ; i < strlen(mas) ; i++)
    {
        if( mas[i] == c)
            n++;
    }
    return n;
}
int main() {

    system("clear");

    FILE *file = fopen("task2.txt", "r");

    char word[1000],c;
    char last[1000];
    int max = 0 , lastmax = 0;
    while((fscanf(file, "%s", word)) != EOF){
            strcat(last,word);
    }
    puts("");
    for (int i = 0 ; i < strlen(last) ; i++)
    {
        max = check(last,last[i]);
        if( max > lastmax){
            lastmax = max;
            c = last[i];
            
        }
    }
    printf("%d ta => %c \n",lastmax,c);
    fclose(file);
}