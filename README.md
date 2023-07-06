# Mac Changer

#### Changing with a specific MAC address
`python mac_changer.py -i eth0 -m 00:11:22:33:44:55
`
#### Changing with a random MAC address:
 `python mac_changer.py -i wlan0 --random`

#### Displaying help and usage instructions:
``python mac_changer.py --help``

------------

### **Note:**

**The above program uses sudo to execute the ifconfig command. Therefore, you'll need administrative privileges before running the program. Additionally, the program relies on the ifconfig command being available on your system.
**