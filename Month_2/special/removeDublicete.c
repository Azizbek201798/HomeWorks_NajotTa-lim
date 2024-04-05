#include <stdio.h>

int removeDublicate(int *arr,int num)
{
    for (int i = 0 ; i < 10; i++)
    {
        if (arr[i] == num)
            return 1;
    }
    return 0;
}

int main()
{
    system("clear");
    int arr[10], newArr[10], k = 0;
    for (int i = 0; i < 10; i++)
    {
        printf("%d - sonni kiriting : ",i+1);
        scanf("%d",&arr[i]);
    }
    for (int i = 0; i < 10; i++)
    {
        if (removeDublicate(newArr,arr[i]) == 0)
        {
            newArr[k] = arr[i];
            k++;
        }

    }
    for (int i = 0; i < k; i++)
    {
        printf("%d : ",newArr[i]);
    }

}