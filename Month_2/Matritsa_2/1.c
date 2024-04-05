#include <stdio.h>

void show_matrix(int b[10][10],int k)
{
	for (int i = 0; i < k; i++){
		for (int j = 0; j < k; j++){
			printf("%4d",b[i][j]);
		}
		puts("\n");
	}
}

void spiral_matrix(int a[10][10],int x)
{
	int num = 1,start_row = 0, end_row = x-1, start_col = 0, end_col = x-1;	

	while(start_row <= end_row && start_col <= end_col){	
	for (int j = start_col; j <= end_col; j++){
		a[start_row][j] = num++;
	}
	start_row++;
	for(int i = start_row; i <= end_row; i++ ){
		a[i][end_col] = num++;
	}
	end_col--;
	for (int j = end_col; j >= start_col; j--){
		a[end_row][j] = num++;
	}
	end_row--;
	for (int i = end_row; i >= start_row; i--){
		a[i][start_col] = num++;
	}
	start_col++;
	}
}

int main()
{
	int n; 
	printf("n = ");
	scanf("%d",&n);
	int mx[10][10];
	spiral_matrix(mx,n);
	show_matrix(mx,n);
}
