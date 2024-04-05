#include <stdio.h>
#include <string.h>

int main() {
    char char_str6[100];
    printf("Enter str: ");
    scanf("%s", char_str6);

    int len = strlen(char_str6);

    printf("Digits from left to right: ");
    for (int i = 0; i < len; i++) {
        printf("%c ", char_str6[i]);
    }
    printf("\n");

    return 0;
}