// ***topshiriq7***
// Berilgan satrdagi so'zlar sonini qaytaruvchi recursive funksiyani hosil qiling!

// DONE!;
#include <stdio.h>
#include <string.h>

int countWords(char str[], char* belgilar) {
    char* token = strtok(str, belgilar);

    if (token == NULL) {
        return 0;
    }

    return 1 + countWords(NULL, belgilar);
}

int main() {
    char str[100];

    printf("Enter str : ");
    fgets(str, sizeof(str), stdin);

    if (str[strlen(str) - 1] == '\n') {
        str[strlen(str) - 1] = '\0';
    }

    char belgilar[] = " ,./;:";
    int wordCount = countWords(str, belgilar);

    printf("So'zlar soni : %d\n", wordCount);

    return 0;
}