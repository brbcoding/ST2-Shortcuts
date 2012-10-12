#include <stdio.h>

/*count characters in input */

main(){
    double nc;
    nc = 0;
    for(nc = 0; getchar() != EOF; ++nc);
        printf("%1.0d\n", nc);
}
