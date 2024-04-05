// ***topshiriq3***
// a haqiqiy soni va n butun sonlari berilgan.(n>=0) Shu a sonini n-darajaga oshiruvchi  
// rekursiyali qism dastur yarating

// DONE;
#include <stdio.h>

double degree(double a, int n)
{
    if (n == 0)
        return 1;
    return a * degree(a,(double)(n-1));
}

int main()
{
    double a;
    int n; // n >= 0;
    printf("n va a => ");
    scanf("%lf%d",&a,&n);
    printf("Result : %.2lf\n",degree(a,n));
}