Uno script Python per modificare l'indirizzo MAC.

mac_address.py = Questo file chiede all'utente il nome_interfaccia e il nuovo_indirizzo_mac.

mac_address.py = Questo file ha più caratteristiche come argomenti della riga di comando, gestione degli errori e verifica che l'obiettivo sia stato veramente raggiunto. Convalida significa che lo script controlla effettivamente il nuovo indirizzo MAC restituito dal comando 'ifconfig' con l'indirizzo MAC a cui l'utente desiderava passare. 

Impostare
Scarica questo repository ed eseguilo localmente,

python mac_address.py -i nome_interfaccia -m new_mac_address

python mac_address.py --interface nome_interfaccia --mac new_mac_address
dove nome_interfaccia è il nome dell'interfaccia di cui si desidera modificare l'indirizzo MAC e new_mac_address è il nuovo indirizzo MAC che si desidera sostituire al posto di quello vecchio.

Produzione
root@kali:~/Desktop/mac_address# python mac_address.py --help

Usage: mac_address.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interfaccia per cambiare il Mac address
  -m NEW_MAC, --mac=NEW_MAC
                        Nuovo Mac address


Prima di eseguire lo script
Nota: guarda il campo "ether" per l'indirizzo MAC

root@kali:~/Desktop/mac_address/mac_addres# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.5  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::a00:27ff:fe92:e43e  prefixlen 64  scopeid 0x20<link>
        ether A8:F0:2F:12:B7:3W  txqueuelen 1000  (Ethernet)
        RX packets 5909  bytes 6760774 (6.4 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3822  bytes 419090 (409.2 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 28  bytes 1596 (1.5 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 28  bytes 1596 (1.5 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

Output dello script

root@kali:~/Desktop/mac_address/mac_addres# python mac_address.py -i eth0 -m 00:11:22:33:44:55
MAC address corrente = A8:F0:2F:12:B7:3W
[+] Cambio MAC Address per eth0 a 00:11:22:33:44:55
[+] Il MAC address cambiato in 00:11:22:33:44:55
