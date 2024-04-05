// ***Array7*** n ta elementdan tashkil topgan massiv berilgan. Massiv elementari Fibonachchi seriyasini (sonlarini)
//   tashkil qilsa 0 aks holda buzgan elementni chiqaradigan
// 	 programma tuzilsin.
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <stdbool.h>
void check(int *slice,int k)
{
    bool check = false;
    for (int i = 2; i < k; i++)
    {
        if (slice[i] != slice[i-1] + slice[i-2]){
            printf("Fibonachi seriasini buzgan Element => %d\n",slice[i]);
            check = true;
            break;
        } else{
            continue;
        }
    }
    if (check == false){
        printf("Massiv Fibonachi seriyasini tashkil qiladi!\n");
    }
}

int main()
{
    system("clear");
    int *arr,N;
    printf("Elementlar sonini kiriting :  => ");
    scanf("%d",&N);
    arr = (int*) calloc(N , (sizeof(int)));
    arr[0] = 1, arr[1] = 1;
    for (int i = 2; i < N; i++){
        printf("arr[%d] -> ",i);
        scanf("%d",&arr[i]);
    }
    puts("");
    check(arr,N);
}