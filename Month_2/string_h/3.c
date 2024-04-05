#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    printf("Enter a string: ");
    scanf("%s", str);

    int len = strlen(str);
    char spaced_str[2*len+1];  

    int j = 0;
    for (int i = 0; i < len; i++) {
        spaced_str[j++] = str[i];
        spaced_str[j++] = ' '; 
    }
    spaced_str[j] = '\0'; 

    printf("Result: %s\n", spaced_str);
    return 0;
}
