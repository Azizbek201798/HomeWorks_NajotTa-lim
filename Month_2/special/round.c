#include <stdio.h>

int main()
{
    float num;
    int res;
    printf("Butun son kiriting : ");
    scanf("%f",&num);
    float kasrQismi = num - (int)num;
    if (kasrQismi >= 0.5)
    {
        res = (int)num + 1; 
    } else {
        res = (int)num;
    }
    printf("%d\n",res);
}