#include "stdio.h"
#include "stdlib.h"
// Not done;
int main(){
    FILE *file1 = fopen("special/1.txt", "r");
    FILE *file2 = fopen("special/output.txt", "w");

    char word[100];
    int arr[1000], k = 0;
    while (fscanf(file1, "%s", word) != EOF){
        arr[k] = atoi(word);
        k++;
    }

    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k -i; ++j) {
            if (arr[j] >arr[j + 1] ){
                int box = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = box;
            }
        }
    }

 for (int i = 0; i < k; ++i) {
        printf("%d ",arr[i]);
    }
    // for (int i = 0; i < k; ++i) {
    //     fprintf(file2,"%d ",arr[i]);
    // }
    puts("");
    fclose(file1);
    fclose(file2);

}













