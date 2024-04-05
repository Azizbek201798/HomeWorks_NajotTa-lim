#include <stdio.h>
#include <stdlib.h>

int is_prime(int num) 
{    
    for (int i = 2; i * i <= num; i++) 
    {
        if (num % i == 0) 
        {
            return 0; 
        }
    }
    return 1; 
};

void PrimeNumbers(int num, int *primes) 
{
    int count = 0;
    for (int i = 2; i <= num; i++) 
    {
        if (is_prime(i)) 
        {
            primes[count++] = i;
        }
    }
}

int main() 
{
    system("clear");
    int n;
    printf("N = ");
    scanf("%d", &n);
    int *primes = (int *)calloc((n + 1), sizeof(int));
    if (primes == NULL) 
    {
        puts("Xotira ajratishda xatolik\n");
        return 0;
    }

    PrimeNumbers(n, primes);

    printf("%d gacha bo'lgan tub sonlar: ", n);
    for (int i = 0; i <= n; i++) 
    {
        if (primes[i] != 0)       
        {
            printf("%d ", primes[i]);
            fflush(stdout);
        }
    }

    free(primes);
    return 0;
}
