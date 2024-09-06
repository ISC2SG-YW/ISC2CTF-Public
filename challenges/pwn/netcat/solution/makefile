X64       := /usr/bin/x86_64-linux-gnu-gcc
CFLAGS    := 
TARGET    := vuln
CHECKSEC  := checksec --file=$(TARGET)

all:
	$(X64) -o $(TARGET) *.c $(CFLAGS)

	@$(CHECKSEC)

clean:
	rm -f $(TARGET)