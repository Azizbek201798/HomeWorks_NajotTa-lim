#include <stdio.h>

void show_matrix(int a[][10],int x,int y)
{
	for(int i = 0; i < x; i++){
		for(int j = 0; j < y; j++){
			printf("%6d",a[i][j]);
		}
		puts("");
	}
}

int find_index(int a[][10],int x,int y)
{
	int res = -1;
	for (int i = 0; i < x; i++){
		for (int j = 0; j < y; j++){
			if ((a[i][j] % 3 == 0) && (a[i][j] % 5 == 0)){
				 return i;
				 
			} 
		}
	}
	return res;
}

int main()
{
	int m,n;
	printf("m va n = ");
	scanf("%d %d",&m,&n);
	int mx[10][10];
	for (int i = 0; i < m; i++){
		for(int j = 0; j < n; j++){
			printf("mx[%d][%d] => ",i,j);
			scanf("%d",&mx[i][j]);
		}
	}
	printf("Before ...\n");
	show_matrix(mx,m,n);
	int result = find_index(mx,m,n);
	if(result != -1){
		for (int k = 0; k < n; k++ ){
			mx[result][k] = mx[result][k]*mx[result][k]; 
		}
        printf("After...\n");
	show_matrix(mx,m,n);			
	} else {
		printf("Bunday satr mavjud emas!\n");
	}
}
