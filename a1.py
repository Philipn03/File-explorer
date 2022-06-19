# Philip Nguyen
# philipbn@uci.edu
# 57277528

from pathlib import Path

# command for option '-r'
# prints all files, directories, and subdirectories
def print_subdir(link):
    p1 = Path(link)
    for i in p1.iterdir():
        if i.is_file():
            print(i)
        if i.is_dir():
            print(i)
            print_subdir(p1 / i)

# command for option '-f'
# prints all files in directory
def print_files(link2):
    p2 = Path(link2)
    for i in p2.iterdir():
        if i.is_file():
            print(i)

# command for '-r -f'
# prints all files in directory and subdirectories
def recur_r_and_f(link):
    p1 = Path(link)
    for i in p1.iterdir():
        if i.is_file():
            print(i)
        if i.is_dir():
            recur_r_and_f(p1 / i)

# command for '-r -s'
# searches for the input file and prints it out (including files in subdirectories)
def recur_r_and_s(link, word):
    p1 = Path(link)
    for i in p1.iterdir():
        if i.is_file() and i.name == word:
            print(i)
        if i.is_dir():
            recur_r_and_s(p1 / i, word)

# command for '-r -e'
# searches for all files with input suffix and prints it out (including files with same suffix in subdirectories)
def recur_r_and_e(link, word):
    p1 = Path(link)
    for i in p1.iterdir():
        if i.is_file() and i.suffix[1:] == word:
            print(i)
        if i.is_dir():
            recur_r_and_e(p1 / i, word)

# User puts in input
# Split input so you have command (L) at index 0 and assign directory to Path (index 1)
x = input()
lst = x.split()
p = Path(lst[1])

# If user inputs Q, make sure program quits 
if lst[0] == 'Q':
    quit()

# If command is not Q, continuing looping through while loop   
while lst[0] != 'Q':

    # Command 'L' prints out contents in directory
    if lst[0] == 'L':
        for obj in p.iterdir():
            if obj.is_file():
                print(obj)
            if obj.is_dir():
                print(obj)
        
        x = input()
        lst = x.split()
        # Splits input depending on what option user chooses (Ex: '-r' or '-r -f')
        if len(lst) == 4 and '-' in lst[3]:
            lst[2] = lst[2] + ' ' + lst[3]  
        if len(lst) == 5:
            lst[2] = lst[2] + ' ' + lst[3]
            
        # Now that we have option that user chooses, option will determine which if statement runs
        while lst[0] != 'Q' and lst[0] == 'L':
            if lst[2] == '-r':
                print_subdir(p)

            elif lst[2] == '-f':
                print_files(p)

            elif lst[2] == '-r -f':
                recur_r_and_f(p)

            elif lst[2] == '-s':
                for i in p.iterdir():
                    if i.name == lst[3]:
                        print(i)
                
            elif lst[2] == '-r -s':
                recur_r_and_s(p, lst[4])

            elif lst[2] == '-e':
                for i in p.iterdir():
                    if i.suffix[1:] == lst[3]:
                        print(i)
            
            elif lst[2] == '-r -e':
                recur_r_and_e(p, lst[4])
            
            # If option invalid, another input is asked
            # If user decides to choose another command then 'L', program will exit while loop
            x = input()
            lst = x.split()
            if len(lst) == 4 and '-' in lst[3]:
                lst[2] = lst[2] + ' ' + lst[3]    
            if len(lst) == 5:
                lst[2] = lst[2] + ' ' + lst[3]

    # An input of just command (one letter) will not work
    # Input has to contain a COMMAND and DIRECTORY
    if len(lst) == 1:
        print('ERROR')
        x = input()
        lst = x.split()

    # Command C creates a new file with extension .dsu. Uses touch() to create file if not exist
    elif lst[0] == 'C':
        file_name_dsu = lst[3] + '.dsu'
        p = Path('.') / lst[1] / file_name_dsu 
        if not p.exists():
            p.touch()
        p = Path(lst[1])
        for i in p.iterdir():
            if i.name == file_name_dsu:
                print(i)
        x = input()
        lst = x.split()
            
    # Command D deletes file with extension .dsu. If file not in .dsu, while loop will continue iterating until .dsu is found
    # Use unlink() to delete file 
    elif lst[0] == 'D':
        path1 = lst[1]
        while path1[-3:] != 'dsu':
            print('ERROR')
            x = input()
            path1 = x[2:]
        p = Path('.') / path1
        if p.exists():
            p.unlink()
            print(path1, 'DELETED')
        x = input()
        lst = x.split()

    # Command R makes sure to print contents of file if in .dsu, else while loop will iterate until .dsu is found 
    elif lst[0] == 'R':
        while lst[1][-3:] != 'dsu':
            print('ERROR')
            x = input()
            lst = x.split()

        p = p / lst[1]

        if p.exists():
            f = p.open()
            c = f.read(1)
            f.close()
            # Makes sure content of file has text
            # While loop will print EMPTY and ask for another input if file empty
            while not c and p.exists():
                print('EMPTY')
                x = input()
                path1 = x[2:]
                p = p / path1
            x = p.open()
            read = x.read()
            print(read, end='')
            x = input()
            lst = x.split()