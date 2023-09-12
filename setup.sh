clear
echo "<═════>Created By 00xJ4CK<══════>"
apt-get update -y
apt-get upgrade -y
apt-get install python3 -y
apt-get install wget -y
apt-get install termux-tools -y
apt-get install proot -y
apt-get install proot-distro -y
rm -rf /data/data/com.termux/files/T-LINUX
mkdir /data/data/com.termux/files/T-LINUX
mv img linuxx.py /data/data/com.termux/files/T-LINUX
touch T-LINUX
echo 'python3 /data/data/com.termux/files/T-LINUX/T-LINUX.py' > T-LINUX
chmod +x T-LINUX
mv linuxx /data/data/com.termux/files/usr/bin
echo
echo
echo "[*] Setup is completed now you can launch this tool by typing 'T-LINUX' in your termux"
rm -rf *
echo
echo
cd
