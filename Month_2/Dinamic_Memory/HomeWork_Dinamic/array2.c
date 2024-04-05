// ***Array2*** n ta elementdan tashkil topgan massiv berilgan. Massiv dastlabki elementidan katta va oxirgi elementidan kichik  
//  oxirgi element indeksini chiqaruvchi programma tuzilsin. 
// 	Agar bunday element bo'lmasa, nol chiqarilsin. (a[0] < a[k] < a[n-1])
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
    for (int i = k - 2; i >= 1; i--)
    {
        if (slice[i] > slice[0] && slice[i] <= slice[k-1]){
            printf("Index_Of_Number : %d\n",i);
            check = true;
            break;
        }
    }
    if (check == false) 
        printf("%d\n",0);
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
