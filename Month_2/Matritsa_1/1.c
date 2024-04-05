#include <stdio.h>

int main()
{
	int m,n;
	printf("m : n = ");
	scanf("%d %d",&m,&n);
	int mtx[10][10];
	
	for (int i = 0; i < m; i++){
		for (int j = 0; j < n; j++){
			mtx[i][j] = 5*j;
			printf("%4d",mtx[i][j]);
		}
		puts("");
	}
}
