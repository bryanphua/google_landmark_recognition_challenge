import os
import shutil



train_path = '/mount_point/home/ubuntu/.kaggle/competitions/landmark-recognition-challenge/data/images/train/'
bad_classes = 0 
classes = os.listdir(train_path)

for f in classes:
    num_files = len(os.listdir(os.path.join(train_path,f)))
    if num_files < 100:
       bad_classes+=1
       shutil.rmtree(os.path.join(train_path,f))
print(len(classes))
print(bad_classes)
