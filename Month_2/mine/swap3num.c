#include <stdio.h>

void swap(float *x,float *y, float *z)
{
    float temp = *z;
    *z = *y;
    *y = *x;
    *x = temp; 
}

int main()
{
    system("clear");
    float a = 10,b = 20,c = 30;
    printf("Before\na = %.2f; b = %.2f; c = %.2f\n",a,b,c);
    swap(&a,&b,&c);
    printf("After\na = %.2f; b = %.2f; c = %.2f\n",a,b,c);
}