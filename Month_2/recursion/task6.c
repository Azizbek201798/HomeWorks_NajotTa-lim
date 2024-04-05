// ***topshiriq6***
// Berilgan massiv elementlari orasidan eng kichik elemetni chiqaruvchi recursiv
// funksiyani hosil qiling!(Sikl operatorlari ishlatilmasin)!

// DONE!
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void findMin(int x[100],int len,int min){
    if (len == 0){
        printf("Min => %d\n",min);
    return ;
    }
    if (min > x[len-1]){
        min = x[len-1];
    }
    findMin(x,len-1,min);     
    }

int main()
{
    int number[100];
    int n; 
    srand(time(NULL));
    printf("n => ");
    scanf("%d",&n);
    int min = number[n - 1];
    for (int i = 0; i < n; i++)
    {
        number[i] = rand()%(99-10+1) + 10;
        printf("%4d",number[i]);
    }
    puts("");
    findMin(number,n,number[n-1]);
}
