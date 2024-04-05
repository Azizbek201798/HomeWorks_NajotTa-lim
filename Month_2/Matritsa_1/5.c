#include <stdio.h>

void Swap(int ant[100][100], int x, int y){
	for (int j = 0; j < y; j++){
		int temp;
		for (int i = 0; i < x/2; i ++){
			temp = ant[i][j];
			ant[i][j] = ant[i + x/2][j];
			ant[i + x/2][j] = temp;
		}
	}
}

int main()
{
	int m,n;
	printf("m(juft) va n => ");
	scanf("%d %d",&m,&n);
	int mtx[100][100];
	for (int i = 0; i < m; i++){
		for (int j = 0; j < n; j++){
			printf("mtx[%d][%d] => ",i,j);
			scanf("%d",&mtx[i][j]);
		}
	}
	// Before;
	printf("\nBefore\n");
        for (int i = 0; i < m; i++ ){
                for (int j = 0; j < n; j++){    
                        printf("%4d",mtx[i][j]);
                }
                puts("");
        }
	// Swapping;
	Swap(mtx,m,n);
	// Show After swap elements
	printf("After swapping\n");
	for (int i = 0; i < m; i++ ){
		for (int j = 0; j < n; j++){	
			printf("%4d",mtx[i][j]);
		}
		puts("");
	}
}
