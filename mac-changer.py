import subprocess
import random
import argparse

# Rastgele MAC adresi oluşturmak için kullanılan fonksiyon
def generate_random_mac():
    mac = [random.choice("0123456789ABCDEF") for _ in range(6)]
    return ":".join(mac)

# Yeni MAC adresini ayarlamak için kullanılan fonksiyon
def change_mac(interface, new_mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print(f"MAC adresi değiştirildi: {new_mac}")

# Komut satırı argümanlarını ayrıştırma
parser = argparse.ArgumentParser(description="Linux üzerinde MAC adresini değiştirme programı")
parser.add_argument("-i", "--interface", dest="interface", help="MAC adresini değiştirecek ağ arayüzünü belirtin")
parser.add_argument("-m", "--mac", dest="new_mac", help="Yeni MAC adresini belirtin")
parser.add_argument("-r", "--random", action="store_true", dest="random_mac", help="Rastgele bir MAC adresi oluşturun")
args = parser.parse_args()

# Kullanıcı girdisi veya rastgele MAC adresiyle işlem yapma
if args.interface:
    if args.random_mac:
        new_mac = generate_random_mac()
        change_mac(args.interface, new_mac)
    elif args.new_mac:
        change_mac(args.interface, args.new_mac)
    else:
        print("Yeni MAC adresini belirtin veya rastgele bir MAC adresi oluşturmak için --random seçeneğini kullanın.")
else:
    print("Ağ arayüzünü belirtin. Detaylar için --help seçeneğini kullanın.")
