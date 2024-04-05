#include <stdio.h>
#include <string.h>

typedef struct Talaba
{
    char Ismi[20];
    int Course;
    int Stipendiyasi;
} Talaba;

void Input_Info(Talaba *Users)
{
    printf("Ismi : ");
    scanf(" %s",Users->Ismi);
    printf("Course : ");
    scanf("%d",&Users->Course);
    printf("Stipendiyasi : ");
    scanf("%d",&Users->Stipendiyasi);
}

void Show_Info(Talaba *Users)
{
    printf("Ismi         : %s\n",Users->Ismi);
    printf("Course       : %d\n",Users->Course);
    printf("Stipendiyasi : %d\n",Users->Stipendiyasi);
}

int main()
{
    system("clear");
    int N;
    printf("Foydalanuvchilar sonini kiriting => ");
    scanf("%d",&N);
    Talaba Users[100];
    puts("**************************************");
    for (int i = 0; i < N; i++)
    {
        Input_Info(&Users[i]);
        printf("******************\n");
    }
    system("clear");
    printf("Barcha talabalar ro'yxati!\n-----------------------\n");
    for (int i = 0; i < N; i++)
    {
        if(strlen(&Users[i].Ismi) < 6)
        {
            Show_Info(&Users[i]);
            printf("-----------------------\n");
        }
    }
}
















