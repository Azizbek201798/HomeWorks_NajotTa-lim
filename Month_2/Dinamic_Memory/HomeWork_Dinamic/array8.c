// ***Array8*** n ta elementdan tashkil topgan massiv berilgan. Massiv elementari geometrik progressiyani tashkil gilsa, 
//  maxrajni aks holda nolni chigaruvchi programma tuzilsin.
// 	Izoh: maxraj = (3 12 48  192) massiv uchun 12 / 3 = 4 
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <stdbool.h>
void check(int *slice,int k)
{
    bool check = false;
    int q = slice[1] / slice[0];
    for (int i = 1; i < k; i++)
    {
        if (slice[i] / slice[i-1] != q){
            printf("Geometrik progressiyani buzgan Element => %d\n",slice[i]);
            check = true;
            break;
        } else{
            continue;
        }
    }
    if (check == false){
        printf("Massiv geometrik progressiyani tashkil qiladi maxraji => %d!\n",q);
    }
}

int main()
{
    system("clear");
    int *arr,N;
    printf("Elementlar sonini kiriting :  => ");
    scanf("%d",&N);
    int i = 0;
    arr = (int*) calloc(N , (sizeof(int)));
    for (int i = 0; i < N; i++){
        printf("arr[%d] -> ",i);
        scanf("%d",&arr[i]);
    }
    puts("");
    check(arr,N);
}