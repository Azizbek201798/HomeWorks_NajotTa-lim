// ***topshiriq5***
// Berilgan sonni ikkilik sanoq sistemasi ko'rinishida chop qiladigan rekursiv 
// funksiyani hosil qiling.

// DONE;
#include <stdio.h>

int converter(int x)
{
    int res;
    if (x == 0)
        return 0;
    return (x % 2) + 10 * converter(x / 2);
}

int main()
{
    int number;
    printf("Number => ");
    scanf("%d",&number);
    printf("Ikkilik sonoq sistemasi da %d => %d ga teng!\n",number,converter(number));
}
