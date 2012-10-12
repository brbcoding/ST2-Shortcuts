#include <stdio.h>
void play()
{
    printf("Play game initiated.\n");
    printf("Loading...");

}
void load()
{
    printf("Loading saved games...\n");
}
void multiplayer()
{
    printf("Loading multiplayer...\n");
}
int main()
{
    int quit = 0;
    while(quit == 0){
    int input;
    printf("1. Play game\n");
    printf("2. Load saved games\n");
    printf("3. Load multiplayer\n");
    printf("4. Exit\n");
    printf("Selection: ");
    scanf("%d", &input);
    switch (input)
    {
        case 1:
            play();
            break;

        case 2:
            load();
            break;

        case 3:
            multiplayer();
            break;

        case 4:
            printf("Quitting game! \n");
            quit = quit + 1;
            break;

        default:
            printf("Bad input, quitting\n");
            quit = quit + 1;
            break;

    }
    getchar();
    return 0;
}
}
