import subprocess

'''
Subprocess is a task of running or executing other programs in Python by creating a new process.

'''
# --------------------------------------------------------------------------
# call() used to run an external command without disturbing it
# shell is a boolean value, if it is true then program executes in new shell

# subprocess.call(['ls','-l'], shell=True)

# --------------------------------------------------------------------------

# run() is similar to call() function. It runs the input commands
# and waits till all the commands are completed

# subprocess.run(['ls','-l'], shell=True)

# subprocess.run(['ls','-l'], capture_output=True)

# subprocess.run(['cmd'], shell=True,check=True)

# result = subprocess.run(['python','system_sys.py'], capture_output=True, text=True)

# print(result.stdout)



# --------------------------------------------------------------------------


# check_call() , This function runs the command(s) with the given arguments and waits for it to complete. 
# Then it takes the return value of the code. If it is zero, it returns. 
# Or else it raises CalledProcessError.

# subprocess.check_call('ls',shell=True)


# --------------------------------------------------------------------------


"""
This function is similar to the check_call() function. It runs the command(s) with the given arguments, 
waits for it to complete, and takes the return value of the code. If it is zero, it returns the output as a byte string. 
Or else it raises CalledProcessError.
"""

# subprocess.check_output(["echo","sagar tiwari"], shell=True)


# --------------------------------------------------------------------------

# Popen() in Subprocess Python
"""It is a constructor that creates and handles processes. 
It executes the program in a new process by using the function CreateProcess() in Windows.
buffered zero means unbuffered, if it is 1 then it means line buffered.
"""

# process = subprocess.Popen(['echo','"Hello world"'], stdout=subprocess.PIPE, shell=True)
# out_value = process.communicate()[0]
# print(out_value)



# p = subprocess.Popen(['python','--help'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
# output, errors = p.communicate()
# print(output)
# print(errors)

# process = subprocess.Popen(['echo','"Hello World"'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
# output, error = process.communicate()
# print(output)


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------




