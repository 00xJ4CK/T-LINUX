import os
import time

ban = """ 
\033[1;91m<\033[1;97m═════\033[1;91m>\033[1;91mCreated By 00xJ4CK\033[1;91m<\033[1;97m══════\033[1;91m>"""

soc = """\033[1;91m[*] \033[1;97mSelect any options

\033[1;97m[00] \033[1;91mQuit

\033[1;97m[\033[1;91m??\033[1;97m] \033[1;T-LINUX>> \033[1;97m"""

list = """
\033[1;97m[##]\033[1;91m Select any options

\033[1;91m[01]\033[1;97m Kali Nethunter
\033[1;91m[02]\033[1;97m Ubuntu
\033[1;91m[03]\033[1;97m Parrot OS
\033[1;91m[04]\033[1;97m Void Linux
\033[1;91m[05]\033[1;97m Alpine
\033[1;91m[06]\033[1;97m ArchLinux
\033[1;91m[07]\033[1;97m Debian
\033[1;91m[08]\033[1;97m Fedora
\033[1;91m[09]\033[1;97m Manjaro Aarch64 \033[1;91m(Only for AArch64)
\033[1;91m[10]\033[1;97m Open SUSE
\033[1;91m[11]\033[1;97m Update
\033[1;91m[00]\033[1;97m Quit

\033[1;91m[\033[1;97m??\033[1;91m]\033[1;97m T-LINUX>> \033[1;91m"""


