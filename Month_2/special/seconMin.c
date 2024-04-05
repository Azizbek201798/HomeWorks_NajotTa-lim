#include <stdio.h>
#include <limits.h>

int findMin(int *arr, int N)
{
    int min = arr[0]; 
    for (int i = 0; i < N; i++)
    {
        if (arr[i] < min)
            min = arr[i];
    }
    return min;
}

int main()
{
    int N;
    printf("Elementlar soni : ");
    scanf("%d",&N);
    int arr[N];
    for (int i = 0; i < N; i++)
    {
        printf("%d - qiymat => ",i+1);
        scanf("%d",&arr[i]);
    }
    int min = findMin(arr,N), secondMin = INT_MAX;
    for (int i = 0; i < N; i++)
    {
        if (arr[i] < secondMin && min != arr[i])
        {
            secondMin = arr[i];
        }
    }     
    printf("\nSecond Min => %d\n",secondMin);
}