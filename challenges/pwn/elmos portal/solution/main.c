#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

void ignore_me() {
    setbuf( stdin, 0 );
    setbuf( stdout, 0 );
}

void admin() {
    char * argv[] = { "/bin/sh", NULL };
    execve( "/bin/sh", argv, NULL );
}

int main() {
    ignore_me();

    char username[64];
    char password[64];

    printf( "~~ LOGIN PORTAL ~~\n" );

    printf( "username: " );
    gets( username );

    printf( "logging in as %s...\n", username );
    sleep( 2 );

    printf( "password: " );
    gets( password );

    /*
        TODO: Implement the login logic, for some reason ChatGPT is refusing to write the remaining code for me.
        Something about the code being vulnerable, weird.

        ref: https://stackoverflow.com/questions/1694036/why-is-the-gets-function-so-dangerous-that-it-should-not-be-used
    */

    return 0;
}