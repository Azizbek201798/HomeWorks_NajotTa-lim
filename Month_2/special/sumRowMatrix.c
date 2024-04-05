#include <stdio.h>

int main()
{
    int arr[5][5];
    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++)
        {
            printf("[%d,%d] => ",i,j);
            scanf("%4d",&arr[i][j]);
        }
        puts("");
    }
    int sum = 0, sumNew = 0, index = 0;
    for (int i = 0; i < 5; i++)
    {
        sum = 0;
        for (int j = 0; j < 5; j++)
        {
            sum += arr[i][j];
        }
        if (sumNew < sum)
        {   
            sumNew = sum;
            index = i;
        }
    }
    // Show line;
    printf("Elementlari yig'indisi eng katta qator : ");
    for (int i = 0; i < 5; i++)
    {
        printf("%d : ",arr[index][i]);
    }
    puts("");
}