#include <stdio.h>

int main()
{
    system("clear");
    int N;
    printf("N => ");
    scanf("%d",&N);
    int right = N - 1, left = 0, top = 0, bottom = N - 1, k = 1;
    int arr[100][100];
    while (right >= left || bottom >= top)
    {
        for (int i = top; i <= bottom; i++)
        {
            for (int j = left; j <= right; j++)
            {
                arr[i][j] = k;
                k++;
            }
            break;
        }
        top += 1;

        for (int j = right; j >= left; j--)
        {
            for (int i = top; i <= bottom ; i++ )
            {
                arr[i][j] = k;
                k++;
            }
            break;
        }
        right -= 1;

        for (int i = bottom; i >= top; i--)
        {
            for (int j = right; j >= left ; j-- )
            {
                arr[i][j] = k;
                k++;
            }
            break;
        }
        bottom -= 1;
               
        for (int j = left; j <= right; j++)
        {
            for (int i = bottom; i >= top ; i-- )
            {
                arr[i][j] = k;
                k++;
            }
            break;
        }
        left += 1;
    }
    // ************************************************
    for (int i = 0; i < N; i ++) 
    {
        for (int j = 0; j < N; j++)
        {
            printf("%4d",arr[i][j]);
        }
        puts("\n");
    }
}