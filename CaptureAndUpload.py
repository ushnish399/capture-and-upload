import cv2
import dropbox
import time
import random
startTime=time.time()

def TakesSnapshot():
    number=random.randint(0, 100)
    video_capture_object=cv2.VideoCapture(0)
    result=True
    while(result):
        ret, frame=video_capture_object.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName, frame)
        startTime=time.time()
        result=False
    return imageName
    print("Snapshot taken")
    
    video_capture_object.release()
    cv2.destroyAllWindows()

def uploadFiles(imageName):
    access_token='MWSgSBpSkj4AAAAAAAAAAUmpIYcnD3zswduek7oTgzIi_vyhF3aEDWaV6h2agEsy'
    file=imageName
    file_to="/testFolder/"+imageName
    dbx=dropbox.Dropbox(access_token)
    with open(file, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
    
def main():
    while(True):
        if((time.time()-startTime)>100):
            name=TakesSnapshot()
            uploadFiles(name)

main()
        

