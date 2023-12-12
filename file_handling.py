import os
'''
Python IOError Exception. IOError exception is raised when an input or output operation is taking place, 
there can be many reasons for this.
'''

def create_file(filename):
    try:
        with open(filename,'w') as f:
            f.write('Hello world\n')
        print(f'File {filename} created successfully')
    except IOError:
        print('Error: could not create file ' + filename)




def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except IOError:
        print('Error: could not read file' + filename)



def append_file(filename, text):
    try:
        with open(filename,'a') as f:
            f.write(text)
        print(f'Text appended to file  {filename} Successfully')
    except IOError:
        print('Error: could not append file {filename}')



def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print(f'File {filename} renamed to {new_filename}')
    except IOError:
        print(f'Error: could not rename file {filename}')



def delete_file(filename):
    try:
        os.remove(filename)
        print(f'File {filename} deleted successfully')
    except IOError:
        print('Error: could not delete file {filename}')



if __name__ == '__main__':
    filename = input("enter filename: ")
    new_filename = input('Rename filename: ')
    create_file(filename)
    read_file(filename)
    append_file(filename, 'sagar tiwari append')
    read_file(filename)
    rename_file(filename, new_filename)
    delete_file(filename)

