#include <stdio.h>
#include <stdlib.h>

void ignore_init() {
    setbuf( stdin, 0 );
    setbuf( stdout, 0 );
}

int main() {
    ignore_init();
    char muppet[64];
    char message[64];

    printf( "what's your favourite muppet? " );
    gets( muppet );

    if ( strcmp( muppet, "elmo" ) == 0 ) {
        printf( "das right, here's a system(): %p\n", system );
        printf( "leave a message for elmo~: " );

        gets( message );
        printf( "thanks for the message!\n" );
        return 0;
    } else {
        printf( "nope, try again\n" );
    }

    return 1;
}