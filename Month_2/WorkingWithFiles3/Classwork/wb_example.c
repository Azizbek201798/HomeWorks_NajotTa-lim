#include <stdio.h>

int main()
{
    system("clear");
    FILE *ptr = fopen("Classwork/f1.bin","wb");
    if (ptr == NULL)
    {
        printf("Error while reading file!");
        return 0;
    }
    int count,a,b;
    printf("Nechta son kiritmoqchisiz?\n");
    scanf("%d",&count);
    for (int i = 1; i <= count; i++)
    {
        printf("%d - sonni kiriting : ",i);
        scanf("%d",&a);
        fwrite(&a,sizeof(int),1,ptr);
    }
    printf("Faylga sonlar yozildi!\n");
    fclose(ptr);
    FILE *file = fopen("Classwork/f1.bin","rb");
    while (fread(&b,4,1,file))
    {
        printf("%d | ",b);
    }
    fclose(file);
}

// DONE;

//   /go/src/NajotTalim/HomeWork/Month_2/WorkingWithFiles3