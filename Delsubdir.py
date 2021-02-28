#Delsubdir v1.0

import os
import fnmatch
import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#######################################################################################
#Directory input Function
#######################################################################################    

def Delsubdir():    
    print("Enter the Directory to Customize")
    folder_with_path=input()
    if os.path.isdir(folder_with_path):
        print(f"{bcolors.OKGREEN}"+f"{bcolors.BOLD}\n"+folder_with_path + f"{bcolors.OKGREEN} is a valid Folder{bcolors.ENDC}")
        print(f"{bcolors.BOLD}")
        choice = input("""
            *****************************MAIN MENU*****************************
            1:  Delete file in directory based on file extension
            2:  Delete sub-directory based on pattern
            3:  Delete the blank sub-directory
            4:  Quit             
            *******************************************************************
            Please enter your choice: """+f"{bcolors.ENDC}")
        
                    
#######################################################################################
# File Deletion based on Extension
#######################################################################################

        if choice == '1':
            try:
                count=0
                print("\nEnter the Extension to delete the file(s)")
                file_extension=input()
                for parent, dirnames, filenames in os.walk(folder_with_path): 
                    for fn in filenames:
                        if fn.lower().endswith(file_extension):
                            os.remove(os.path.join(parent, fn))
                            print("\nThe Deleting File(s) list\n"+fn)
                            count+=1  
                print("\n"+str(count)+" files deleted!")                              
            except:
                print("\nNo File with this Extension. Thank You")
            
#######################################################################################
# Sub-Directory Deletion based on Pattern
#######################################################################################

        elif choice == '2':
            try:
                count=0
                print("\nEnter the Pattern to delete the sub-directory(s)")
                pattern=input()
                for parent, dirnames, filenames in os.walk(folder_with_path): 
                    if fnmatch.fnmatch(parent,pattern):
                        print("\nThe Deleting Sub-Directory(s) list\n"+parent)
                        shutil.rmtree(parent)  
                        count+=1  
                print("\n"+str(count)+" sub-directory(s) deleted!")                              
            except:
                print("\nNo Sub-Directory with this Pattern. Thank You")  
 
#######################################################################################
# Blank Sub-Directory Deletion
#######################################################################################             

        elif choice == '3':
            try:
                count=0
                for parent, dirnames, filenames in os.walk(folder_with_path): 
                    if len(os.listdir(parent)) == 0:
                        print("\nThe Deleting Sub-Directory(s) list\n"+parent)
                        shutil.rmtree(parent)  
                        count+=1  
                print("\n"+str(count)+" blank sub-directory(s) deleted!")                              
            except:
                print("\nNo Blank Sub-Directory. Thank You")		
                  
#######################################################################################
# Exit
#######################################################################################

        elif choice=='4':
            exit()    
        else:
            print("Please select the correct number")
            print("Please try again\n\n")

    else:
        print ("\nDirectory not exists. Try Again!!")  
                  
#######################################################################################
# Main
#######################################################################################

if __name__ == '__main__':
    Delsubdir()
        
                    


