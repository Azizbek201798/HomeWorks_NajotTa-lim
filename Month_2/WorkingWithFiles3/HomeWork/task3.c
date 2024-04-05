// ***topshiriq_3***
//  Binar faylga nta elementdan iborat int seriyasini kiriting va ushbu fayldagi juftlarni chiqaring.
// Input (Binar faylning ichida): n=10 1 2 3 4 5 6 7 8 9 10
// Output: 2 4 6 8 10

#include <stdio.h>
// DONE!
int main()
{
    system("clear");
    int n;
    printf("Elementlar sonini kiriting : ");
    scanf("%d",&n);
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        printf("%d - element => ",i+1);
        scanf("%d",&arr[i]);
    };
    FILE *ptr = fopen("HomeWork/task3.dat","wb+");
    if (ptr == NULL)
    {
        printf("Error while reading file!\n");
        return 0;
    } 
    for (int i = 0; i < n; i++)
    {
        fwrite(&arr[i],4,1,ptr);
    }
    int x;
    rewind(ptr);
    for(;fread(&x,4,1,ptr);)
    {
        //printf("%d : ",x);
        if (x % 2 == 0)
            printf("%d ",x);
    }
    puts("");
    fclose(ptr);
}