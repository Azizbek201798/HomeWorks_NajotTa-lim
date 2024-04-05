// 6-masala. Faylda ma'lumot berilgan. Fayldagi barcha katta harflarni kichik harfga kichiklarini katta harfga almashtiring!
// Input: "Salom yoshlaR"
// Output: "sALOM YOSHLAr"

#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main ()
{
        system("clear");
        int n,x;
        char satr[1000],satrr[1000];
        FILE *file = fopen("task6.txt","r");
        FILE *harf = fopen("harf.txt","w+");
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
	puts("\n");
        for(int i = 1 ; i < s ; i++)
        {
                if(isupper(satr[i]) > 0){
                        fprintf(harf,"%c",satr[i]+32);
                }
		else if(islower(satr[i]) > 0)
			fprintf(harf,"%c",satr[i]-32);
        }
        printf("\n");
        fclose(file);
        fclose(harf);

        return 0;
}
// DONE;
