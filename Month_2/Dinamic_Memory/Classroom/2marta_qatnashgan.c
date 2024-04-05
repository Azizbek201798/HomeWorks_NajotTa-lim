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
        scanf("%f",&arr[i]);
    }
    free(arr);
    }