// 7 - masala. Fayl berilgan faylning tarkibidagi barcha polindrom so'zlarni yangi faylga ko'chirib yozing
// Izoh: polindrom - 'kiyik','aka'
// #matnli_fayllar_bilan_ishlash;
#include <stdio.h>
#include <ctype.h>
#include <string.h>
int polindrom1(char s[])
{
	int n = strlen(s);
	int m = n-1;
	for(int i = 0; i < n ; i++)
	{
		if(s[i] != s[m])
			return 0;
		m--;
	}
	return 1;
}
int main ()
{
        system("clear");
        int n;
        char satr[100];
        FILE *file = fopen("task7.txt","r+");
        FILE *poli = fopen("palindrom.txt","w+");
        while(file ==  NULL)
        {
                puts("faylni ochishda xatolik boldi!");
                        return 0;
        }
        while(fscanf(file,"%s",satr) != EOF)
        {
              	if(polindrom1(satr)==1){
			fputs(" ",poli);
			fputs(satr,poli);
			puts(satr);
			}
        }
        printf("\n");
        fclose(file);
        fclose(poli);
        return 0;
}

// DONE;