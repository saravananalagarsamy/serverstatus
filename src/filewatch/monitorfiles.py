'''
Created on Jul 1, 2019

@author: saravananalagarsamy@yahoo.com
'''

import filecmp
import os
from shutil import copy2
from email.send_email import SendEmail
from subprocess import check_output

class MonitorFiles(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def compare_folders(self,stage_dir_path,config_path,process_name = "chrome"):
        comparison = filecmp.dircmp(stage_dir_path, config_path)
        comparison.report_full_closure()
        self.send_email("Files available in both stage and config dir but contents not same", comparison.diff_files)
        self.copy_missing_files(stage_dir_path, config_path, comparison.left_only)
        self.delete_extra_files(config_path, comparison.right_only)
    
    def copy_missing_files(self,source_path,destination_path,files):
        for filename in files:
            try:
                copy2(os.path.join(source_path, filename), os.path.join(destination_path, filename))
                print("File "+ filename +" Successfully copied to "+destination_path)
            except Exception as e:
                print(e)
            else:
                print("send Email about copied files ")
                self.send_email("Copied missing from stage dir to config dir ", files)
        
    def delete_extra_files(self, directory_path, files):
        for file in files:
            file_path = os.path.join(directory_path, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    print("File "+ file +" Successfully Deleted from "+directory_path)
            except Exception as e:
                print(e)
            else:
                print("send Email about deleted files ")
                self.send_email("Deleted extra files from config dir ", files)    
    
    def find_process_status(self,name):
        process = map(int,check_output(["pidof",name]).split())
        if not process:
            print('%s - No such process' % (name)) 
            self.send_email("No process running with process name  ", name)
        elif 'Not Responding' in process:
            print('%s is Not responding' % (name))
        else:
            print('%s is Running or Unknown' % (name))
        
print(os.getcwd())
test = MonitorFiles()
test.compare_folders("/Users/m509575/Workspace/Python/serverstatus/src/resources/stagedir", "/Users/m509575/Workspace/Python/serverstatus/src/resources/configdir")