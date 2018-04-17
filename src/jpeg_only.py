import imghdr
import os 


if __name__ == '__main__':
    image_dir = '/mount_point/home/ubuntu/.kaggle/competitions/landmark-recognition-challenge/data/images/test/' 
    dest_dir = '/mount_point/home/ubuntu/.kaggle/competitions/landmark-recognition-challenge/data/images/test_not_jpgs/' 
    print("getting subfolders")
    dirs = [os.path.join(image_dir,dr) for dr in os.listdir(image_dir) if os.path.isdir(os.path.join(image_dir,dr))]
    print("got all dirs")
    x = 0
    i = 0
    files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir,f))]
    for f in files: 
        i+=1
        if i%10000==0:
            print(i)
        f_name = f
        f_path = os.path.join(image_dir,f)
        if imghdr.what(f_path) in ['webp','gif'] or imghdr.what(f_path) is None:
           x+=1
           # print("removing {} file : \n{}".format(imghdr.what(f_path),f_path))
           dst_path = os.path.join(dest_dir,f_name) 
           # print("new_path = {}".format(dst_path))
           os.rename(f_path,dst_path)
print(x)
