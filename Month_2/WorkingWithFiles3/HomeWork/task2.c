// ***topshiriq_2***
// Binar faylga "Country" nomli struct yaratib, 5 ta mamlakat haqida ma'lumotlarni
// kiriting. Aholisi 100 mlndan yuqori mamlakatlar haqida ma'lumotni
// Country.html nomli matnli faylga yozing.
#include <stdio.h>
#include <stdlib.h>
// DONE;
typedef struct Country {
    char name[50];
    int population;
} Country;

void writeToFile(char* filename, Country* countries, int size) {
    FILE* file = fopen(filename, "wb");
    if (file == NULL) {
        printf("Error while reading file : %s\n", filename);
        return;
    }

    fwrite(countries, sizeof(Country), size, file);
    fclose(file);
}

int main() {
    system("clear");
    Country countries[5];

    strcpy(countries[0].name, "China");
    countries[0].population = 140;

    strcpy(countries[1].name, "India");
    countries[1].population = 135;

    strcpy(countries[2].name, "United States");
    countries[2].population = 33;

    strcpy(countries[3].name, "Indonesia");
    countries[3].population = 27;

    strcpy(countries[4].name, "Pakistan");
    countries[4].population = 225;

    writeToFile("HomeWork/Country", countries, 5);

    FILE* htmlFile = fopen("HomeWork/Country.html", "w");
    if (htmlFile == NULL) {
        printf("Failed to open the file HomeWork/Country.html\n");
        return 0;
    }

    fprintf(htmlFile, "<html>\n");
    fprintf(htmlFile, "<body>\n");
    fprintf(htmlFile, "<h1>Countries with Population above 100 million</h1>\n");
    fprintf(htmlFile, "<ul>\n");

    for (int i = 0; i < 5; i++) {
        if (countries[i].population > 100) {
            fprintf(htmlFile, "<li>%s - %d million</li>\n", countries[i].name, countries[i].population);
        }
    }

    fprintf(htmlFile, "</ul>\n");
    fprintf(htmlFile, "</body>\n");
    fprintf(htmlFile, "</html>\n");

    fclose(htmlFile);

    return 0;
}