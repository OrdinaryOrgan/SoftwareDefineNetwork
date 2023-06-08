from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import OVSBridge

class FatTree(Topo):
    def build(self):
        switchOpts = {'cls': OVSBridge,'stp': 1}
        "Create custom topo."
        # Add hosts and switches
        # Add hosts in pod1
        Host11 = self.addHost('h11')
        Host12 = self.addHost('h12')
        Host13 = self.addHost('h13')
        Host14 = self.addHost('h14')
        # Add hosts in pod2
        Host21 = self.addHost('h21')
        Host22 = self.addHost('h22')
        Host23 = self.addHost('h23')
        Host24 = self.addHost('h24')
        # Add hosts in pod3
        Host31 = self.addHost('h31')
        Host32 = self.addHost('h32')
        Host33 = self.addHost('h33')
        Host34 = self.addHost('h34')
        # Add hosts in pod4
        Host41 = self.addHost('h41')
        Host42 = self.addHost('h42')
        Host43 = self.addHost('h43')
        Host44 = self.addHost('h44')
        # Add Access Layer Switchs
        AcsSwitch12 = self.addSwitch('AcS12', **switchOpts)
        AcsSwitch21 = self.addSwitch('AcS21', **switchOpts)
        AcsSwitch22 = self.addSwitch('AcS22', **switchOpts)
        AcsSwitch31 = self.addSwitch('AcS31', **switchOpts)
        AcsSwitch11 = self.addSwitch('AcS11', **switchOpts)
        AcsSwitch32 = self.addSwitch('AcS32', **switchOpts)
        AcsSwitch41 = self.addSwitch('AcS41', **switchOpts)
        AcsSwitch42 = self.addSwitch('AcS42', **switchOpts)
        # Add Distribution Layer Switchs
        DstSwitch11 = self.addSwitch('DstS11', **switchOpts)
        DstSwitch12 = self.addSwitch('DstS12', **switchOpts)
        DstSwitch21 = self.addSwitch('DstS21', **switchOpts)
        DstSwitch22 = self.addSwitch('DstS22', **switchOpts)
        DstSwitch31 = self.addSwitch('DstS31', **switchOpts)
        DstSwitch32 = self.addSwitch('DstS32', **switchOpts)
        DstSwitch41 = self.addSwitch('DstS41', **switchOpts)
        DstSwitch42 = self.addSwitch('DstS42', **switchOpts)
        # Add Core Layer Switchs
        CoreSwitch1 = self.addSwitch('CoreS1', **switchOpts)
        CoreSwitch2 = self.addSwitch('CoreS2', **switchOpts)
        CoreSwitch3 = self.addSwitch('CoreS3', **switchOpts)
        CoreSwitch4 = self.addSwitch('CoreS4', **switchOpts)
        # Add links
        # Add links between Core Layer and Distribution Layer
        self.addLink(CoreSwitch1, DstSwitch11)
        self.addLink(CoreSwitch1, DstSwitch21)
        self.addLink(CoreSwitch1, DstSwitch31)
        self.addLink(CoreSwitch1, DstSwitch41)
        self.addLink(CoreSwitch2, DstSwitch11)
        self.addLink(CoreSwitch2, DstSwitch21)
        self.addLink(CoreSwitch2, DstSwitch31)
        self.addLink(CoreSwitch2, DstSwitch41)
        self.addLink(CoreSwitch3, DstSwitch12)
        self.addLink(CoreSwitch3, DstSwitch22)
        self.addLink(CoreSwitch3, DstSwitch32)
        self.addLink(CoreSwitch3, DstSwitch42)
        self.addLink(CoreSwitch4, DstSwitch12)
        self.addLink(CoreSwitch4, DstSwitch22)
        self.addLink(CoreSwitch4, DstSwitch32)
        self.addLink(CoreSwitch4, DstSwitch42)
        # Add links between Distribution Layer and Access Layer
        self.addLink(DstSwitch11, AcsSwitch11)
        self.addLink(DstSwitch11, AcsSwitch12)
        self.addLink(DstSwitch12, AcsSwitch11)
        self.addLink(DstSwitch12, AcsSwitch12)
        self.addLink(DstSwitch21, AcsSwitch21)
        self.addLink(DstSwitch21, AcsSwitch22)
        self.addLink(DstSwitch22, AcsSwitch21)
        self.addLink(DstSwitch22, AcsSwitch22)
        self.addLink(DstSwitch31, AcsSwitch31)
        self.addLink(DstSwitch31, AcsSwitch32)
        self.addLink(DstSwitch32, AcsSwitch31)
        self.addLink(DstSwitch32, AcsSwitch32)
        self.addLink(DstSwitch41, AcsSwitch41)
        self.addLink(DstSwitch41, AcsSwitch42)
        self.addLink(DstSwitch42, AcsSwitch41)
        self.addLink(DstSwitch42, AcsSwitch42)
        # Add links between Access Layer and host
        self.addLink(AcsSwitch11, Host11)
        self.addLink(AcsSwitch11, Host12)
        self.addLink(AcsSwitch12, Host13)
        self.addLink(AcsSwitch12, Host14)
        self.addLink(AcsSwitch21, Host21)
        self.addLink(AcsSwitch21, Host22)
        self.addLink(AcsSwitch22, Host23)
        self.addLink(AcsSwitch22, Host24)
        self.addLink(AcsSwitch31, Host31)
        self.addLink(AcsSwitch31, Host32)
        self.addLink(AcsSwitch32, Host33)
        self.addLink(AcsSwitch32, Host34)
        self.addLink(AcsSwitch41, Host41)
        self.addLink(AcsSwitch41, Host42)
        self.addLink(AcsSwitch42, Host43)
        self.addLink(AcsSwitch42, Host44)


def run():
    topo = FatTree()
    net = Mininet(topo)
    net.start()
    net.waitConnected()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
