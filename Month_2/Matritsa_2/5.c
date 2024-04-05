#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

int getRandom(int min ,int max)
{
	return min + rand()%(max - min + 1);
}

int sum_max_ind(int a[][10],int x,int y)
{
	int sum = 0,k,min = INT_MAX;
	for (int j = 0; j < y;j++){
		sum = 0;
		for (int i = 0; i < x; i++ ){
			sum += a[i][j];
		}
		printf(" =%2d",sum);
		if (sum < min){
			min = sum;
			k = j;
		}
	} 
	return k;
}	

int main()
{
	int m,n,mx[10][10];
	printf("m va n = ");
	scanf("%d%d",&m,&n);
	srand(time(NULL));
	for (int i = 0; i < m; i++){
		for (int j = 0; j < n; j++){
			mx[i][j] = getRandom(1,9);
			printf("%4d",mx[i][j]);
		}
		puts("");
	}
	int res = sum_max_ind(mx,m,n),max = mx[0][res];
	for(int i = 1; i < m; i++){
		if (max < mx[i][res]){
			max = mx[i][res];
		}
	}
	printf("\nMax element in Min SUM = %d\nCongratulatins you solved this!\n",max);
}
