#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

int getRandom(int min,int max)
{
	return rand()%(max - min + 1) + min;
}

void lk_min(int a[100][100],int n,int k){
	int lk_imn = INT_MAX;
	for (int i = 1; i < n - 1; i++){
		for (int j = 1; j < k - 1; j++){
			if (a[i][j] < a[i-1][j] && a[i][j] < a[i+1][j] && a[i][j] < a[i][j-1] && a[i][j] < a[i][j+1]){
				a[i][j] = 0;
			}  
		}
	}
}

int main()
{
	int x,y;
	srand(time(NULL));
	printf("x and y = ");
	scanf("%d %d",&x,&y);
	int mtx[100][100];

	// Elementlar kiritish;
	printf("Before ...\n");
	for (int i = 0; i < x; i++){
		for (int j = 0; j < y; j++){
			mtx[i][j] = getRandom(10,30);
			printf("%4d",mtx[i][j]);
		}
		printf("\n");
	}
	// Swap to zero;
	lk_min(mtx,x,y);
	// Print;
	printf("After ...\n");
	for (int i = 0; i < x; i ++){
		for (int j = 0; j < y; j ++){
			printf("%4d",mtx[i][j]);
		}
		puts("");
	}

}
