#include "stdio.h"

int main(){
    FILE *ptr = fopen("special/2.txt","r");
    FILE *fcb = fopen("special/output2.txt","w");
    char str[100];
    int count = 0,ignore;
    printf("Input ignored num : ");
    scanf("%d",&ignore);
    while (fgets(str,100,ptr))
    {
        count++;
        if (count == ignore)
        {
            continue;
        }
        fprintf(fcb,"%s",str);
    }
    fclose(ptr);
    fclose(fcb);
}
