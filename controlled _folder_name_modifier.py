import os
import numpy as np
parent_dir = "**********"  # enter the specific path of folder
contents = os.listdir(parent_dir)
print(contents)
n_array = np.array(contents)
length=len(n_array)
while 1:
#for i in range(1,length):
    sel = int(input("enter the selection number from the array list: "))
    print(n_array[sel])
    source = n_array[sel]
    dest = input("enter the new date to be modified: ")
    os.chdir(parent_dir)
    os.rename(source, dest)
    print("true")
    path = parent_dir + dest
    os.chdir(path) 
    print("Source path renamed to destination path successfully.") 
    def main(): 

            for count, filename in enumerate(os.listdir()): 
                    dst =dest + "_" + str(count) + ".jpg"
                    src = filename 
                    os.rename(src, dst) 
    if __name__ == '__main__': 
            main() 
