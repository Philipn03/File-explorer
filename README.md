# File-explorer

User input for this program will take the following format:
[COMMAND] [INPUT] [[-]OPTION] [INPUT]

Program Features:
L - List the contents of the user specified directory.

Q - Quit the program.

Example: L c:\users\mark\a1

-r Output directory content recursively.

-f Output only files, excluding directories in the results.

-s Output only files that match a given file name.

-e Output only files that match a give file extension.

Example: L c:\users\mark\a1 -r
         L c:\users\mark\a1 -f
         L c:\users\mark\a1 -r -f
         L c:\users\mark\a1 -s readme.txt
         L c:\users\mark\a1\assets -e jpg
         
------------------------------------------------------------------------------------------------------------------------

Three additional commands to your program:
C - Create a new file in the specified directory.
D - Delete the file.
R - Read the contents of a file.

Example:
C c:\users\mark\a1 -n mark
D c:\users\mark\a1\mark.dsu
R c:\users\mark\a1\mark.dsu
