import paramiko
import time
import datetime
def format_railway_time(time):
    hours = time.strftime("%H")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    return f"{hours}:{minutes}:{seconds}"

current_time = datetime.datetime.now()
railway_time = format_railway_time(current_time)

x = str(current_time + datetime.timedelta(seconds=60))
a= x.split(':')
#print(a)
temp=a[0].split(' ')
#print(temp[1],a[1],a[2])
print(temp[1]+':'+a[1])
cmd = 'SCHTASKS /CREATE /SC DAILY /TN "popup" /TR "C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\venv\\Scripts\\popupnew.py" /ST '+ temp[1]+':'+a[1]


print(paramiko.__version__)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='3.215.109.253', username='Administrator',
            password='@WMoC)ouyPRaOQ1gneHN5iLZ?hSD2?mC', port=22, timeout=3)

(stdin, stdout, stderr) = ssh.exec_command('python C:\\Users\\Administrator\\new\\popupvb\\helloworld.py')

# redirecting all the output in cmd_output
# variable
cmd_output = stdout.read()
print(cmd_output)

x = str(current_time + datetime.timedelta(seconds=60))
a= x.split(':')


(stdin, stdout, stderr) = ssh.exec_command(cmd)
#(stdin, stdout, stderr) = ssh.exec_command('SCHTASKS /DELETE /TN "popup"')
'''
time.sleep(40)
ftp_client=ssh.open_sftp()
ftp_client.put('C:\\popupresults\\windowsslave4.txt','C:\\popupresults\\windowsslave4.txt')

ftp_client.close()
'''



time.sleep(20)
stdin.close()
