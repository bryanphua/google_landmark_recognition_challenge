import os
import pandas as pd

if __name__ == "__main__":
    out_dir = "/mount_point/home/ubuntu/.kaggle/competitions/landmark-recognition-challenge/data/images/train"
    log_path = "/mount_point/home/ubuntu/.kaggle/competitions/landmark-recognition-challenge/data/download_train_log.csv"
    
    train_df = pd.read_csv(log_path, skiprows=2)
    train_df = train_df.loc[train_df['download']=='Y']

    # list of landmark_ids
    landmarks = train_df['landmark_id'].values

    # create folders in out_dir for each landmark_id if it does not exist
    print("creating landmark directories...")
    for lm_id in landmarks:
        lm_subfolder_dir = os.path.join(out_dir,str(lm_id))
        if not os.path.exists(lm_subfolder_dir):
            os.makedirs(lm_subfolder_dir)
    print("directories created")

    # move each image into respective subfolder 
    print('moving files...')
    for index,image in train_df.iterrows():
        landmark_id = image['landmark_id']
        original_path = image['path']
        image_id = image['id']
        filename = str(image_id)+'.jpg'
        dest_path = os.path.join(out_dir, str(landmark_id), filename)
#        print('original = {}'.format(original_path))
#        print('dest = {}'.format(dest_path))
        os.rename(original_path,dest_path)
    print('files moved')
