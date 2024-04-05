#include <stdio.h>

typedef struct Talaba
{
    char Ismi[20];
    int Stipendiya;
    int Course_degree;
} Talaba;

void Input_Info(Talaba *Users)
{
    printf("Talaba ismi : ");
    scanf(" %s",Users->Ismi);
    printf("Stipendiya : ");
    scanf("%d",&Users->Stipendiya);
    printf("Course_Degree : ");
    scanf("%d",&Users->Course_degree);
}

void Show_Info(Talaba *Users)
{
    printf("Ismi          : %s\n",Users->Ismi);
    printf("Stipendiyasi  : %d\n",Users->Stipendiya);
    printf("Course_Degree : %d\n",Users->Course_degree);

}

int Sum_Stipendiya(Talaba *Users)
{
    int Sum = 0;
    if (Users->Course_degree == 2){
        Sum += Users->Stipendiya;
    }
    return Sum;
}

int main()
{
    system("clear");
    int N, Total_Sum = 0;
    printf("N => ");
    scanf("%d",&N);
    Talaba Users[100];
    for (int i = 0; i < N; i++)
    {
        Input_Info(&Users[i]);
        printf("***********************\n");
    }
    for (int i = 0; i < N; i++)
    {
        Total_Sum += Sum_Stipendiya(&Users[i]);
    }
    system("clear");
    printf("Barcha ikkinchi kurslarga to'langan stipendiya miqdori : %d so'm!\n",Total_Sum);
    printf("\n***********************\n\nUmumiy Talabalar ro'yxati : \n\n");
    for (int i = 0; i < N; i++)
    {
        Show_Info(&Users[i]);
        printf("----------------------\n");

    }

}