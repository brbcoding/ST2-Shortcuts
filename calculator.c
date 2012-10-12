#include <stdio.h>
#include <stdlib.h>

int main(void)
{

    char letter;
    float num1, num2;
    printf("What operation do you want to do?\n\t+)Addition\n\t-)Subtraction,\n\t/)Division,\n\t*)Multiplication\n");
    /*get user input*/
    scanf("%c", &letter);
        if(letter != '+' && letter != '-' && letter != '/' && letter != '*' )
    {
        printf("You didn't enter a valid operation.");
    }
    else
    {
    printf("Please enter a number: ");
    scanf("%f", &num1);
    printf("Please enter a second number: ");
    scanf("%f", &num2);

        if(num2 != 0)
        {
            if (letter == '+')
            {
            printf("The sum of %.2f and %.2f is %.2f", num1, num2, num1 + num2);
            }

            else if(letter == '-')
            {
            printf("The difference of %.2f and %.2f is %.2f", num1, num2, num1 - num2);
            }

            else if(letter == '*')
            {
            printf("The quotient of %.2f and %.2f is %.2f", num1, num2, num1 * num2);
            }

            else if(letter == '/')
            {
            printf("The product of %.2f and %.2f is %.2f", num1, num2, num1 / num2);
            }
        }

        else{

        printf("You cannot divide by zero.");

        }
    }
    return 0;
}
