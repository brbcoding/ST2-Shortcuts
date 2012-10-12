#include <stdio.h>

int main(int argc, char *argv[])
{
    int bugs = 100;
    double bug_rate = 1.2;
    double expected_bugs = bugs * bug_rate;
    printf("You have %d bugs at the rate of %d bugs.\n", bugs, bug_rate);
    printf("You are expected to have %f bugs.\n",expected_bugs);

}
