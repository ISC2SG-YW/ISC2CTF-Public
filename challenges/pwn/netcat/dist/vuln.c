#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>


char* get_flag() {
    int     fd;
    char *  flag;
    ssize_t read_bytes;

    if ( ( fd = open( "./flag.txt", O_RDONLY ) ) == -1 ) {
        printf( "couldn't open flag.txt file\n" );
        exit( 1 );
    }

    if ( ( flag = (char *)calloc( 0x50, sizeof( char ) ) ) == NULL ) {
        printf( "calloc failed\n" );
        close( fd );
        exit( 1 );
    }

    if ( ( read_bytes = read( fd, flag, 0x50 ) ) == -1 ) {
        printf( "couldn't read flag.txt file\n" );
        free( flag );
        close( fd );
        exit( 1 );
    }

    close( fd );

    return flag;
}

void init_ignore_me() {
    setbuf( stdin, 0 );
    setbuf( stdout, 0 );
}

void main() {
    init_ignore_me();
    int choice;

    printf( "1. Get flag\n" );
    printf( "2. Exit\n" );
    printf( "Enter your choice: " );

    fscanf( stdin, "%d", &choice );

    switch ( choice ) {
        case 1:
            printf( "Flag: %s\n", get_flag() );
            break;
        case 2:
            printf( "Goodbyye\n" );
            exit( 0 );
        default:
            printf( "Invalid choice\n" );
            break;
    }

}