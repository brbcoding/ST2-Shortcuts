#include <stdio.h>

/*This uses functions to multiply and divide*/
int multiply (int x, int y);
int divide (int x, int y);

int main()
{
    int x;
    int y;
    char o;
    printf( "x or /");
    scanf( "%c", &o );
    printf( "Please input two numbers: ");
    scanf( "%d", &x );
    scanf( "%d", &y );
    if(o == "x"){
    printf( "The product of your two numbers is %d\n", multiply( x , y ));
    }
    else{
    printf( "The quotient of your two numbers is %d\n", divide( x , y));
    }
    getchar();
    return 0;
}
int multiply (int x, int y)
{
    return x * y;
}
int divide (int x, int y)
{
    return x / y;

}
