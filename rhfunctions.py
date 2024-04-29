def open_file(filepath="todos.txt"):
    ''' Used to open file which stores our items '''
    with open(filepath, 'r') as file:
        return file.readlines()

def append_file(x):
    ''' Used to append items to our existing list '''
    with open('todos.txt', 'a') as file:
        file.writelines(x)

def write_file(x):
    with open('todos.txt', 'w') as file:
        file.writelines(x)

#print(__name__)
if __name__ == "__main__":
    print("Hello...you called this directly")
    print(open_file())