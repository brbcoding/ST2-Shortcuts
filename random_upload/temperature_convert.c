#include <stdio.h>
/*print fahrenheit-celcius table
for fahr = 0, 20, ..., 300 */
main(){
    float fahr, celcius; /*declare all variables BEFORE they are used*/
    float lower, upper, step;
    lower = 0; /*lower limit of the temp scale*/
    upper = 300; /*upper limit*/
    step = 20; /*step size*/
    printf("%3s %5s\n","Fahr","Celc");
    fahr = lower;
    /*this while loops will create a table of fahr -> celcius*/
    while (fahr <= upper){
        celcius = (5.0 / 9.0) * (fahr-32.0);
        printf("%3.0f %6.1f\n",fahr,celcius);
        fahr = fahr + step;
    }
    printf("\n\n");
    printf("%3s %5s\n","Celc","Fahr");
    celcius = lower;
    /*this one will create the opposite... celc -> fahr */
    while (celcius <= upper){
        fahr = celcius * (9.0/5.0 + 32.0);
        printf("%3.0f %6.1f\n",celcius,fahr);
        celcius = celcius + step;
    }
}
