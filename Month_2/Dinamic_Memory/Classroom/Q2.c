#include <stdio.h>
#include <stdlib.h>

typedef struct Car
{
    char Name[10];
    char Model[20];
    char Color[20];
    int  Capacity;
    char Producer[10];
    char Category[10];
} Car;

void Input_Info(Car *cars)
{
    printf("Name     : %s");
    scanf(" %s",cars->Name);
    printf("Model    : %s");
    scanf(" %s",cars->Model);
    printf("Color    : %s");
    scanf(" %s",cars->Color);
    printf("Capacity : %d");
    scanf("%d",cars->Capacity);
    printf("Producer : %s");
    scanf(" %s",cars->Producer);
    printf("Category : %s");
    scanf(" %s",cars->Category);
}

void Show(Car *cars)
{
    printf("Name     : %s\n", cars->Name);
    printf("Model    : %s\n", cars->Model);
    printf("Color    : %s\n", cars->Color);
    printf("Capacity : %d\n", cars->Capacity);
    printf("Producer : %s\n", cars->Producer);
    printf("Category : %s\n", cars->Category);
}

int main()
{
    system("clear");
    Car cars[2];
    int index = 0;
    for (int i = 0; i < 2; i++){
        Input_Info(&cars[index]);
        index++;
    }
    for (int i = 0; i < 2; i++){
        Show(&cars[i]);
        puts("***********************");
    }
}

