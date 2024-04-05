#include<stdio.h>
#include<string.h>
#include<stdbool.h>
bool solishtir(char s[],char c[]){

        char res[100[;
        int index=0;
        for(int i=strlen(c)-1;i>=0;i--){

                res[index++]=c[i];
                }

                res[index]='\0'

        return strcmp(s,res)==0;
}
int main(){

        system("clear");

        FILE*f=fopen(fayl nomini ozilar kiritilAR,"r");
        if(f==NULL){

        printf("FAylni ochishda xatolik!");
        return 0;
        }
        fseek(f,0,SEEK_END);
        int size=ftell(f);
        char satr[1000];
        rewind(f);
        fgets(satr,1000,f);

        char str[100],ctr[100];
        int t=0;

        for(int i=0;i<size/2;i++){

                str[t]=satr[i];
                ctr[t]=satr[size-1-i];
                str[t+1]='\0'
                ctr[t+1]='\0'

        if(solishtirish(str,ctr)==true){

                if(strlen(str)!=1){

                printf("len=%d\n",t+1);
                break;

                }

        }

        t++;

        }

        return 0;
}