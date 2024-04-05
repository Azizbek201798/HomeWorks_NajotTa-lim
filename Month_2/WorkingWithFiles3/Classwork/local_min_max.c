#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float getRandom(int a, int b)
{
    int x = rand()%(b - a + 1) + a;
    return x * 0.421;
}

int main()
{
    system("clear");
    srand(time(NULL));
    FILE *ptr = fopen("Classwork/f2.Bin","wb+");
    if (ptr == NULL)
    {
        printf("Error while reading file!;\n");
        return 0;
    }
    int k;
    float a,b;
    int const count1 = 15;
    k = count1;
    while (k)
    {
        a = getRandom(10,30);
        printf("%.3f\n",a);
        fwrite(&a,sizeof(float),1,ptr);
        k--;
    }
    printf("Faylga ma'lumotlar yozildi!\n");
    int size = ftell(ptr);
    int count = size/4;
    rewind(ptr);
    float arr[100];
    fread(arr,4,count,ptr);
    //printf("%f\n",arr[2]);
    fclose(ptr);
    FILE *lc_min = fopen("Classwork/Lokal_Min.txt","w");
    FILE *lc_max = fopen("Classwork/Lokal_Max.txt","w");
    for (int i = 1; i < count - 1; i++)
    {
        //printf("%f | ",arr[i]);
        if (arr[i] > arr[i-1] && arr[i] > arr[i+1])
        {
            fprintf(lc_max,"%.2f : ",arr[i]);
        } 
        else if (arr[i] < arr[i-1] && arr[i] < arr[i+1])
        {
            fprintf(lc_min,"%.2f : ",arr[i]);
        }
    }
    fclose(lc_min);
    fclose(lc_max);
    //system("start Lokal_Min.txt");
    //system("start Lokal_Max.txt");
}
