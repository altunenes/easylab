# ==========================================================================================================================================================
                                                                     
                                                              
                                                                    #Enes Altun 05/21/2022
                                              #This script saves all the names of visual stimuli in a folder as a CSV.
                                                           #Change the 19th line to find stim directory
#Since SHINE TOOLBOX ads "SHINEd" in front of all image names I also added a condition to remove this. You can remove the lines 28 to 32 if you want to hold "SHINEd"
      
# ==========================================================================================================================================================


import os
import pandas as pd

path = os.getcwd()
print('Working directory: ' + path)

# write directory
folder_name = r'C:\Users\altunenes\Desktop\shined_all'
folder_name_save = 'anoutputfolder'
path_folder = os.path.join(path, folder_name)
path_folder_save = os.path.join(path, folder_name_save)
list_files = os.listdir(path_folder)

if not os.path.exists(path_folder_save):
    os.makedirs(path_folder_save)
list_files_new = []
for i in list_files:
    if 'SHINEd' in i:
        i = i.replace('SHINEd_', '')
        list_files_new.append(i)
    else:
        list_files_new.append(i)

#save the list as csv
df = pd.DataFrame(list_files_new)
df.to_csv(os.path.join(path_folder_save, 'list_files.csv'), index=False)
print('Saved directory: ' + path_folder_save)
print('Number of the images: ' + str(len(list_files_new)))
