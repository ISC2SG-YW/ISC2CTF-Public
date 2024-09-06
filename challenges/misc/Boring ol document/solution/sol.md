# Solution

If you search for ISC2CTF in the docx file, you can see some clues are in white text hidden in plain sight. If you turn all the words to white and look at the description, you might see a clue, the word `settings`
Since word files are actually zip files, if you unzip the file, and go to the words directory, you can see a settings.xml. There you can see where the accents are, the flag is in there.
Flag: `ISC2CTF{th4t5_a_l0tt4_w0rd5}`