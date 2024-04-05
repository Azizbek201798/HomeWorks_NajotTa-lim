#include <stdio.h>

int main()
{
	int m = 5,n = 6;
	int mtx[m][n];
	for (int i = 0; i < m; i++){
		for (int j = 0; j < n; j++){
			mtx[i][j] = j+1;
			printf("%3d",mtx[i][j]); 
		}
		puts("");
	}
}
