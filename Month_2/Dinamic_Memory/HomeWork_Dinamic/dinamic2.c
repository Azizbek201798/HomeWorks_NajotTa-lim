#include <stdio.h>
#include <stdlib.h> // Ikkita kutubxonadan birini ishlatsa ham yetarli;
#include <malloc.h> // Ikkita kutubxonadan birini ishlatsa ham yetarli;
#include <time.h>
#include <limits.h>
// 2-masala. Dinamic int seriya berilgan ushbu seriyadagi 2 - minimal elementni o'chiruvchi dastur tuzing.
// Input: A={1,2,3,4,5}
// Output: A={1,3,4,5}

int getRandom(int a,int b)
{
    return rand()%(b - a + 1) + a;
}

void removeSecondMax(int arr[], int a)
{
    int beforeMin = INT_MAX,min = INT_MAX, k;
    for (int i = 1; i < a; i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
        }
    }
    int min2_Index = 0;
    for (int i = 1; i < a; i++)
    {
        if (arr[i] < beforeMin && arr[i] > min)
        {
            beforeMin = arr[i];
            min2_Index = i;
        }
    }
    for (int i = min2_Index; i < a; i++)
    {
        arr[i] = arr[i + 1];
    }
    int *newArr = (int *) realloc(arr,(a - 1) * sizeof(int));
        for(int i = 0; i < a-1; i++){
        printf("%d | ",arr[i]);
    }
    puts("");
}

int main()
{
    system("clear");
    srand(time(NULL));
    int N;
    printf("Elementlar sonini kiriting : ");
    scanf("%d",&N);
    int *arr,k;
    arr = (int *) calloc(N,(sizeof(int)));
    printf("Before arr ...\n");
    for (int i = 0; i < N; i++)
    {
        arr[i] = getRandom(10,99);
        printf("%d | ",arr[i]);
    }
    puts("");
    printf("Removed arr => \n");
    removeSecondMax(arr,N);
    

}
