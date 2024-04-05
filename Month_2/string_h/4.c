#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    printf("Enter a string: ");
    scanf("%s", str);

    int N;
    printf("Enter the number of asterisks: ");
    scanf("%d", &N);

    int len = strlen(str);
    char newStr[2*len + N*len + 1]; 

    int j = 0;
    for (int i = 0; i < len; i++) {
        newStr[j++] = str[i];
        for (int k = 0; k < N; k++) {
            newStr[j++] = '*';  
        }
    }
    newStr[j] = '\0';  

    printf("Result: %s\n", newStr);
    return 0;
}