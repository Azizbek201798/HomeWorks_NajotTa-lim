// ***topshiriq4***
// Takrorlanish operatoridan foydalanmagan holda S satrdagi raqamlar sonini topuvchi 
// butun toifadagi Raqamlar_soni(S) rekursiv funksiyasini tuzing

// DONE;
#include <stdio.h>
#include <ctype.h>
#include <string.h>
void countDigit(char x[100],int len, int count)
{
    if (len == 0){
        printf("Raqamlar soni : %d\n",count);
        return ;
    }
    if (isdigit(x[len-1])){
        count += 1;
    }
    countDigit(x,len-1,count);
}
int main()
{
    char str[100];
    printf("Enter str : ");
    fgets(str,100,stdin);
    int len = strlen(str);
    countDigit(str,len,0);
}