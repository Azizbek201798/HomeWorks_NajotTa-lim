#include <stdio.h>
#include <stdbool.h>
#include <string.h>
typedef struct Aeroport
{
    char Turi[10];
    char Uchish_Sanasi[30];
    char Uchish_Shaxri[20];
    char Qonish_Shaxri[20];
    char Uchish_Vaqti[20];
} Aeroport;

void Input_Info(Aeroport *Data)
{
    printf("Samalyot turini kiriting             : ");
    scanf(" %s",Data->Turi);
    printf("Uchish sanasini kiriting(dd.mm.yyyy) : ");
    scanf(" %s",Data->Uchish_Sanasi);
    printf("Uchish shaxri                        : ");
    scanf(" %s",Data->Uchish_Shaxri);
    printf("Qo'nish shaxri                       : ");
    scanf(" %s",Data->Qonish_Shaxri);
    printf("Uchish vaqti(hh.mm)                  : ");
    scanf(" %s",Data->Uchish_Vaqti);
}

void Show_Info(Aeroport *Data)
{
    printf("Samalyot turi            : %s\n",Data->Turi);
    printf("Uchish sanasini kiriting : %s\n",Data->Uchish_Sanasi);
    printf("Uchish shaxri            : %s\n",Data->Uchish_Shaxri);
    printf("Qo'nish shaxri           : %s\n",Data->Qonish_Shaxri);
    printf("Uchish vaqti             : %s\n",Data->Uchish_Vaqti);
}

bool Check_Mouth(char Data[])
{
    int month = 0;
    for (int i = 3; i <= 4; i++)
    {
        month = month * 10 + (Data[i] - '0');
    }
    if (month >= 3 && month <= 5)
    {
        return true;
    }
    return false;
}

int main()
{
    system("clear");
    int N;
    printf("Nechta ma'lumot kiritmoqchisiz => ");
    scanf("%d",&N);
    printf("\n***********************************\n\n");
    Aeroport Data[100];

    // This Input Data;

    for (int i = 0; i < N; i++ )
    {
        Input_Info(&Data[i]);
        printf("***************************************\n");
    }
    system("clear");

    // This check month for Spring and print All;

    for (int i = 0; i < N; i++)
    {
        if (Check_Mouth(Data[i].Uchish_Sanasi))
        {
            Show_Info(&Data[i]);
            printf("***************************************\n");
        }
    }    
};
