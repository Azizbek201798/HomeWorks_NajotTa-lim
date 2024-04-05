// ***topshiririq9***;
// Berilgan uzunlikdagi passwordni (faqat katta va kichik lotin harflari, hamda raqamlardan tashkil topgan ) 
// tasodifiy hosil qiladigan protsedura yarating;
// Masalan: random__password(12); Natija: C3S2ry13QcdS;  
// #topshiriq_char_seriya;

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    system("clear");
    srand(time(NULL));
    FILE *password;
    password = fopen("task9.txt","w");
    int N, z, index = 0;
    char my[N];
    printf("Password uzunligini kiriting : ");
    scanf("%d",&N);
    while (N > 0){
        z = rand()%(122 - 48 + 1) + 48;
        if ((z >= 48 && z <= 57) || (z >= 97 && z <= 122) || (z >= 65 && z <= 90))
        {
            my[index++] = z;
            N--;
        }
    }
    printf("%s\n",my);
    fputs(my,password);
    fclose(password);
}
