#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int getRandom(int min, int max)
{
	return min + rand()%(max - min + 1);
}

void Sort(int a[100][100],int x, int y){
	int temp;
	for (int j = 0; j < y; j++){
		for (int k = 0; k < x; k++){
			for (int i = 1; i < x - k; i++){
				if (a[i-1][j] > a[i][j]){
					temp = a[i-1][j];
					a[i-1][j] = a[i][j];
					a[i][j] = temp; 
				}
			}
		}
	}
}

int main()
{
	int row,col;
	printf("Row and Col = ");
	scanf("%d %d",&row,&col);
	int mtx[100][100];
	printf("Before Sorting ...\n");
	for (int i = 0; i < row; i++){
		for (int j = 0; j < col; j++){
			mtx[i][j] = getRandom(10,30);
			printf("%4d",mtx[i][j]);
		}
		printf("\n");
	}
	// After Sorting;
	printf("After sorting ...\n");
	Sort(mtx,row,col);
	// Printing After Sorting;
        for (int i = 0; i < row; i++){
                for (int j = 0; j < col; j++){
                        printf("%4d",mtx[i][j]);
                }
                printf("\n");
        }

}
