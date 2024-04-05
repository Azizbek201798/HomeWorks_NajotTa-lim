// 5-masala. Faylni ichida matn berilgan va ushbu matndagi sonlarni yig'indisini son+son+.. ko'rinishida chiqaring.
// Input(Faylni ichida): "FoundationN50 21.11.2023"
// Output: 50+21+11+2023=2105

#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main()
{
	system("clear");
	FILE *fayl = fopen("task5.txt","r");
	if(fayl == NULL)
	{
		puts("Faylni o'qishda xatolik!");
		return 0;
	}
	char satr[1000];
	int son[1000];
	while(fgets(satr,1000,fayl))
	{
		continue;
	}
	fclose(fayl);

    int numbers[100], count = 0, num = 0, sum = 0; 
    
	for (int i = 0; satr[i] != '\0'; i++) {
        if (isdigit(satr[i])) {
            num = num * 10 + (satr[i] - '0');
        } else {
            if ( num != 0) {
                numbers[count++] = num;
                num = 0;
            }
        }
    }
    if (num != 0) {
        numbers[count++] = num;
    }
    for (int i = 0; i < count; i++)
	{
		sum += numbers[i];
	}
	FILE *file = fopen("result.txt","w");
	for (int j = 0; j < count - 1; j++)
	{
		fprintf(file,"%d + ",numbers[j]);
	}
	fprintf(file," %d = ",numbers[count-1]);
	fprintf(file," %d",sum);
	fclose(file);
	return 0;
}

// DONE;