#include <stdio.h>

// Time nomli struct elon qiling uning propertylari quyidagidan iborat:

// - Hour(Soati);
// - Minut(Daqiqa);
// - Sekund(Soniyasi);

// ushbu classdan 5 ta object yarating.

// Har bir object uchun tungi soat 24:00:00 gacha qancha vaqt qolganini aniqlaydigan funksiya tuzing.

typedef struct Time
{
    int Hour;
    int Min;
    int Sekund;
} Time;

int main()
{
    int res;
    Time times[2] = {{12,15,24},{15,45,59}};
    for (int i = 0; i < sizeof(times)/sizeof(Time); i++)
    {
        res = (23 * 2600 - times[i].Hour * 3600) + (59 * 60 - times[i].Min * 60) + (59 - times[i].Sekund);
        printf("%d : %d : %d vaqt qoldi!\n",res / 3600, res % 3600 /60, res %3600 % 60);
        puts("***********************************");
    }

}