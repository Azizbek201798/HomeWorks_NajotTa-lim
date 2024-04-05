#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int irand(int a,int b){

        return rand()%(b-a+1)+a;

}
void Sort_ASC(int arr[],int count){

            for (int i = 0; i < count; ++i) {

                for (int j = 0; j < count - i; ++j) {

                if (arr[j] >arr[j + 1] ){

                int box = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = box;
            }
        }
    }
}
void Sort_DESC(int arr[],int count){

            for (int i = 0; i < count; ++i) {

                for (int j = 0; j < count -i; ++j) {

                if (arr[j] < arr[j + 1] ){

                int box = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = box;
            }
        }
    }
}

int main ()
{
    system("clear");
    FILE *file = fopen ("HomeWork/problem5.dat","wb+");
    while(file == NULL)
    {
        puts("xatolik yuz berdi!");
        return 0;
    }
    int n,num;
    printf("nechta sondan iborat bolsin? ");
    scanf("%d",&n);
    for(int i = 0 ; i < n ; i++)
    {
        num = irand(-50,50);
        printf("%d |",num);
        fwrite(&num,sizeof(int),1,file);
    }
    int son = ftell(file);
    int size = son/4;
    rewind(file);
    int mas[size];
    fread(mas,sizeof(int),size,file);
    fclose(file);
    puts("");
    int toqq[100],juftt[100],manfiyy[100],musbatt[100];
    int k = 0 , l = 0, j = 0 , h = 0;
    FILE *toq = fopen("HomeWork/toq_num.txt","w");
    FILE *juft = fopen("HomeWork/juft_num.txt","w");
    FILE *manfiy = fopen("HomeWork/manfiy_num.txt","w");
    FILE *musbat = fopen("HomeWork/musbat_num.txt","w");
    for(int i = 1 ; i <= size ; i ++)
    {
        if(mas[i] % 2 == 0){
            juftt[k] = mas[i];
            k++;
        }
        if(mas[i] % 2 == 1){
            toqq[l] = mas[i];
            l++;
        }
        if(mas[i] > 0){
            musbatt[j] = mas[i];
            j++;
        }
        if(mas[i] < 0){
            manfiyy[h] = mas[i];
            h++;
        }
    }

    Sort_ASC(juftt,k);
    printf("Juft sonlar : ");
    for(int i = 0 ; i < k ; i ++)
    {
        fprintf(juft,"%d |",juftt[i]);
        printf("%d |",juftt[i]);
    }
    puts("");

    Sort_DESC(toqq,l);
    printf("Toq sonlar : ");
    for(int i = 0 ; i < l ; i ++)
    {
        fprintf(toq,"%d |",toqq[i]);
        printf("%d : ",toqq[i]);
    }
    puts("");

    Sort_DESC(musbatt,j);
    printf("Musbat sonlar : ");
    for(int i = 0 ; i < j ; i ++)
    {
        fprintf(musbat,"%d |",musbatt[i]);
        printf("%d : ",musbatt[i]);
    }
    puts("");

    Sort_ASC(manfiyy,h);
    printf("Manfiy sonlar : ");
    for(int i = 0 ; i < h ; i ++)
    {
        fprintf(manfiy,"%d |",manfiyy[i]);
        printf("%d : ",manfiyy[i]);
    }
        return 0;
}









