// ***Topshiriq1
// Birinchi elementi 1 bo'lgan qolgan ixtiyoriy elementi o'zidan oldingi elementlar 
// yig'indisiga teng bo'lgan ketma-ketlikning n-hadi qiymati rekursiya qism dastur 
// orqali aniqlovchi dastur tuzing.

// DONE;
#include <stdio.h>

int ketma_ketlik(int k)
{
    if (k == 1)
        return 1; 
    return 2 * ketma_ketlik(k-1);
}

int main()
{
    int n;
    printf("n = ");
    scanf("%d",&n);
    printf("Ketma-ketlikni n - hadi => %d\n",ketma_ketlik(n));
}