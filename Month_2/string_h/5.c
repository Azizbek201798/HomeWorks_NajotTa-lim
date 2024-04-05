#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

bool isInteger(char *str) {
    if (str == NULL || *str == '\0' || isspace(*str)) {
        return false;
    }

    char* endptr;
    strtol(str, &endptr, 10);

    return (*endptr == '\0');
}

bool isFloat(char* str) {
    if (str == NULL || *str == '\0' || isspace(*str)) {
        return false;
    }

    char* endptr;
    strtof(str, &endptr);

    return (*endptr == '\0');
}

int main() {
    char char_str5[100];
    printf("Enter a string: ");
    scanf("%s", char_str5);

    int len = strlen(char_str5);

    if (isInteger(char_str5)) {
        printf("Output: 1\n");
    } else if (isFloat(char_str5)) {
        printf("Output: 2\n");
    } else {
        printf("Output: 0\n");
    }

    return 0;
}