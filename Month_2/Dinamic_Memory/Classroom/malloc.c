#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

int main()
{
    system("clear");
    int count;
    float *arr;
    printf("Count = ");
    scanf("%d",&count);
    arr = (float *) malloc(count * sizeof(float));
    for (int i = 0; i < count; i++)
    {
        arr[i] = (i + 2) * 1.0 / (i + 5);
        printf("%.2f | ",arr[i]);
    }
    puts("");
    free(arr);
    }