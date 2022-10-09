import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs, files in os.walk(file_from):

            for filename in files:

                local_path = os.path.join(root,filename)

                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BQZvTkzBJ3UuRnHAtFmKzupHOKI0t4lhGhzhZZ-p_IF7Jz0bySRzbTAMnOeQ2x7ZJqZ5sY8PkGZYsOkLZpL5nBvCkyDl_tWIg4bwrjxtKYRq1BKJsKLgPgsd8JVZ7i5DdmdYAnI'
    transferData = TransferData(access_token)

    file_from = input("C:/Users/vedhe/OneDrive/Desktop/whjpro/demo.txt")
    file_to = input("/demo/demo.txt")
    transferData.upload_file(file_from,file_to)
    print("folder has been moved")

main()
    

