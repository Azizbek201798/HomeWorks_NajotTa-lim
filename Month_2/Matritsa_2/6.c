#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int getRandom(int min,int max)
{
	return  rand()%(max - min + 1) + min;
}

int find(int a[10][10],int x, int y)
{
	int res = -1;
	int c_positive, c_negative;
	for(int i = 0; i < x; i++){
		c_positive = 0;
		c_negative = 0;
		for (int j = 0; j < y; j++){
			if (a[i][j] > 0){
				c_positive++;
			} else if(a[i][j] < 0 && a[i][j] != 0){
				c_negative++;
			}
		}
		if (c_negative == c_positive){
			return i;
		}
	}
	return res;
}

int main()
{
	srand(time(NULL));
	int m,n,mx[10][10];
	printf("m va n = ");
	scanf("%d%d",&m,&n);
	for (int i = 0; i < m; i++){
		for (int j = 0; j < n; j++){
			mx[i][j] = getRandom(-10,10);
			printf("%5d",mx[i][j]);
		}
		puts("");
	}
	int result = find(mx,m,n);
	if (result != -1){
		printf("Musbat va manfiy elementlari teng bo'lgan birinchi qator!\n");
		for (int j = 0; j < n; j++){
			printf("%5d",mx[result][j]);
		}
	} else {
		printf("NOT FOUND");
	}
	puts("");
}
