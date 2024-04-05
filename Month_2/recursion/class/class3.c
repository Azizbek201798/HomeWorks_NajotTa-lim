#include <stdio.h>
#include <stdbool.h>

bool isPerfect(int n)
{
    int sum = 0;
    for (int i = 1; i < n; i++){
        if (n % i == 0)
            sum += i;
    }
    return sum == n;
}

int main()
{
    int n;
    printf("Input n => ");
    scanf("%d",&n);
    isPerfect(n) ? printf("%d - Mukammal Son\n",n) : printf("%d - Mukammal EMAS!\n",n);
}