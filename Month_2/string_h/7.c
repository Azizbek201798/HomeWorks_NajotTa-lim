#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    printf("Enter a positive integer: ");
    scanf("%s", str);

    int len = strlen(str);

    printf("Digits from right to left: ");
    for (int i = len - 1; i >= 0; i--) {
        printf("%c ", str[i]);
    }
    printf("\n");

    return 0;
}