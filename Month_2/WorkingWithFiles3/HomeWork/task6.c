// ***topshiriq_6***
//  Binar faylda berilgan sonlar ichidan lokal minimumlar sonini va shu elementlarni chop qiling:
// M:12 23 4 34 5 76 8 98
// Natija: 4 5 8 jami: 3 ta
// #topshiriq_binar_fayl

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
    int N;
    printf("Elementlar sonini kiriting : ");
    scanf("%d",&N);
    int arr[100];
    FILE *k = fopen("HomeWork/task6.Bin","wb+");
    if (k == NULL)
    {
        printf("Error while reading file!\n");
        return 0;
    }
    for (int i = 0; i < N; i++)
    {
        arr[i] = getRandom(10,99);
        printf("%d : ",arr[i]);
        fwrite(&arr[i],4,1,k);
    }
    int size = ftell(k);
    int count = size/4;
    rewind(k);
    int arrNew[100],z = 0;
    fread(arrNew,4,count,k);
    printf("\nLokal minimumlar : ");
    for (int i = 1; i < count - 1; i++)
    {
        if (arrNew[i] < arrNew[i-1] && arrNew[i] < arrNew[i+1])
        {
            printf("%d ",arrNew[i]);
            z++;
        }
    }
    puts("");
    printf("Soni : %d\n",z);
}