#include <stdio.h>

int main()
{
    FILE *k = fopen("cola.txt","w");
    if (k == NULL)
    {
        printf("Error while opening file!\n");
        return 0;
    }
    fputs("Barselona cho'kmoqda to'grimi!",k);
    fclose(k);
    //printf("Ko'rish uchun 1 ni bsoing : ");
    //int op;
    //scanf("%d",&op);
    //op == 1 ? system("start cola.txt"): printf("Hazillashdim\n");
    return 0;
}