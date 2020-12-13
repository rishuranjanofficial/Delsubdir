#Delsubdir v0.1

import os
import fnmatch
import shutil


for parent, dirnames, filenames in os.walk('path'):
    for fn in filenames:
        if fn.lower().endswith('.xlsx'):
            os.remove(os.path.join(parent, fn))
        elif fn.lower().endswith('.csv'):
            os.remove(os.path.join(parent, fn)) 
    
    if fnmatch.fnmatch(parent,'pattern'):
        print(parent)
        shutil.rmtree(parent)          
    
    
    if len(os.listdir(parent)) == 0: # Check is empty..
        print(parent)
        shutil.rmtree(parent) # Delete..

            
        
                    

