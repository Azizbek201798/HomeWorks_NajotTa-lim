#include <stdio.h>
#include <ctype.h>

int count_letter(char x[100],int index,int count)
{
    if (x[index] == '\0')
        return count;
    if (isalpha(x[index]))
        count++;
    return count_letter(x,index + 1,count); 
}
int main()
{
    char str[100];
    printf("Enter str : ");
    fgets(str,100,stdin);
    printf("Harflar soni => %d\n",count_letter(str,0,0));

}