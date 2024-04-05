#include <stdio.h>
#include <stdbool.h>

typedef struct User
{
    char Name[10];
    char Login[20];
    char password[20];
    int  age;
    char country[10];
    char gender[10];
    float height;
    float weight;
    int brith_year;
    char email[20];
    int year_of_experience;
    bool children;
} User;

void Input_info(User *User)
{
    printf("Ismi          : %s",User->Name);
    scanf("%s",User->Name);
    printf("Login         : %s",User->Login);
    scanf("%s",User->Login);
    printf("Password      : %s",User->password);
    scanf("%s",User->password);
    printf("Age           : %d",User->age);
    scanf("%d",&User->age);
    printf("Country       : %s",User->country);
    scanf("%s",User->country);
    printf("Gender        : %s",User->gender);
    scanf("%s",User->gender);
    printf("Height        : %f",User->height);
    scanf("%f",User->height);
    printf("Weight        : %f",User->weight);
    scanf("%f",User->weight);
    printf("Brith_day     : %d",User->brith_year);
    scanf("%s",User->brith_year);
    printf("Email         : %s",User->email);
    scanf("%s",User->email);
    printf("Year_of_exp   : %d",User->year_of_experience);
    scanf("%d",User->year_of_experience);
    printf("Children      : %s",User->children ? "Bor\n" : "Yoq\n");
    scanf("%d",User->children);
}

void show_info(User *User)
{
    printf("Ismi          : %s",User->Name);
    printf("Login         : %s",User->Login);
    printf("Password      : %s",User->password);
    printf("Age           : %d",User->age);
    printf("Country       : %s",User->country);
    printf("Gender        : %s",User->gender);
    printf("Height        : %f",User->height);
    printf("Weight        : %f",User->weight);
    printf("Brith_day     : %d",User->brith_year);
    printf("Email         : %s",User->email);
    printf("Year_of_exp   : %d",User->year_of_experience);
    printf("Children      : %s",User->children ? "Bor\n" : "Yoq\n");
}

int main()
{
    User Users[100];
    int option,index = 0;
    while(option){

        printf("Ma'lumot kiritasizmi? 1 - \"Ha\"; 2 - \"Yoq\";");
        scanf("%d",&option);
        Input_info(&Users[index++]);
    };
    for (int i = 0; i < index; i++){
        show_info(&Users[i]);
    }


}