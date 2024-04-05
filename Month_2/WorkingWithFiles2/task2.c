// 2-masala. Faylni ichida matn yozilgan. Ushbu matnda nechta raqam ishtikor etganini toping.
// Input(Faylni ichida): "#include<iosteram>int main(){ return 0; }"
// Output: 1ta

#include <stdio.h>
#include <ctype.h>

int main()
{
    system("clear");
    FILE *fayl = fopen("task2.txt","w+");
    char str[1000];
    printf("Ma'lumot kiriting : ");
    fgets(str,1000,stdin);
    fprintf(fayl,"%s",str);
    int count = 0;
    rewind(fayl);
    char n;
    while(fscanf(fayl,"%c",&n) >= 0)
    {
        if (isdigit(n)){
            count++;
        }
    }
    printf("Task2.txt fayldagi raqamlar soni >= %d ta!\n",count);
    fclose(fayl);

    // DONE;
}