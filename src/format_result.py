import pandas as pd

test_path = '/mount_point/home/ubuntu/.kaggle/competitions/landmark-recognition-challenge/data/test.csv'
result_path = '/tmp/result.csv'
df = pd.read_csv(test_path)
ids = df['id'].values

df2 = pd.read_csv(result_path)
result_ids = df2['id'].values

print(df2.head())
f = open('/tmp/formatted_result.csv','w')
f.write('id,landmarks\n')
 #for indx, row in df2.iterrows():
 #   f.write('{},{}\n'.format(row['id'],row['landmarks']))

for idd in ids:
    f.write('{},9633\n'.format(idd))

f.close()
