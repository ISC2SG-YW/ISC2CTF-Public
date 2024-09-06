First, open the sheets document and you can see there is a a piece of text at the top
"496e206469676974616c206669656c64732077686572652064617461206c6965732c0d0a5365637265742070616765732062656e6561746820636c65617220736b6965732e0d0a43656c6c7320656e7477696e652c206d7973746572696573206665656c2c0d0a4c6179657273206f66207365637265747320746865792072657665616c2e" translates to 
In digital fields where data lies,
Secret pages beneath clear skies.
Cells entwine, mysteries feel,
Layers of secrets they reveal.
This tells you that theres a secret inside the document, so we can check hidden sheets and sure enough there is a hidden sheet with some index and bytes.
There is some hidden text also in the first cell which translates to
Lurking shadows, secrets play,
Stealthy whispers on display.
BITS aligned, LEAST in SIGht,
Gleams of secrets, veiled in light.
this shows that its least significant bits
if we sort the index and bytes and extract the right most bit and concatenate all of it, it should come out to something like this
By taking the next 2 columns and using the formulas
=RIGHT(C4,1)
and 
=CONCATENATE(D4:D)
we can get the binary string
`010010010101001101000011001100100100001101010100010001100111101101011001001100000111010101011111011000010110110000110001011001110110111000110011011001000101111101110100011010000011001101011111011000100011000101110100011100110010000101111101`
which once decoded gives us our flag