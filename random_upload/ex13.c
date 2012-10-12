#include <stdio.h>
int main(int argc, char *argv[])
{

    if(argc != 2)
    {
        printf("ERROR: You need one argument.\n");
        // this is how you abort a program
        return 1;
    }
    int i = 0;
    for (i = 0; argv[1][i] != '\0'; i++)
    {
        char letter = argv[1][i];

        switch(letter) {
            case 'A':
            case 'a':
                printf("%d: 'A'\n", i);
            break;

            case 'E':
            case 'e':
                printf("%d: 'E'\n", i);
            break;

            case 'I':
            case 'i':
                printf("%d: 'I'\n", i);
            break;

            case 'O':
            case 'o':
                printf("%d: 'O'\n", i);
            break;

            case 'u':
            case 'U':
                printf("%d: 'U'\n", i);
            break;

            case 'y':
            case 'Y':
                if(i > 2)
                {
                    printf("%d: 'Y'\n", i);
                }
                break;

            default:
                printf("%d: %c is not a vowel\n", i, letter);

        }
    }

    return 0;
}
