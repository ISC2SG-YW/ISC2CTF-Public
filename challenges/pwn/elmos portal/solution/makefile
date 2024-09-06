X64       := gcc
CFLAGS    := -fno-stack-protector -no-pie
LIBC      := .
TARGET    := vuln
CHECKSEC  := checksec --file=$(TARGET)

all:
	$(X64) -o $(TARGET) *.c $(CFLAGS)

	@$(CHECKSEC)

clean:
	rm -f $(TARGET)
