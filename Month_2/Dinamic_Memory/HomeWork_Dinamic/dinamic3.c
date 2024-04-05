// 3-masala. Dinamic int seriya berilgan ushbu seriyadagi oxiridan k ta elementni o'chiruvchi dastur tuzing.
// Input: A={1,2,3,4,5} k=2
// Output: A={1,2,3}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


int getRandom(int min,int max)
{
    return rand()%(max - min + 1) + min;
}

void removeElements(int arr[], int a,int x)
{
    a = a - x;
    int *newArr = (int *) realloc(arr,a * sizeof(int));
        for(int i = 0; i < a; i++){
            printf("%d | ",newArr[i]);
    }
    puts("");
    free(newArr);
}

int main()
{
    system("clear");
    srand(time(NULL));
    int N,x;
    printf("Elementlar sonini kiriting : ");
    scanf("%d",&N);
    printf("O'chirilishi kerak Elementlar sonini kiriting : ");
    scanf("%d",&x);
    if (N < x){
        printf("Xatolik!\n");
        return 0;
    }
    int *arr;
    arr = (int *) calloc(N,(sizeof(int)));
    printf("Before arr ...\n");
    for (int i = 0; i < N; i++)
    {
        arr[i] = getRandom(10,99);
        printf("%d | ",arr[i]);
    }
    puts("");
    printf("Removed arr => \n");
    removeElements(arr,N,x);    
}
