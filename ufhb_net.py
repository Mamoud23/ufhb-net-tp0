#!/usr/bin/env python3
"""UFHB-Net, version 0 : topologie du campus pour le projet fil rouge."""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info

class UFHBNet(Topo):
    def build(self):
        of13 = dict(protocols='OpenFlow13')
        coeur = self.addSwitch('s1', **of13)
        
        # Trois zones du campus : commutateur -> (prefixe des hôtes, base IP)
        zones = {'s2': ('adm', 10), 's3': ('ufr', 20), 's4': ('cit', 30)}
        for nom_sw, (prefixe, base) in zones.items():
            sw = self.addSwitch(nom_sw, **of13)
            self.addLink(sw, coeur, bw=100, delay='1ms')
            
            # AJOUT DE cit3, adm3 et ufr3 : on passe de (1, 2) à (1, 2, 3)
            for i in (1, 2, 3):
                h = self.addHost(f'{prefixe}{i}', ip=f'10.0.0.{base + i}/24')
                self.addLink(h, sw, bw=10)
                
        # Centre de données
        dc = self.addSwitch('s5', **of13)
        self.addLink(dc, coeur, bw=1000)
        for i in (1, 2):
            web = self.addHost(f'web{i}', ip=f'10.0.0.{100 + i}/24')
            self.addLink(web, dc, bw=100)

def lancer():
    net = Mininet(topo=UFHBNet(), switch=OVSKernelSwitch, link=TCLink,
                  controller=None, autoSetMacs=True)
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)
    net.start()
    info('*** Test de connectivité\n')
    net.pingAll()
    CLI(net)
    net.stop()

# Permet aussi : sudo mn --custom ufhb_net.py --topo ufhbnet ...
topos = {'ufhbnet': (lambda: UFHBNet())}

if __name__ == '__main__':
    setLogLevel('info')
    lancer()
