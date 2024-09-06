#include <stdio.h>

int cmp(char* s1, const char* s2) {
	int i = 0;
	while (s2[i]) {
		if (s1[i] != s2[i]) return 0;
		i += 1;
	}
	return 1;
}

void xor(char* s1) {
	const char s2[31] = "\x20\x0c\x22_\x1c\x35\x19\t\x16\x02\x04\x06\x1a\x06\x00\x04\x00\x06\x05\x17\x16\x0c\x01\x36\x01\x15\x25\x0dro";
	for (int i = 0; i < 30; i++) {
		printf("%c", s2[i] ^ s1[i]);
	}
	printf("\n");
}

int main() {
	char s[50] = {0,};
	char c;
	int d;
	printf("Welcome to Reverse Engineering! Let's answer some questions and you'll be right on your way to the flag\n");
	printf("What's your name?\n>> ");
	scanf("%50s", s);
	printf("What's 1+2?\n>> ");
	scanf("%d%c", &d, &c);
	if (d != 3) {
		printf("You might need to get your math checked out. :(");
		return 0;
	}
	printf("Most important question. What's the password?\n>> ");
	scanf("%10s", s);
	if (cmp(s, "i_am_a_reverse_engineering_pro") == 1) {
		printf("Correct!\n");
		xor(s);
	} else {
		printf("You don't seem to have the password :(\n");
	}
}
