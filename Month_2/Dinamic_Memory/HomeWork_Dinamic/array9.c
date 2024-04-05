// ***Array9*** n ta elementdan tashkil topgan massiv berilgan. Massivda juft va toq elementar ketma - ket kelishini 
//  tekshiruchi programma tuzilsin. 
// 	Ketma - ketlik bajarilsa nol chiqarilsin. Aks holda ketma - ketikni buzgan birinchi element indeksi chigarilsin.
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <stdbool.h>
void check(int *slice,int k)
{
    bool check = false;
    for (int i = 1; i < k; i++)
    {
        if ((slice[i-1] % 2 == 0 && slice[i] % 2 == 0) || (slice[i-1] % 2 == 1 && slice[i] % 2 == 1)){
            printf("Ketma-ketlikni buzgan Element indeksi => %d\n",i);
            check = true;
            break;
        } else{
            continue;
        }
    }
    if (check == false){
        printf("Massiv elementlari juft va toq ketma-ketlikni tashkil qiladi!\n");
    }
}

int main()
{
    system("clear");
    int *arr,N;
    printf("Elementlar sonini kiriting :  => ");
    scanf("%d",&N);
    arr = (int*) calloc(N , (sizeof(int)));
    for (int i = 0; i < N; i++){
        printf("arr[%d] -> ",i);
        scanf("%d",&arr[i]);
    }
    puts("");
    check(arr,N);
}