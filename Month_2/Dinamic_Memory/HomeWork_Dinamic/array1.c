// n ta elementdan tashkil topgan massiv berilgan. Massiv oxirgi elementidan katta bo'lgan birinchi elementni chiqaruvchi dastur tuzing.
// Agar bunday element bo'lmasa, nol chiqarilsin.
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <time.h>
#include <stdbool.h>
int getRandom(int min,int max)
{
    return rand()%(max - min + 1) + min;
}

void findBigger(int *slice,int k)
{
    bool check = false;
    for (int i = 0; i < k - 1; i++)
    {
        if (slice[i] > slice[k - 1]){
            printf("First_Bigger : %d\n",slice[i]);
            check = true;
            break;
        }
    }
    if (check == false) 
        printf("Ohirgi qiymatdan katta qiymat mavjud emas!\n");
}

int main()
{
    system("clear");
    srand(time(NULL));
    int *arr , N;
    printf("N => ");
    scanf("%d",&N);
    arr = (int*) calloc(N , (sizeof(int)));
    for (int i = 0; i < N; i++)
    {
        arr[i] = getRandom(10,99);
        printf("%d | ",arr[i]);
    }
    puts("");
    findBigger(arr,N);
}