#include <stdio.h>
#include <math.h>

int kasr_qismi(float son){
    float box = son;
    int count = 0;

    while (box - (int)box != 0.0){
        box *=10;
        count++;
    }

    float num = son - (int)son;
    
    for (int i = 0; i < count; ++i) {
        num *= 10;
    }

    return  (int)round(num);
}

int main()
{
    system("clear");
    float num1,num2;
    int kasr1,kasr2;
    printf("Ikkita son kiriting : ");
    scanf("%f %f",&num1,&num2);
    kasr1 = kasr_qismi(num1);
    kasr2 = kasr_qismi(num2);
    if ((int)num1 + (int)num2 > kasr1 + kasr2)
    {
        printf("%d > %d",(int)num1 + (int)num2, kasr1 + kasr2);
    } else {
        printf("%d < %d",(int)num1 + (int)num2, kasr1 + kasr2);
    }
    puts("");
}

