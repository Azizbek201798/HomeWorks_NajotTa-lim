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

// Bu funksiya uchish vaqti kunduzgi yoki kechki 2 dan 3 gacha bo'lgan va Qo'nish shaxri Toshkent bo'lgan Samalyotlar ro'yxatini chiqaradi!
bool Check_Time(char time[], char city[])
{
    int hour = 0, min = 0;
    hour = (time[0] - '0') * 10 + (time[1] - '0');
    min = (time[3] - '0') * 10 + (time[4] - '0');
    if ((hour == 14 && min <= 59) || (hour == 2 && min <= 59) && !strcmp(city,"Toshkent")){
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

    // This check time for print All;

    for (int i = 0; i < N; i++)
    {
        if (Check_Time(Data[i].Uchish_Vaqti,Data[i].Qonish_Shaxri))
        {
            //printf("%d : %s",&Data[i].Uchish_Vaqti,Data[i].Qonish_Shaxri);
            Show_Info(&Data[i]);
            printf("***************************************\n");
        }
    }    
}
