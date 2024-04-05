// Input  : num = 123; add = 40; 
// OutPut : 40123;
#include <stdio.h>

int addNumber(int num, int add)
{
    int son = num, count = 0;
    while(son)
    {
        son /= 10;
        add *= 10;
    }
    return add + num;
}

int main()
{
    int num,add;
    printf("Son va unga qo'shish kerak bo'lgan sonni kiriting : ");
    scanf("%d %d",&num,&add);
    int res = addNumber(num,add);
    printf("Result : %d\n",res);    
}