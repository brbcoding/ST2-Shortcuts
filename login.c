#include <stdio.h>
#include <string.h>

int main()
{
    char username[25];
    char password[25];
    char usercorrect[] = {"cody"};
    char passcorrect[] = {"1234"};
    printf("Please enter your username: ");
    scanf( "%s", &username );
    getchar();
    printf("Please enter your password: ");
    scanf( "%s", &password );
    getchar();
    if(strcmp(username,usercorrect) == 0 && strcmp(password,passcorrect) == 0){
        printf("You have successfully logged in, %s\n", username);
    }
    else{
        printf("Wrong username and password.");
    }
    return 0;
}
