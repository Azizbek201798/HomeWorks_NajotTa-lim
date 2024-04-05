// ***topshiriq2
// Birinchi elementi 1 bo'lgan qolgan ixtiyoriy elementi o'zidan oldingi elementlar 
// kvadratlari yig'indisiga teng bo'lgan ketma-ketlikning n-hadi qiymati rekursiya 
// qism dastur orqali aniqlovchi dastur tuzing.

// DONE; 
#include <stdio.h>

int n_hadi(int n) {
    if (n == 1) {
        return 1;
    } else {
        int prevValue = n_hadi(n - 1);
        return prevValue * prevValue + prevValue;
    }
}

int main() {
    int n;

    printf("n => ");
    scanf("%d", &n);

    int nthValue = n_hadi(n);
    printf("n - hadi : %d\n", nthValue);

    return 0;
}