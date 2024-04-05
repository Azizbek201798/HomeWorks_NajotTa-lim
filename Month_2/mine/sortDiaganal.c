#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void sort(int *arr, int N)
{
    int temp;
    for (int i = 0; i < N; i++)
    {
        for (int j = 1; j < N; j++)
        {
            if (arr[j-1] > arr[j])
            temp = arr[j-1];
            arr[j-1] = arr[j];
            arr[j] = temp;
        }
    }
}

int main()
{
    system("clear");
    srand(time(NULL));
    int N = 5;
    int arr[N][N];
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            arr[i][j] = rand()%(99 - 10) + 10;
            printf("%4d",arr[i][j]);
        }
        puts("\n");
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (i == j)
            {
                sort(arr[i][j],N);
            }
        }
    }

}