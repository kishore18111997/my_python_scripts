import os
import paramiko

divideddata_folder_path = 'C:\\my-files\\database-extracts\\divideddatas\\'

# Get the list of files in the folder
all_divideddata_files = os.listdir(divideddata_folder_path)

# Count the number of files
num_divideddata_files = len(all_divideddata_files)

# Create an empty list
divideddata_files_list = []

# Iterate over the files
for file_name in all_divideddata_files:
    # Construct the absolute path of each file
    file_path = os.path.join(divideddata_folder_path, file_name)
    # Add the file path to the list
    divideddata_files_list.append(file_path)

print(f"The number of files in the folder is: {num_divideddata_files}")
print(divideddata_files_list)
#print(divideddata_files_list[0])

index= int(0)
for x in range(index,num_divideddata_files):
    #if else condition to copy divided data to relevant slave
        windowsslave4 = paramiko.SSHClient()
        windowsslave4.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        windowsslave4.connect(hostname='43.205.39.50', username='Administrator',
                              password='X94uRX%pmwW!05eW!;GNb(t.@Qq%Kf6E', port=22, timeout=3)

        commandslave_4 = 'dir /B "C:\\smart-watch\\" | find /c /v ""'
        stdin, stdout, stderr = windowsslave4.exec_command(commandslave_4)
        output = stdout.read().decode().strip()
        print(output)
        file_count_slave4 = int(output)
        windowsslave4.close()

        windowsslave3 = paramiko.SSHClient()
        windowsslave3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        windowsslave3.connect(hostname='3.108.130.28', username='Administrator',
                              password='kxP(R&IVI;JZ&v0frDm.!yT$QxWrhq(k', port=22, timeout=3)
        command2 = 'dir /B "C:\\smart-watch\\" | find /c /v ""'
        stdin, stdout, stderr = windowsslave3.exec_command(command2)
        output = stdout.read().decode().strip()
        print(output)
        file_count_slave3 = int(output)
        windowsslave3.close()

        windowsslave2 = paramiko.SSHClient()
        windowsslave2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        windowsslave2.connect(hostname='52.66.35.139', username='Administrator',
                              password='5p%sHRTuyNgvRTc)QGICpi04t.-;nNO;', port=22, timeout=3)
        commandslave_2 = 'dir /B "C:\\smart-watch\\" | find /c /v ""'
        stdin, stdout, stderr = windowsslave2.exec_command(commandslave_2)
        output = stdout.read().decode().strip()
        print(output)
        file_count_slave2 = int(output)
        windowsslave2.close()


        windowsslave_4result = open('C:\\popupresults\\windowsslave4.txt', 'r')
        slave4_result = int(windowsslave_4result.readline())

        windowsslave_3result = open('C:\\popupresults\\windowsslave3.txt', 'r')
        slave3_result = int(windowsslave_3result.readline())

        windowsslave_2result = open('C:\\popupresults\\windowsslave2.txt', 'r')
        slave2_result = int(windowsslave_2result.readline())

        if slave4_result ==1 and file_count_slave4 ==0:

            windowsslave4 = paramiko.SSHClient()
            windowsslave4.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            windowsslave4.connect(hostname='43.205.39.50', username='Administrator',
                                  password='X94uRX%pmwW!05eW!;GNb(t.@Qq%Kf6E', port=22, timeout=3)

            ftp_client4 = windowsslave4.open_sftp()
            ftp_client4.put(divideddata_files_list[x], 'C:\\smart-watch\\divideddata.txt')
            ftp_client4.close()
            print('File successfully copied to windowsslave4')


        elif slave3_result ==1 and file_count_slave3 ==0:

            windowsslave3 = paramiko.SSHClient()
            windowsslave3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            windowsslave3.connect(hostname='3.108.130.28', username='Administrator',
                                  password='kxP(R&IVI;JZ&v0frDm.!yT$QxWrhq(k', port=22, timeout=3)

            ftp_client3 = windowsslave3.open_sftp()
            ftp_client3.put(divideddata_files_list[x], 'C:\\smart-watch\\divideddata.txt')
            ftp_client3.close()
            print('File successfully copied to windowsslave3')


        elif slave2_result ==1 and file_count_slave2 ==0:

            windowsslave2 = paramiko.SSHClient()
            windowsslave2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            windowsslave2.connect(hostname='52.66.35.139', username='Administrator',
                                  password='5p%sHRTuyNgvRTc)QGICpi04t.-;nNO;', port=22, timeout=3)

            ftp_client2 = windowsslave2.open_sftp()
            ftp_client2.put(divideddata_files_list[x], 'C:\\smart-watch\\divideddata.txt')
            ftp_client2.close()
            print('File successfully copied to windowsslave2')
        else:
            exit()

print('hello world')



