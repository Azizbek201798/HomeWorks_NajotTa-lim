#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int getRandom(int a,int b)
{
    return rand()%(b-a+1) + a;
}

int main()
{
    system("clear");
    srand(time(NULL));
    int count = 0;
    printf("Nechta son kiritmoqchisiz : ");
    scanf("%d",&count);
    int x,r = 1;
    freopen("sonlar.txt","w+",stdout);
    for (int i = 0; i < count; i++)
    {

            x = getRandom(10,99);
            printf("%d | ",x);
    }
    //fclose();
    FILE *k = fopen("tub.txt","w");

        for (int j = 2; j < x; j++ ){
            if (x % j == 0){
                r = 0;
                break;
            } 
        }
        if (r = 1){
            fprintf(k,"%d\n",x);
        } 
    fclose(k);
    FILE *ki = fopen("murakkab.txt","w");

        for (int j = 2; j < x; j++ ){
            if (x % j == 0){
                r = 0;
                fprintf(ki,"%d\n",x);
            } 
        }
         
    fclose(k);
}