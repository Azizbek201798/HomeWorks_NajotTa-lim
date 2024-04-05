#include <stdio.h>
#include <stdlib.h>

float getRandom(int a, int b)
{
    int x = rand()%(b - a + 1) + a;
    return x * 0.421;
}

int main()
{
    system("clear");
    FILE *ptr = fopen("Classwork/f2.Bin","wb+");
    if (ptr == NULL)
    {
        printf("Error while reading file!;\n");
        return 0;
    }
    int k;
    float a,b;
    int const count = 15;
    k = count;
    while (k)
    {
        a = getRandom(10,20);
        fwrite(&a,sizeof(float),1,ptr);
        k--;
    }
    printf("Faylga ma'lumotlar yozildi!\n");
    rewind(ptr); 
    //fseek(ptr,0,SEEK_END);
    for (;fread(&b,4,1,ptr);)
    {
        printf("%.2f | ",b);
    }
    puts("");
    fclose(ptr);
}
