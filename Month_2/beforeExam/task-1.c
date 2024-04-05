// ***topshiriq1***
// Matnli fayldagi so'zlarni birinchini ikkinchiga, uchinchini 
// toâ€™rtinchiga va hokazo   oâ€™zgartiruvchi dastur tuzing.
// >>> M: Mana  senga  olam  olam  gul! Havo yaxshi. 
// <<< Natija: senga Mana olam olam gul! yaxshi Havo.  

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// DONE;

void swapWords(char *word1, char *word2) {
    char temp[100];
    strcpy(temp, word1);
    strcpy(word1, word2);
    strcpy(word2, temp);
}

int main() {

    system("clear");
    
    FILE* inputFile = fopen("input.txt", "r");
    FILE* outputFile = fopen("output.txt", "w");

    if (inputFile == NULL || outputFile == NULL) {
        printf("Failed to open files.\n");
        return 1;
    }

    char word1[100];
    char word2[100];
    int wordCount = 0;

    while (fscanf(inputFile, "%s %s", word1, word2) == 2) {
        if (wordCount % 2 == 0) {
            swapWords(word1, word2);
        }
        fprintf(outputFile, "%s %s ", word1, word2);
        wordCount++;
    }

    fclose(inputFile);
    fclose(outputFile);

    printf("Words swapped and written to output.txt.\n");
    return 0;
}