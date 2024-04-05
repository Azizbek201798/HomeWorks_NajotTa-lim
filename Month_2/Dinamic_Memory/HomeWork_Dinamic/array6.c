// ***Array6*** n ta elementdan tashkil topgan massiv berilgan. Massiv elementari arifmetik progressiyani tashkil qilsa 
// 0 aks holda buzgan elementni chiqaradigan
// programma tuzilsin.
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <stdbool.h>
void check(int *slice,int k)
{
    bool check = false;
    int count = 0,d = slice[1] - slice[0];
    for (int i = 1; i < k; i++)
    {
        if (slice[i] - slice[i-1] != d){
            printf("Arifmetik progressiyani buzgan Element => %d\n",slice[i]);
            check = true;
            break;
        } else{
            continue;
        }
    }
    if (check == false){
        printf("Massiv arifmetik progressiyani tashkil qiladi!\n");
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