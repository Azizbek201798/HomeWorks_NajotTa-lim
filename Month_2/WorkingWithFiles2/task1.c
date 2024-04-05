// 1-masala. Faylni ichida matn yozilgan. Ushbu matnda nechta lotin harfi ishtikor etganini toping.
// Input(Faylni ichida): "#include<iosteram>int main(){ return 0; }"
// Output: 28ta

#include <stdio.h>
#include <ctype.h>

int main()
{
    system("clear");
    FILE *p = fopen("task1.txt","w+");
    char str[1000];
    printf("Ma'lumot kiriting : ");
    fgets(str,1000,stdin);
    fprintf(p,"%s",str);
    rewind(p);
    char k;
    int count = 0;
    while(fscanf(p,"%c",&k) >= 0)
    {
        if (isalpha(k))
        {
            count++;
        }
    }

    printf("Task1.txt faylida => %d ta <= harf mavjud!\n",count);
    fclose(p);

    // DONE;
}