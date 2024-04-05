// 3-masala. Faylni nomini input orqali kiriting. Faylni nomidagi raqamlarni kamayish tartibida new1 fayliga 
// va new2 fayliga esa ushbu raqamlarni o'sish tartibida yozing.
// Input: "7519318749"
// Output: new1 faylida: 9 9 8 7 7 5 4 3 1 1
// new2 faylida: 1 1 3 4 5 7 7 8 9 9

#include <string.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
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
        srand(time(0));
        int n,x;
        char satr[1000],satrr[1000];
        FILE *file = fopen("top3.txt","w+");
        FILE *new1 = fopen("new1.txt","w+");
        FILE *new2 = fopen("new2.txt","w+");
        while(file ==  NULL)
        {
                puts("faylni ochishda xatolik boldi!");
                        return 0;
        }
        printf("nechta random raqam bolsin: ");
        fflush(stdout);
        scanf("%d",&n);
        for(int i = 0 ; i < n+1 ; i ++)
        {
                x = rand()% 9 + 1;
                fprintf(file,"%d",x);
                printf("%d",x);
        }
        rewind(file);
        while(fgets(satrr,1000,file))
        {
                strcat(satr,satrr);
        }
        sort(satr,n);
        puts("\n");
        for(int i = 0 ; i < n ; i++)
        {
                if(satr[i] >= 48 && satr[i] <= 58)
                        fprintf(new2,"%c ",satr[i]);
              if(satr[i]<=58 && satr[i]>=48)
                      printf("%c |",satr[i]);
        }
        puts("\n");
	for(int i = n ; i > 0 ; i-- )
        {
                if(satr[i] >= 48 && satr[i] <= 58){
                        fprintf(new1,"%c ",satr[i]);
                        printf("%c|",satr[i]);
                }
        }
	printf("\nustoz sortirovkasi new1 va new2 degan faylda boladi");
        fclose(file);
        fclose(new1);
        fclose(new2);
        return 0;
}

// DONE;