#include <stdio.h>
#include <string.h>

void decimalToBinary(int decimal_value, char* binary_str) {
    if (decimal_value == 0) {
        strcpy(binary_str, "0");
        return;
    }

    int index = 0;
    while (decimal_value > 0) {
        int remainder = decimal_value % 2;
        binary_str[index++] = remainder + '0';
        decimal_value /= 2;
    }

    int len = index;
    for (int i = 0; i < len / 2; i++) {
        char temp = binary_str[i];
        binary_str[i] = binary_str[len - i - 1];
        binary_str[len - i - 1] = temp;
    }

    binary_str[index] = '\0';
}

int main() {
    char binary_str[100];
    int decimal_value;

    printf("Enter a positive integer in decimal: ");
    scanf("%d", &decimal_value);

    decimalToBinary(decimal_value, binary_str);

    printf("Binary value: %s\n", binary_str);

    return 0;
}