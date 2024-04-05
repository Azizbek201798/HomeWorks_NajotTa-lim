// 4-masala. Faylni nomini input orqali kiriting. Faylni nomidagi lotin harflarini alfavit teskari tartibida new1 fayliga va new2 fayliga esa ushbu harflarni alfavit to'g'ri tartibida yozing.
// Input: "salom bolalar"
// Output: new1 fayl ichida: s r o m l l l b a a a  
// new2 fayl ichida: a a a b l l l m o r s

#include <string.h>
#include <stdio.h>
#include <ctype.h>
void sort(char s[] , int n)
{
        int temp;
        for( int i = 0 ; i < n ; i++)
        {
                for(int j = 0 ; j < n ; j++)
                {

                        if(s[j] > s[j+1])
                        {
                                temp = s[j+1];
                                s[j+1] = s[j];
                                s[j] = temp;
                        }
                }
        }

}
int main ()
{
	system("clear");
        int n,x;
        char satr[1000],satrr[1000];
        FILE *file = fopen("task4.txt","r");
        FILE *harf1 = fopen("harf1.txt","w+");
        FILE *harf2 = fopen("harf2.txt","w+");
        while(file ==  NULL)
        {
                puts("faylni ochishda xatolik boldi!");
                        return 0;
        }
        while(fgets(satrr,1000,file))
        {
                strcat(satr,satrr);
        }
        int s = strlen(satr);
	puts(satr);
        sort(satr,s);
        for(int i = 0 ; i < s+1 ; i++)
        {
                if(isalpha(satr[i])){
                        fprintf(harf2,"%c",satr[i]);
			printf("%c",satr[i]);
		}
	}
	puts("\n");
        for(int i = s ; i > 0 ; i-- )
        {
                if(isalpha(satr[i])){
                        fprintf(harf1,"%c",satr[i]);
                        printf("%c",satr[i]);
                }
        }
	printf("\n");
        fclose(file);
        fclose(harf1);
        fclose(harf2);
        return 0;
}
//DONE;

