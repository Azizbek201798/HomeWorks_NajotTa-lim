// ***Array4*** N ta elementan tashkil topgan massiv va K, L butun sonlari berilgan. (0 <= K <= L < N).
// 	Massivning K va L indekslari orasidagi elementlarining o'rta arifmetigini chigaruchi programma
// 	tuzilsin.
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <time.h>
#include <stdbool.h>
int getRandom(int min,int max)
{
    return rand()%(max - min + 1) + min;
}

void avgSum(int *slice,int k,int a,int b)
{
    bool check = false;
    int sum = 0,count = 0;
    for (int i = a; i <= b; i++)
    {
        sum += slice[i];
        count++; 
    }
    sum /= count;
    printf("K va L  indekslar orasidagi qiymatlar yig'indisi = %d\n",sum);
}

int main()
{
    system("clear");
    srand(time(NULL));
    int *arr , K,L,N;
    printf("Elementlar sonini kiriting :  => ");
    scanf("%d",&N);
    printf("K and L( 0 <= K < L < N ) => ");
    scanf("%d%d",&K,&L);
    if (K < 0 || L > N || L < K){
        printf("XATOLIK K va L ni berilgan oraliqda kiriting!\n");
        return ;
    }

    arr = (int*) calloc(N , (sizeof(int)));
    for (int i = 0; i < N; i++)
    {
        arr[i] = getRandom(1,5);
        printf("%d | ",arr[i]);
    }
    puts("");
    avgSum(arr,N,K,L);
}