#include <stdio.h>
#include <ctype.h>

int checkDate(char date[100]) {
	int day = 0, month = 0, year = 0;
	int i = 0;

	while (isdigit(date[i])) {
        	day = day * 10 + (date[i] - '0');
        	i++;
    	}

    	if (date[i] != '.') {
    		return 0;
    	}
    	i++;

	while (isdigit(date[i])) {
    		month = month * 10 + (date[i] - '0');
    		i++;
    	}
	if (date[i] != '.') {
    	return 0;
    	}
    	i++;

	while (isdigit(date[i])) {
        	year = year * 10 + (date[i] - '0');
        	i++;
    	}
	if (date[i] != '\0') {
        return 0;
    	}

    	if (day < 1 || day > 31 || month < 1 || month > 12 || year < 1) {
        	return 0; 
    	}

	return 1;
}

int main() {
    char date[100];
    printf("Sanani kiriting(dd.mm.yyyy): ");
    scanf("%10s", date);

    if (checkDate(date)) {
        printf("To'g'ri\n");
    } else {
        printf("Noto'g'ri\n");
    }

    return 0;
}
