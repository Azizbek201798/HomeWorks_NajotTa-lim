#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

typedef struct aeroport 
{
    char Samalyot_turi[20];
    char Uchish_sanasi[11];
    char Uchish_shaxri[20];
    char Qonish_shaxri[20];
    char Uchish_soati[11];
} aeroport;

void show_plane(aeroport key[])
{
    printf("Samalyot turi : %s",key->Samalyot_turi);
    printf("Uchish_Sanasi : %s",key->Uchish_shaxri);
    printf("Uchish_Shaxri : %s",key->Uchish_shaxri);
    printf("Qonish_shaxri : %s",key->Qonish_shaxri);
    printf("Uchish_Vaqti  : %s",key->Uchish_soati);

}

bool check_time(char st[])
{
    char st1[10];
    strcpy(st1,st);
    char *ptr = strtok(st1,":");
    int hour = atoi(ptr);
    ptr = strtok(NULL,":");
    int min = atoi(ptr);
    if ((hour == 15 && min > 0) || hour < 14 || hour > 15)
        return false;
    else 
        return true;
};

int main()
{
    system("clear");
    aeroport aero[10] = {{"Al - 100","21.04.2014","Samarqand","Termez","14:21"},
                       {"Boing -745","14.02.2034","Termez","Toshkent","14:59"},                       
                    };
    for (int i = 0; i < sizeof(aero)/sizeof(aeroport); i++)
    {
        bool check = false;
        if (check_time(aero[i].Uchish_soati) && stricmp(aero[i].Qonish_shaxri,"Toshkent") == 0)
        {
            show_plane(&aero[i]);
            check ==true;
            printf("************************************\n");
        }
        if (check == false){
            printf("Bu vaqt oralig'ida samalyotlar mavjud emas!\n");
        }
    }
};