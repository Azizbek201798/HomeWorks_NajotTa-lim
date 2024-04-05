#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

int getRandom(int min,int max)
{
	return min + rand()%(max - min + 1);
}

int max_index(int a[][10],int x,int y)
{
	int res = -1, mult, max = 1, k = 0;
	for (int j = 0; j < y; j++){
		mult = 1;
		for (int i = 0; i < x; i++){
			mult *= a[i][j];
		}
		printf("= %d ",mult);
		if (mult > max){
			max = mult;
			k = j;
		}
	}
	return k;
}

int main()
{
	srand(time(NULL));
	int m,n,mx[10][10];
	printf("m va n = ");
	scanf("%d %d",&m,&n);
	for (int i = 0; i < m; i++){
		for(int j = 0; j < n; j++){
			mx[i][j] = getRandom(1,10);
			printf("%5d",mx[i][j]);
		}
		puts("");
	}
	int result = max_index(mx,m,n), min =INT_MAX;
	printf("\nMax row ...\n");
	for (int i = 0; i < m; i++){
		printf("%4d",mx[i][result]);
		if (mx[i][result] < min){
			min = mx[i][result];
		}
	}
	printf("\nMin = %d\n",min);
}
