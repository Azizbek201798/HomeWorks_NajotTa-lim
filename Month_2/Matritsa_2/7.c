#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int getRandom(int min,int max)
{
	return  rand()%(max - min + 1) + min;
}

int find(int a[10][10],int x, int y)
{
	int res = -1,k = -1;
	int c_even, c_odd;
	for(int j = 0; j < y; j++){
		c_even = 0;
		c_odd = 0;
		for (int i = 0; i < x; i++){
			if (a[i][j] % 2 == 0){
				c_even++;
			} else {
				c_odd++;
			}
		}
		if (c_even == c_odd){
			k = j;
		}
	}
    if (k != -1){
        return k;
    } else {
        return res;
    }
	
}

int main()
{
	srand(time(NULL));
	int m,n,mx[10][10];
	printf("m va n = ");
	scanf("%d%d",&m,&n);
	for (int i = 0; i < m; i++){
		for (int j = 0; j < n; j++){
			mx[i][j] = getRandom(0,5);
			printf("%5d",mx[i][j]);
		}
		puts("");
	}
	int result = find(mx,m,n);
	if (result != -1){
		printf("Juft va Toq elementlari teng bo'lgan ohirgi ustun!\n");
		for (int i = 0; i < m; i++){
			printf("%5d",mx[i][result]);
		}
	} else {
		printf("NOT FOUND");
	}
	puts("");
}
