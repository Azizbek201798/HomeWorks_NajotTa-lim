#include <stdio.h>
#include <stdbool.h>
#include <string.h>
typedef struct  key
{
	int size;
	bool avto;
	char metall_type[20];
	int price;	
} key;

void show_info(key kalit)
{
	printf("Size:         %d\n",kalit.size);
	printf("Key  type:    %s\n",kalit.avto ? "Auto" : "Manual");
	printf("Metall:       %s\n",kalit.metall_type);
	printf("Price:        %d\n",kalit.price);
}

void  input_info(key *kalit)
{
	printf("Kalit o'lchamini kiriting: ");
	scanf("%d",&kalit->size);
	printf("Kalit auto (1 : \"ha\" 0 : \"Yo'q\") >>> ");
	scanf("%d",&kalit->avto);
	printf("Metall turi: ");
	scanf(" %s",kalit->metall_type);
	printf("Price: ");
	scanf("%d",&kalit->price);
}

void show_keys(key kalit[],int n)
{
	for (int i = 0 ; i < n ; i ++)
	{
		show_info(kalit[i]);
		printf("\n********************************************\n");
	}
}

int main()
{
	system("clear");
	key  kalitlar[100],temp;
	int  op = 1,index = 0;
	while (op)
	{
		system("clear");
		input_info(&kalitlar[index]);
		index++;
		printf("Yana ma'lumot qo'shasizmi\n 1: 'Yes' 0  : 'No'  >>> ");
		scanf("%d",&op);
	}
	system("clear");
	int  select,razmer,narx,avto;
	char type[20];
	bool check;
	printf("1. Size bo'yicha qidirish\n");
	printf("2. Price bo'yicha saralash\n");
	printf("3. Price bo'yicha qidirish\n");
	printf("4. Avto yoki manual \n");
	printf("5. Metall turi bo'yicha qidirish\n");
	printf("Yuqoridagilardna birini tanlang: ");
	scanf("%d",&select);
	switch(select)
	{
		case 1:
		check = false;
		printf("Siz izlayotgan o'lchamni kiriting: ");
		scanf("%d",&razmer);
		for (int i = 0 ; i < index; i ++)
		{
			if (kalitlar[i].size == razmer)
			{
				check = true;
				show_info(kalitlar[i]);
			}
		}
		if (check == false)
			printf("Siz qidirgan '%d' - o'lchamli key mavjud emas\n",razmer);
		break;
		case 2 :
			for (int i = 0 ; i < index - 1; i ++)
			{
				for (int j = i + 1; j < index; j ++)
				{
					if (kalitlar[i].price  > kalitlar[j].price)
					{
						       temp = kalitlar[i];
						kalitlar[i] = kalitlar[j];
						kalitlar[j] = temp;
					}  
				}
			}
			show_keys(kalitlar,index);
		case 3: // price boyicha qidirish:
		check = false;
		printf("Siz qidirayotgan narxni kiriting : ");
		scanf("%d",&narx);
		system("clear");
		for (int i = 0; i < index; i++)
		{
			if (kalitlar[i].price == narx){
				check = true;
				show_info(kalitlar[i]);
				printf("*************************\n");
			} 
		}
		puts("");
		if (check == false)
			printf("Siz qidirayorgan narx mavjud EMAS!\n");
		case 4: // Auto or Manual;
		check = false;
		printf("Kalit avto yoki ruchnoyligini belgilang : "); 
		scanf("%d",&avto);
		for (int i = 0; i < index; i++)
		{
			if (kalitlar[i].avto == avto)
			{
				check = true;
				show_info(kalitlar[i]);
				printf("**************************\n");				
			}
		}	
		puts("");
			if (check == false){
				printf("Siz qidirayorgan avto mavjud EMAS!\n");
		}
		case 5: // Metall turi bo'yicha qidirish;
		check = false;
		printf("Qidirmoqchi bo'lgan metal turini kiriting : ");
		scanf("%s",type);
		for (int i = 0; i < index; i++)
		{
			if (!strcmp(kalitlar[i].metall_type,type))
			{
				check = true;
				show_info(kalitlar[i]);
				printf("************************\n");
			}
		}
		if (check == false)
		{
			printf("Bunday turdagi kalit mavjud EMAS!\n");
		}
	}
	return 0;
}
