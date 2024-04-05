#include <stdio.h>

int Summa(int n)
{
    int sum = 0;
    if (n == 0)
        return 0;
    return n % 10 + Summa(n/10);
}

int main()
{
    int number;
    printf("Input number : ");
    scanf("%d",&number);
    printf("Summa = %d\n",Summa(number));
}