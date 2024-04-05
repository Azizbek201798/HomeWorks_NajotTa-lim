#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int irand(int a,int b){

        return rand()%(b-a+1)+a;

}
void sort_kop(int arr[],int count){

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
void sort_kam(int arr[],int count){

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
    FILE *file = fopen ("problem5.dat","wb+");
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
    //printf("{%d}",son);
    int siz = son/4;
    //printf("{%d}",siz);
    rewind(file);
    int mas[siz];
    fread(mas,sizeof(int),siz,file);
    fclose(file);
    puts("");
    int toqq[100],juftt[100],manfiyy[100],musbatt[100];
    int k = 0 , l = 0, j = 0 , h = 0;
    FILE *toq = fopen("toq_num.txt","w");
    FILE *juft = fopen("juft_num.txt","w");
    FILE *manfiy = fopen("manfiy_num.txt","w");
    FILE *musbat = fopen("musbat_num.txt","w");
    for(int i = 1 ; i <= siz ; i ++)
    {
        if(mas[i] % 2==0){
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
    sort_kop(juftt,k);
    for(int i = 0 ; i < k ; i ++)
    {
        fprintf(juft,"%d |",juftt[i]);
        printf("%d |",juftt[i]);
    }
    puts("");
    sort_kam(toqq,l);
    for(int i = 0 ; i < l ; i ++)
    {
        fprintf(toq,"%d |",toqq[i]);
        printf("%d /",toqq[i]);
    }
    puts("");
    sort_kam(musbatt,j);
    for(int i = 0 ; i < j ; i ++)
    {
        fprintf(musbat,"%d |",musbatt[i]);
        printf("%d [",musbatt[i]);
    }
    puts("");
    sort_kop(manfiyy,h);
    for(int i = 0 ; i < h ; i ++)
    {
        fprintf(manfiy,"%d |",manfiyy[i]);
        printf("%d ]",manfiyy[i]);
    }
    
    

        return 0;
}









