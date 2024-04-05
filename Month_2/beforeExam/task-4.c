// ***topshiriq4***
// Davlat nomli struct yarating. Davlat tili ingliz tili bo'lgan va aholisi 
// 100 mlndan ortiq davlatlar haqidagi ma'lumotni matnli faylga chiqaring! 
  
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// DONE;

typedef struct Country{
    char name[50];
    int population;
    char language[10];
    double area;
    char capital[50];
} Country;

void writeCountryInfoToFile(char *filename, Country *countries, int numCountries) {
    FILE* file = fopen("result.txt", "w");
    if (file == NULL) {
        printf("Error while opening file %s.\n", "result.txt");
        return;
    }

    for (int i = 0; i < numCountries; i++) {
        if (strcmp(countries[i].language,"English") == 0 && countries[i].population > 100)
        {
            fprintf(file, "Country: %s\n", countries[i].name);
            fprintf(file, "Population: %d million\n", countries[i].population);
            fprintf(file, "Language: %s\n", countries[i].language);
            fprintf(file, "Area: %.2f square kilometers\n", countries[i].area);
            fprintf(file, "Capital: %s\n\n", countries[i].capital);
        }
    }

    fclose(file);
}

int main() {

    system("clear");

    Country countries[] = {
        {"Surxondaryo", 331,"English", 9.83, "Termiz"},
        {"Qashqadaryo", 67,"Uzbek",0.24, "Qarshi"},
    };
    int numCountries = sizeof(countries) / sizeof(countries[0]);
 
    writeCountryInfoToFile("result.txt", countries, numCountries);

    printf("Country information written to %s.\n", "result.txt");

    return 0;
}