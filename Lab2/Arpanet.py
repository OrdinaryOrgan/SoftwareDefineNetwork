from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import OVSBridge


class Arpanet(Topo):
    def build(self):
        switchOpts = {'cls': OVSBridge, 'stp': 1}
        "Create local hosts"
        HUCLA = self.addHost('UCLA')
        HUTAH = self.addHost('UTAH')
        HUCSB = self.addHost('UCSB')
        HSTFD = self.addHost('STFD')
        # Add Switchs
        SUCLA = self.addSwitch('S1A', **switchOpts)
        SUTAH = self.addSwitch('S2H', **switchOpts)
        SUCSB = self.addSwitch('S3B', **switchOpts)
        SSTFD = self.addSwitch('S4D', **switchOpts)
        # Add Links
        self.addLink(HUCLA, SUCLA)
        self.addLink(HUTAH, SUTAH)
        self.addLink(HUCSB, SUCSB)
        self.addLink(HSTFD, SSTFD)
        self.addLink(SUCLA, SUTAH)
        self.addLink(SUCLA, SUCSB)
        self.addLink(SUCLA, SSTFD)
        self.addLink(SUTAH, SUCSB)
        self.addLink(SUTAH, SSTFD)
        self.addLink(SUCSB, SSTFD)


def run():
    topo = Arpanet()
    net = Mininet(topo)
    net.start()
    net.waitConnected()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
