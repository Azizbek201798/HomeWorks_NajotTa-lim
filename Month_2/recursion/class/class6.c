#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <limits.h>

int Max = INT_MIN;

int find_Max(int x[100], int n, int a)
{
    if (a == n)
        return Max;
    if (x[a] > Max)
        Max = x[a];
    return find_Max(x,n,a++);
}

int main()
{
    srand(time(NULL));
    int n , numbers[100];
    printf("Input n => ");
    scanf("%d",&n);
    for (int i = 0; i < n; i++){
        numbers[i] = rand()%(99-10+1) + 10;
        printf("%4d",numbers[i]);
    }
    printf("Max => %4d\n",find_Max(numbers,n,0));
}