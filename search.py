import os

string1 = 'button'
string2 = 'Button'
string3 = 'btn'
string4 = 'view'
  
rootdir = 'ardupilot'
 
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        # opening a text file
        file1 = open(filepath, "r")
        
        # read file content
        readfile = file1.read()
        
        # checking condition for string found or not
        if string1 in readfile or string2 in readfile or string3 in readfile: 
          if string4 in readfile: 
            print(filepath)
        
        # closing a file
        file1.close() 