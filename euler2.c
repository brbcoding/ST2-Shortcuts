#include <stdio.h>

int main(){
    int f1 = 0, f2 = 1, i = 2, total = 0, fn;
    for(i; i <= 400000; i++){
        if(fn >= 4000000){
            break;
        }
        else{
        fn = f1 + f2;
        f1 = f2;
        f2 = fn;
        if(f1 % 2 == 0){
            total += f1;
            }
        }
    }
    printf("%i",total);
    return 0;
}
