#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int getRandom(int min,int max)
{
	return rand()%(max - min + 1) + min;
}

bool isPrime(int z,int x)
{
	for (int k = 2; k < z; k++){
		if (z % k == 0){
			return false;
		}
	}
	return true;
}

int main()
{
	int n;
	srand(time(NULL));
	printf("n = ");
	scanf("%d",&n);
	int mtx[n][n];
	for (int i = 0; i < n; i++ ){
		for (int j = 0; j < n; j++){
			mtx[i][j] = getRandom(10,30);
			printf("%4d",mtx[i][j]);
		}
		printf("\n");
	}
	// Functionni tekshirish;
	int count = 0;
	for (int i = 0; i < n; i ++){
		for (int j = 0; j < n; j++){
			if (isPrime(mtx[i][j],n) == true){
				count ++;
				printf("%d | ",mtx[i][j]);	
			}
		}
	}
	printf("\nCount = %d\n",count);
}
