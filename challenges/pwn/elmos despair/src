#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>

void ignore_me() {
    setbuf( stdin, 0 );
    setbuf( stdout, 0 );
}

__attribute__( ( noreturn ) ) void ignore_me_2() {
    __asm__( "pop %rdi; ret;" );
    __asm__( "pop %rsi; ret;" );
    __asm__( "pop %rdx; ret;" );
    __asm__( "pop %rcx; ret;" );
    __asm__( "pop %r8; ret;" );
    __asm__( "pop %r9; ret;" );
    exit( 0 );
}

const char * credentials[2][2] = {
    { "kermit", "134e6b499a55" },
    { "elmo", "b1b3773a05c0" },
};

void login( const char * username, const char * password ) {
    for ( int i = 0; i < 2; i++ ) {
        if ( strcmp( username, credentials[i][0] ) == 0 && strcmp( password, credentials[i][1] ) == 0 ) {
            if ( strcmp( username, "elmo" ) == 0 ) {
                printf( "Welcome, Elmo!\n" );
                execve( "/bin/sh", NULL, NULL );
            } else {
                printf( "oops, you're not Elmo!\n" );
                exit( 1 );
            }
        }
    }

    printf( "Invalid credentials.\n" );
    exit( 1 );
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
        TODO: Finish implementing the login functionality.
    */

    return 0;
}