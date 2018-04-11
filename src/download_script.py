import urllib.request
import os
import datetime

def main():
    csv_path = \
        '/mount_point/home/ubuntu/.kaggle/competitions/landmark-recognition-challenge/data/test.csv'
    dest = \
        '/mount_point/home/ubuntu/.kaggle/competitions/landmark-recognition-challenge/data/images/test'
    log = \
        '/mount_point/home/ubuntu/.kaggle/competitions/landmark-recognition-challenge/data/download_test_log.csv'

    counter = 0
    no_counter = 0
    with open(csv_path, 'r') as csv:
        with open(log, 'w') as log:
            line = csv.readline()  # skip header
            log.write("Script ran on - {}\n\n".format(str(datetime.datetime.now())))
            log.write("{},{},{}\n".format(line[:-1],'download','path'))
            while line:
                entry = line[:-1].split(',')
                id_str = entry[0][1:-1]
                image_link = entry[1][1:-1]
                #landmark_id = entry[2] 
                #print("downloading id:{}\nlink:{}".format(id_str,image_link))
                
                try:
                    out_dest = os.path.join(dest,id_str+'.jpg')
                    if not os.path.isfile(out_dest):  # skip existing files
                        urllib.request.urlretrieve(image_link, out_dest)
                    log.write("{},{},{}\n".format(line[:-1],'Y',out_dest))
                except:
                    no_counter +=1
                    log.write("{},{}\n".format(line[:-1],'N'))
                counter += 1
                if counter % 1000 == 0:
                    print(counter)
                line = csv.readline()
            print("COMPLETED\nTOTAL FILES:{}\nFAILED FILES:{}".format(counter,no_counter))
			
if __name__ == "__main__":
    main()
