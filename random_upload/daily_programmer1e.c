#include <stdio.h>

int main()
{
    char name;
    int age;
    char username[50];
    printf("What is your name?");
    scanf("%c", &name);
    getchar();
    printf("How old are you?");
    scanf("%i", &age);
    printf("Enter a username");
    scanf("%c", &username);
    getchar();
    printf("your name is %c, you are %i years old, and your username is %c",name,age,username);
    return 0;
}
