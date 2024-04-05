#include <stdio.h>

typedef struct Talaba
{
    char Ismi[10];
    int Age;
    int Stipendiya;
    int Grade[5];
} Talaba;

void Input_Info(Talaba *Users)
{
    printf("Talaba ismi : ");
    scanf(" %s",Users->Ismi);
    printf("Yoshi : ");
    scanf("%d",&Users->Age);
    printf("Stipendiya miqdori : ");
    scanf("%d",&Users->Stipendiya);
    for (int i = 0; i < 5; i++){
        printf("Grade [%d] = ",i+1);
        scanf("%d",&Users->Grade[i]);
    }
}

void Show_info(Talaba *Users)
{
    printf("Talaba ismi  %s:\n ",Users->Ismi);
    printf("Talaba yoshi %d:\n ",Users->Age);
    printf("Stipendiyasi %d:\n ",Users->Stipendiya);
    for (int i = 0; i < 5; i++)
    {
        printf("Grade [%d]: %d; ",i+1,Users->Grade[i]);
    }
    puts("");
}

int Average_Grade(Talaba *Users)
{
    int sum = 0,avg;
    for (int i = 0; i < 5; i++)
    {
        sum += Users->Grade[i];
    }
    return avg = sum / 5;
}

int main()
{
    system("clear");
    int N;
    Talaba Users[100];
    printf("N => ");
    scanf("%d",&N);
    int index = 0;
    for (int i = 0; i < N; i++)
    {
        printf("%d - User => ",i+1);
        Input_Info(&Users[index]);
        index++;
    }
    system("clear");
    for (int i = 0; i < N;i++)
    {
        if(Average_Grade(&Users[i]) == 4){
            Show_info(&Users[i]);
            printf("**************************************************************************\n");
        }
    }
}
