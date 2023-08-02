import pandas as pd
import os

def find_no_of_slaves_available():

    r1 = open('C:\\popupresults\\windowsslave4.txt', 'r')
    r2 = open('C:\\popupresults\\windowsslave3.txt', 'r')
    r3 = open('C:\\popupresults\\windowsslave2.txt', 'r')


    d={}

    d['windowsslave4']=int(r1.read()); d['windowsslave3']=int(r2.read()); d['windowsslave2']=int(r3.read());

    print(d)
    l=[]
    for x in d.items():
        if 1 in x:
            l.append(x[0])
    print(l)
    print(len(l))
    return len(l), l

p, l = find_no_of_slaves_available()
print(p)
print(l)

def input_data(in_data):
    file_testdata =  open("C:\\my-files\\database-extracts\\ECG_PUT_000170.txt","r")
    test_dict = []
    for line in file_testdata:
        test_dict.append(int(line.strip('\n')))
    df = pd.DataFrame.from_dict(test_dict)
    print('Size of dataFrame=', len(df.index))
    desired_number_of_groups,l = find_no_of_slaves_available()
    group_size = int(len(df.index) / (desired_number_of_groups))
    print("group_size=", group_size)
    remainder_size = len(df.index) % group_size
    print("remainder_size=", remainder_size)
    df_split_list = [df.iloc[i:i + group_size] for i in range(0, len(df) - group_size + 1, group_size)]
    print("Number of split_dataframes=", len(df_split_list))
    if remainder_size > 0:
        df_remainder = df.iloc[-remainder_size:len(df.index)]
        df_split_list.append(df_remainder)
    print("Revised Number of split_dataframes=", len(df_split_list))
    print("Splitting complete, verifying counts")
    count_all_rows_after_split = 0
    for index, split_df in enumerate(df_split_list):
        path = in_data + str(index) + ".txt"
        text = open(path, 'w')
        if os.path.exists(path):
            for p in test_dict[index:len(split_df.index)]:
                text.write(str(p)+"\n")
        else:
            pass
        print("split_df:", index, " size=", len(split_df.index))
        count_all_rows_after_split += len(split_df.index)
        print(">>>>>",test_dict[index:len(split_df.index)])
    print(">>>>>>",count_all_rows_after_split)
    if count_all_rows_after_split != len(df.index):
        raise Exception('count_all_rows_after_split = ', count_all_rows_after_split,
                    " but original CSV DataFrame has count =", len(df.index)
                    )

#---------------------
in_data = "C:\\my-files\\database-extracts\\"
input_data(in_data)

