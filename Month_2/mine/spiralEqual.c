#include <stdio.h>

int main()
{
    int N,k;
    printf("N => ");
    scanf("%d",&N);
    int left = 0, right = 2*N - 2, top = 0, bottom = 2*N - 2;
    k = N;
    int arr[100][100];
    while (left <= right || top <= bottom)
    {
        for (int i = top; i <= bottom; i++)
        {
            for (int j = left; j <= right; j++)
            {
                arr[i][j] = k;
            }
        }
        top += 1;

         for (int j = right; j >= left; j--)
         {
             for (int i = top; i <= bottom; i++)
             {
                 arr[i][j] = k;
             }
         }
        right -= 1;

        for (int i = bottom; i >= top; i--)
         {
             for (int j = right; j >= left; j--)
             {
                 arr[i][j] = k;
             }
         }
        bottom -= 1;

        for (int j = left; j <= right; j++)
         {
             for (int i = bottom; i >= top; i--)
             {
                 arr[i][j] = k;
             }
         }
        left += 1;
        k--;
    }

    // For Display;
    for (int i = 0; i <= 2*N - 2; i++)
    {
        for (int j = 0; j <= 2*N - 2; j++)
        {
            printf("%3d",arr[i][j]);
        }
        puts("");
    }

}