while True:
    os.system('clear')
    print(ban)
    linx = input(list)

    if linx == '01' or linx == '1':
        print()
        print('\033[1;97m[*]\033[1;91m Downloading Kali Nethunter ...\n')
        print("\033[1;97m[*]\033[1;91m Please be patient, It can take few minutes\033[0m\n")
        os.system("wget https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter")
        os.system("chmod +x kalinethunter")
        os.system("bash kalinethunter")
        print("\n\033[1;97m[*]\033[1;91m Download is completed\n")
        time.sleep(1)
        print("\033[1;97m[*]\033[1;91m Setting up Environment\n")
        time.sleep(2)
        print("\033[1;97m[*]\033[1;91m Installation is completed, Type 'nethunter' to launch Kali Nethunter In Your termux.")
        input('\033[1;94mPress ENTER To Continue')
    
    elif linx == '2' or linx == '02':
        print()
        print("\033[1;97m[*]\033[1;91m Downloading Ubuntu ...\n")
        print("\033[1;97m[*]\033[1;91m Please be patient, It can take few minutes\033[0m\n")
        os.system("proot-distro install ubuntu")
        print("\n\033[1;97m[*]\033[1;91m Download is completed\n")
        print("\033[1;97m[*]\033[1;91m Setting up Environment")
        time.sleep(2)
        os.system("touch ubuntu")
        os.system("echo 'proot-distro login ubuntu' > ubuntu")
        os.system("chmod +x ubuntu")
        os.system("mv ubuntu /data/data/com.termux/files/usr/bin")
        print("\n\033[1;97m[*]\033[1;91m Installation is completed Type 'ubuntu' to launch Ubuntu Linux In Your termux.")
        input('\033[1;94mPress ENTER To Continue')
        print()

    elif linx == '3' or linx == '03':
        print()
        print("\033[1;97m[*]\033[1;91m Downloading Parrot OS...\n")
        print("\033[1;97m[*]\033[1;91m Please be patient, It can take few minutes\033[0m\n")
        os.system("wget https://raw.githubusercontent.com/risecid/parrot-in-termux/main/parrot.sh")
        os.system("chmod +x parrot.sh")
        os.system("bash parrot.sh -y")
        print("\n\033[1;97m[*]\033[1;91m Download is completed\n")
        time.sleep(1)
        print("\033[1;97m[*]\033[1;91m Setting up Environment\n")
        time.sleep(2)
        os.system("mkdir /data/data/com.termux/parrot")
        os.system("mv parrot-fs parrot-binds startparrot.sh /data/data/com.termux/files/parrot")
        os.system("touch parrot")
        os.system("echo '/data/data/com.termux/files/parrot/startparrot.sh' > parrot")
        os.system("chmod +x parrot")
        os.system("mv parrot /data/data/com.termux/files/usr/bin")
        print
        print("\033[1;97m[*]\033[1;91m Installation is completed, Type 'parrot' to launch Parrot OS In Your termux.")
        input('\033[1;94mPress ENTER To Continue')

    elif linx == '4' or linx == '04':
        print()
        print("\033[1;97m[*]\033[1;91m Downloading Void Linux ...\n")
        print("\033[1;97m[*]\033[1;91m Please be patient, It can take few minutes\033[0m\n")
        os.system("proot-distro install void")
        print("\n\033[1;97m[*]\033[1;91m Download is completed\n")
        time.sleep(1)
        print("\033[1;97m[*]\033[1;91m Setting up Environment\n")
        time.sleep(2)
        os.system("touch void")
        os.system("echo 'proot-distro login void' > void")
        os.system("chmod +x void")
        os.system("mv void /data/data/com.termux/files/usr/bin")
        print("\033[1;97m[*]\033[1;91m Installation is completed Type 'void' to launch Void Linux In Your termux.")
        input('\033[1;94mPress ENTER To Continue')
        print()
    elif linx == '5' or linx == '05':
        print()
        print("\033[1;97m[*]\033[1;91m Downloading Alpine ...\n")
        print("\033[1;97m[*]\033[1;91m Please be patient, It can take few minutes\033[0m\n")
        os.system("proot-distro install alpine")
        print("\n\033[1;97m[*]\033[1;91m Download is completed\n")
        time.sleep(1)
        print("\033[1;97m[*]\033[1;91m Setting up Environment\n")
        time.sleep(2)
        os.system("touch alpine")
        os.system("echo 'proot-distro login alpine' > alpine")
        os.system("chmod +x alpine")
        os.system("mv alpine /data/data/com.termux/files/usr/bin")
        print()
        print("\033[1;97m[*]\033[1;91m Installation is completed Type 'alpine' to launch Alpine In Your termux.")
        input('\033[1;94mPress ENTER To Continue')
        print()
    elif linx == '6' or linx == '06':
        print()
        print("\033[1;97m[*]\033[1;91m Downloading Arch Linux ...\n")
        print("\033[1;97m[*]\033[1;91m Please be patient, It can take few minutes\033[0m\n")
        os.system("proot-distro install archlinux")
        print("\n\033[1;97m[*]\033[1;91m Download is completed\n")
        time.sleep(1)
        print("\033[1;97m[*]\033[1;91m Setting up Environment\n")
        time.sleep(2)
        os.system("touch archlinux")
        os.system("echo 'proot-distro login archlinux' > arch")
        os.system("chmod +x arch")
        os.system("mv arch /data/data/com.termux/files/usr/bin")
        print()
        print("\033[1;97m[*]\033[1;91m Installation is completed Type 'arch' to launch Arch Linux In Your termux.")
        input('\033[1;94mPress ENTER To Continue')
        print()
    elif linx == '7' or linx == '07':
        print()
        print("\033[1;97m[*]\033[1;91m Downloading Debian ...\n")
        print("\033[1;97m[*]\033[1;91m Please be patient, It can take few minutes\033[0m\n")
        os.system("proot-distro install debian")
        print("\n\033[1;97m[*]\033[1;91m Download is completed\n")
        time.sleep(1)
        print("\033[1;97m[*]\033[1;91m Setting up Environment\n")
        time.sleep(2)
        os.system("touch debian")
        os.system("echo 'proot-distro login debian' > debian")
        os.system("chmod +x debian")
        os.system("mv debian /data/data/com.termux/files/usr/bin")
        print()
        print("\033[1;97m[*]\033[1;91m Installation is completed Type 'debian' to launch Debian In Your termux.")
        input('\033[1;94mPress ENTER To Continue')
        print()
    elif linx == '8' or linx == '08':
        print()
        print("\033[1;97m[*]\033[1;91m Downloading Fedora ...\n")
        print("\033[1;97m[*]\033[1;91m Please be patient, It can take few minutes\033[0m\n")
        os.system("proot-distro install fedora")
        print("\n\033[1;97m[*]\033[1;91m Download is completed\n")
        time.sleep(1)
        print("\033[1;97m[*]\033[1;91m Setting up Environment\n")
        time.sleep(2)
        os.system("touch fedora")
        os.system("echo 'proot-distro login fedora' > fedora")
        os.system("chmod +x fedora")
        os.system("mv fedora /data/data/com.termux/files/usr/bin")
        print()
        print("\033[1;97m[*]\033[1;91m Installation is completed Type 'fedora' to launch Fedora In Your termux.")
        input('\033[1;94mPress ENTER To Continue')
        print()
    elif linx == '9' or linx == '09':
        print()
        print("\033[1;97m[*]\033[1;91m Downloading Manjaro Aarch64 ...\n")
        print("\033[1;97m[*]\033[1;91m Please be patient, It can take few minutes\033[0m\n")
        os.system("proot-distro install manjaro-aarch64")
        print("\n\033[1;97m[*]\033[1;91m Download is completed\n")
        time.sleep(1)
        print("\033[1;97m[*]\033[1;91m Setting up Environment\n")
        time.sleep(2)
        os.system("touch manjaro")
        os.system("echo 'proot-distro login manjaro-aarch64' > manjaro")
        os.system("chmod +x manjaro")
        os.system("mv manjaro /data/data/com.termux/files/usr/bin")
        print()
        print("\033[1;97m[*]\033[1;91m Installation is completed Type 'manjaro' to launch Manjaro Aarch64 In Your termux.")
        input('\033[1;94mPress ENTER To Continue')
        print()

    elif linx == '10':
        print()
        print("\033[1;97m[*]\033[1;91m Downloading Open SUSE ...\n")
        print("\033[1;97m[*]\033[1;91m Please be patient, It can take few minutes\033[0m\n")
        os.system("proot-distro install OpenSUSE")
        print("\n\033[1;97m[*]\033[1;91m Download is completed\n")
        time.sleep(1)
        print("\033[1;97m[*]\033[1;91m Setting up Environment\n")
        time.sleep(2)
        os.system("touch opensuse")
        os.system("echo 'proot-distro login OpenSUSE' > opensuse")
        os.system("chmod +x opensuse")
        os.system("mv opensuse /data/data/com.termux/files/usr/bin")
        print()
        print("\033[1;97m[*]\033[1;91m Installation is completed Type 'opensuse' to launch Open SUSE In Your termux.")
        input('\033[1;94mPress ENTER To Continue')
        print()

    elif linx == '11':
        print()
        print("\033[1;91m[*]\033[1;97m This process can take few minutes, So be patience")
        print()
        print("\033[1;91m[*]\033[1;97m Udating T-LINUX in your Termux\n")
        os.system("git clone https://github.com/00xJ4CK/T-LINUX.git")
        os.system("rm /data/data/com.termux/T-LINUX/T-LINUX.py")
        os.system("chmod +x T-LINUX/*")
        os.system("mv T-LINUX/T-LINUX.py /data/data/com.termux/T-LINUX")
        os.system("rm -rf T-LINUX")
        print()
        print("\033[1;97m[*] \033[1;92mUpdated Successfully")
        print()


    elif linx == '00' or linx == '0':
        print()
        print("\033[1;91m[*]\033[1;97m Thanks for using T-LINUX\n")
        print("\033[1;97m[*]\033[1;91m Quiting....\n")
        time.sleep(1)
        exit()

    else:
        print()
        print("\033[1;91mInvalid Input")
        print()
        
