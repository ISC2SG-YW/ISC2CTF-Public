#include <cstdio>
#include <cstdlib>
#include <string.h>


int slen(char* x) {
	int i = 0;
	while (x[i]) i++;
	return i;
}

void swp(char* x, int i, int j) {
	char tmp = x[i];
	x[i] = x[j];
	x[j] = tmp;
}

int main() {
	const char s[33] = "FAfYucHDAeCmRoCKKiuYFHuIuudc**";
	char* c = (char*)calloc(30, sizeof(char));
	char* d = (char*)calloc(30, sizeof(char));
	printf(">> ");
	scanf("%29s", c);
	int clen = slen(c);
	for (int i=0;i<clen;i++) {
		d[i] = c[i];
	}
	for (int i=0;i<clen;i++) {
		for (int j=i+1;j<clen;j+=2) {
			for (int k=i;k<j;k++) {
				swp(c, j, k); 
			}
		}
	}
	memfrob(c, 30);
	for (int i=0; i<30;i++) {
		if (c[i] != s[i]) {
			printf("%s\n", c);
			return 0;
		}
	}
	printf("ISC2CTF{%s}\n", d);
}
