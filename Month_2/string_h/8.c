#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    printf("Enter a positive integer: ");
    scanf("%s", str);

    int len = strlen(str);
    int sum = 0;

    for (int i = 0; i < len; i++) {
        int digit = str[i] - '0';
        sum += digit;
    }

    printf("Sum of digits: %d\n", sum);

    return 0;
}