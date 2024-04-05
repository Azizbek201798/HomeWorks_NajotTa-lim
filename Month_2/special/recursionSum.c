#include <stdio.h>

int sumRecursion(int n)
{
    if (n == 1)
    {
        return 1; 
    } else {
        return n + sumRecursion(n-1);
    }
};

int main()
{
    int n;
    printf("n => ");
    scanf("%d",&n);
    int sum = sumRecursion(n);
    printf("1 dan n gacha sonlar yig'indisi : %d\n",sum);
};