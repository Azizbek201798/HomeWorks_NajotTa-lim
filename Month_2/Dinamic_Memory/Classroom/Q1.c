#include <stdio.h>

typedef struct Car
{
    char Name[10];
    char Model[20];
    char Color[20];
    int  Capacity;
    char Producer[10];
    char Category[10];
} Car;

void Show(Car obj[])
{
    printf("Name     : %s\n", obj->Name);
    printf("Model    : %s\n", obj->Model);
    printf("Color    : %s\n", obj->Color);
    printf("Capacity : %d\n", obj->Capacity);
    printf("Producer : %s\n", obj->Producer);
    printf("Category : %s\n", obj->Category);
}

int main()
{
    system("clear");
    Car car1 = {"Malibu-2","101","Black",20,"USA","Sedan"};
    Car car2 = {"Tahoe","919","White",40,"USA","Sedan"};
    Show(&car1);
    puts("***********************");
    Show(&car2);
}

