#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int getRandom(int min,int max)
{
	return rand()%(max - min + 1) + min;
}

void find(int a[][10],int x,int y)
{
	int lk_max = 0;
	printf("Lokal Max = > ");
	for (int i = 1; i < x - 1; i++){
		for(int j = 1; j < y - 1; j++){
			if ((a[i][j] > a [i+1][j]) && (a[i][j] > a[i-1][j] && a[i][j] > a[i][j+1] && a[i][j] > a[i][j-1]) ){
				printf("%d | ",a[i][j]);
			}
		}
	}
	puts("");
}

int main()
{
	int m,n, mx[10][10];
	printf("m va n = ");
	scanf("%d %d",&m,&n);
	for (int i = 0; i < m; i++){
		for (int j = 0; j < n; j++){
			mx[i][j] = getRandom(10,99);
			printf("%4d",mx[i][j]); 
		}
		puts("");
	}
	find(mx,m,n);
}
