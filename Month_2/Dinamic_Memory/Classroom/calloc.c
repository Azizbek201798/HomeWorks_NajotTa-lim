#include <stdio.h>
#include <stdlib.h>

int tasodif(int a,int b)
{
    return rand() % (b - a + 1) + a;
}

int main()
{
    system("clear");
    srand(time(NULL));
    int n;
    printf("n = ");
    scanf("%d",&n);
    int *arr;
    arr = (int*) calloc (n,sizeof(int));
    for (int i = 0; i < n; i++)
    {
        arr[i] = tasodif(10,99);
        printf("%d | ", arr[i]);
    }
}
