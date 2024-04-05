#include <stdio.h>
#include <string.h>
#include <math.h>

int main() {
    char binary_str[100];
    printf("Enter a positive integer in binary: ");
    scanf("%s", binary_str);

    int len = strlen(binary_str);
    int decimal_value = 0;

    for (int i = len - 1; i >= 0; i--) {
        int digit = binary_str[i] - '0';
        decimal_value += digit * pow(2, len - i - 1);
    }

    printf("Decimal value: %d\n", decimal_value);

    return 0;
}