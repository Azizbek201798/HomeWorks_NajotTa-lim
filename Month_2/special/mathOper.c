#include <stdio.h>
#include <ctype.h>
int main(){
    system("clear");
    char word[10];

    fgets(word, 10, stdin);

    char amal;
    int a,b;
    int vaqtincha = 1;

    for (int i = 0; word[i]; ++i) {
        if (isdigit(word[i]) && vaqtincha == 1){
            a  = word[i] - 48;
            vaqtincha = 0;
        } else if (isdigit(word[i])){
            b  = word[i] - 48;
        } else if (ispunct(word[i])){
            amal = word[i] ;
        }
    }

    switch (amal) {
        case '/':
            printf("%d / %d = %d", a , b, a / b);
            break;
        case '*':
            printf("%d * %d = %d", a , b, a * b);
            break;
        case '-':
            printf("%d - %d = %d", a , b, a - b);
            break;
        case '+':
            printf("%d + %d = %d", a , b, a + b);
            break;
    }
