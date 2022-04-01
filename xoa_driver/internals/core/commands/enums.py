from enum import IntEnum
class ReservedStatus(IntEnum):
    """Test resource reservation status"""
    RELEASED = 0
    """Test resource is released."""
    RESERVED_BY_YOU = 1
    """Test resource is reserved by you."""
    RESERVED_BY_OTHER = 2
    """Test resource is reserved by another user."""


class ReservedAction(IntEnum):
    """Reservation actions."""
    RELEASE = 0
    """Release the test resource."""
    RESERVE = 1
    """Reserve the test resource."""
    RELINQUISH = 2
    """Force release other's ownership of the test resource."""


class ChassisShutdownAction(IntEnum):
    """Chassis shutdown actions."""
    RESTART = 1
    """Restart after shutdown."""
    POWEROFF = 2
    """Keep power-off after shutdown."""


class OnOff(IntEnum):
    """On or Off."""
    OFF = 0
    """Off"""
    ON = 1
    """On"""


class RESTControlAction(IntEnum):
    """Controls of Valkyrie REST server."""
    START = 0
    """Start the REST server on the chassis."""
    STOP = 1
    """Stop the REST server on the chassis."""
    RESTART = 2
    """Restart the REST server on the chassis."""


class ServiceStatus(IntEnum):
    """Service status."""
    SERVICE_OFF = 0
    """Service is off."""
    SERVICE_ON = 1
    """Service is on."""


class ChassisSessionType(IntEnum):
    """The type of the session between the client and the chassis."""
    MANAGER = 1
    """Connection on port 22606 running binary command (used by ValkyrieManager & VulcanManager)."""
    SCRIPT = 2
    """Connection on port 22611, running CLI command."""


class TimeSyncMode(IntEnum):
    """Module's time sync mode."""
    CHASSIS = 0
    """Module syncs to chassis's clock."""
    EXTERNAL = 1
    """Module syncs to an external clock."""
    MODULE = 2
    """Module syncs to its own clock."""


class CFPState(IntEnum):
    """Modules' CFP state"""
    NOTCFP = 0
    """This is not a CFP-based test module."""
    NOTPRESENT = 1
    """No transceiver, the CFP cage is empty"""
    NOTFLEXIBLE = 2
    """Transceiver present, supporting a fixed speed and port-count"""
    FLEXIBLE = 3
    """Transceiver present, supporting flexible speed and port-count"""


class CFPType(IntEnum):
    """Type of CFP"""
    CFP_UNKNOWN = 0
    """CFP unknown"""
    CFP_INVALID = 1
    """CFP 100G not supported"""
    CFP_1X40_SR4 = 2
    """CFP 40G SR4 850 nm"""
    CFP_2X40_SR4 = 3
    """CFP 40G SR4 850 nm"""
    CFP_1X40_LR4 = 4
    """CFP 40G LR4 1310 nm"""
    CFP_1X100_LR4 = 5
    """CFP 100G LR4 1310 nm"""
    CFP_1X100_SR10 = 6
    """CFP 100G SR10 850 nm / CFP 40G SR4 850 nm"""
    CFP_4X10_SFPP = 7
    """"""
    QSFP_EMPTY = 8
    """QSFP empty"""
    QSFP_UNKNOWN = 9
    """QSFP unknown"""
    QSFP_SR = 10
    """QSFP SR 850 nm"""
    QSFP_LR = 11
    """QSFP LR 1550 nm"""
    QSFP_ER = 12
    """QSFP ER 1550 nm"""
    CXP_UNKNOWN = 13
    """CXP unknown SR10"""
    CXP_SR10 = 14
    """CXP 100G SR10 850 nm / CXP 40G SR4 850 nm"""
    CXP_AOC = 15
    """CXP 100G SR10 AOC / CXP 40G SR4 AOC"""
    CFP4_UNKNOWN = 16
    """CFP4 unknown"""
    CFP4_1X100_LR4 = 17
    """CFP4 100G LR4"""
    CFP4_1X100_ER4 = 18
    """CFP4 100G ER4"""
    CFP4_1X100_SR4 = 19
    """CFP4 100G SR4"""
    QSFP28_CR4 = 20
    """QSFP28 CR4"""
    QSFP28_SR4 = 21
    """QSFP28 SR4"""
    QSFP28_LR4 = 22
    """QSFP28 LR4"""
    QSFP28_ER4 = 23
    """QSFP28 ER4"""
    QSFP28_AOC = 24
    """QSFP28 AOC"""
    QSFP28_ACC = 25
    """QSFP28 ACC"""
    QSFP28_UNKNOWN = 26
    """QSFP28 unknown"""
    QSFP28P_SR4 = 27
    """QSFP+ SR4 850 nm"""
    QSFP28P_LR4 = 28
    """QSFP+ LR4 1310 nm"""
    QSFP28P_ER4 = 29
    """QSFP+ ER4 1500 nm"""
    QSFP28P_CR4 = 30
    """QSFP+ CR4 Copper"""
    QSFP28P_ISM4 = 31
    """QSFP+ iSM4 1310 nm"""
    QSFP28P_UNKNOWN = 32
    """QSFP+ unknown"""
    TCVR_UNKNOWN = 33
    """Transceiver unknown"""
    QSFP28_CWDM4 = 34
    """QSFP28 CWDM4"""
    QSFP28_CWDM4FEC = 35
    """QSFP28 CWDM4 FEC"""
    QSFP28_PSM4 = 36
    """QSFP28 PSM4"""


class SMAInputFunction(IntEnum):
    """SMA input function"""
    NOTUSED = 0
    """SMA input not used"""
    TX2MHZ = 1
    """TX Clock Ref. 2.048 MHz"""
    TX10MHZ = 2
    """TX Clock Ref. 10.0 MHz"""


class SMAOutputFunction(IntEnum):
    """SMA output function"""
    DISABLED = 0
    """Disabled"""
    PASSTHROUGH = 1
    """Pass-through"""
    P0SOF = 2
    """Port 0 Start-of-Frame Pulse"""
    P1SOF = 3
    """Port 1 Start-of-Frame Pulse"""
    REF2MHZ = 4
    """TX Clock (nom. 2.048 MHz)"""
    REF10MHZ = 5
    """TX Clock (nom. 10.0 MHz)"""
    REF125MHZ = 6
    """TX Clock (nom. 125 MHz)"""
    REF156MHZ = 7
    """TX Clock (nom. 156.25 MHz)"""
    P0RXCLK = 8
    """Port 0 RX Clock (nom. 10.0 MHz)"""
    P1RXCLK = 9
    """Port 1 RX Clock (nom. 10.0 MHz)"""
    P0RXCLK2MHZ = 10
    """Port 0 RX Clock (nom. 2.048 MHz)"""
    P1RXCLK2MHZ = 11
    """Port 1 RX Clock (nom. 2.048 MHz)"""
    TS_PPS = 12
    """Timing Source (Pulse-Per-Second)"""


class SMAStatus(IntEnum):
    """SMA status"""
    OK = 0
    """Status OK"""
    NO_VALID_SIGNAL = 1
    """No valid signal"""


class HasDemo(IntEnum):
    """Demo or not"""
    NON_DEMO = 0
    """Not a demo unit"""
    DEMO = 1
    """Demo unit"""


class IsValid(IntEnum):
    """Whether it is valid"""
    INVALID = 0
    """Invalid"""
    VALID = 1
    """Valid"""


class IsPermanent(IntEnum):
    """Whether it is permanent"""
    NON_PERMANENT = 0
    """Not permanent"""
    PERMANENT = 1
    """Permanent"""


class YesNo(IntEnum):
    NO = 0
    """No"""
    YES = 1
    """Yes"""


class UpdateState(IntEnum):
    """License update state"""
    NONE = 0
    """None"""
    UPDATING = 1
    """Updating"""
    UPDATE_SUCCESS = 2
    """Update successful"""
    UPDATE_FAIL = 3
    """Update failed"""


class IsOnline(IntEnum):
    """Chassis online or not"""
    OFFLINE = 0
    """Chassis offline"""
    ONLINE = 1
    """Chassis online"""


class PortSpeedMode(IntEnum):
    """Port speed mode"""
    AUTO = 0
    """Auto negotiate with peer"""
    F10M = 1
    """Forced to 10 Mbit/s"""
    F100M = 2
    """Forced to 100 Mbit/s"""
    F1G = 3
    """Forced to 1 Gbit/s"""
    F10G = 4
    """Forced to 10 Gbit/s"""
    F40G = 5
    """Forced to 40 Gbit/s"""
    F100G = 6
    """Forced to 100 Gbit/s"""
    F10MHDX = 7
    """Forced to 10 Mbit/s half-duplex"""
    F100MHDX = 8
    """Forced to 100 Mbit/s half-duplex"""
    F10M100M = 9
    """Auto negotiate to 10/100 Mbit/s"""
    F100M1G = 10
    """Auto negotiate to 100 Mbit/s or 1 Gbit/s"""
    F100M1G10G = 11
    """Auto negotiate to 100 Mbit/s or 1 Gbit/s or 10 Gbit/s"""
    F2500M = 12
    """Forced to 2500 Mbit/s"""
    F5G = 13
    """Forced to 5 Gbit/s"""
    F100M1G2500M = 14
    """Auto negotiate to 100 Mbit/s or 1 Gbit/s or 2500 Mbit/s"""
    F25G = 15
    """Forced to 25 Gbit/s"""
    F50G = 16
    """Forced to 50 Gbit/s"""
    F200G = 17
    """Forced to 200 Gbit/s"""
    F400G = 18
    """Forced to 400 Gbit/s"""
    F800G = 19
    """Forced to 800 Gbit/s"""
    F1600G = 20
    """Forced to 1600 Gbit/s"""
    UNKNOWN = 255
    """Speed mode unknown"""


class SyncStatus(IntEnum):
    """Port sync status"""
    NO_SYNC = 0
    """Not sync"""
    IN_SYNC = 1
    """In sync with peer"""


class LoopbackMode(IntEnum):
    """Port loopback mode"""
    NONE = 0
    """Off"""
    L1RX2TX = 1
    """L1 RX-to-TX"""
    L2RX2TX = 2
    """L2 RX-to-TX"""
    L3RX2TX = 3
    """L3 RX-to-TX"""
    TXON2RX = 4
    """TX(on)-to-RX"""
    TXOFF2RX = 5
    """TX(off)-to-RX"""
    PORT2PORT = 6
    """Port-to-Port"""


class TrafficOnOff(IntEnum):
    """Traffic status"""
    OFF = 0
    """Traffic off"""
    ON = 1
    """Traffic on"""
    PREPARING = 2
    """Traffic preparing"""


class StartOrStop(IntEnum):
    STOP = 0
    """Stop the action"""
    START = 1
    """Start the action"""


class LatencyMode(IntEnum):
    """Latency measurement mode"""
    LAST2LAST = 0
    """Last-to-Last"""
    FIRST2LAST = 1
    """First-to-Last"""
    LAST2FIRST = 2
    """Last-to-First"""
    FIRST2FIRST = 3
    """First-to-First"""


class SourceType(IntEnum):
    TXIFG = 0
    """TX IFG"""
    TXLEN = 1
    """TX Length"""
    RXIFG = 2
    """RX IFG"""
    RXLEN = 3
    """RX Length"""
    RXLAT = 4
    """RX Latency"""
    RXJIT = 5
    """RX Jitter"""


class PacketDetailSelection(IntEnum):
    ALL = 0
    """All"""
    TPLD = 1
    """Based on Test Payload ID"""
    FILTER = 2
    """Based on filter"""


class OnOffWithSuppress(IntEnum):
    """Stream status"""
    OFF = 0
    """Off"""
    ON = 1
    """On"""
    SUPPRESS = 2
    """Suppressed"""


class ProtocolOption(IntEnum):
    """Protocol header options"""
    ETHERNET = 1
    """Ethernet II"""
    VLAN = 2
    """VLAN"""
    ARP = 3
    """Address Resolution Protocol"""
    IP = 4
    """IPv4"""
    IPV6 = 5
    """IPv6"""
    UDP = 6
    """User Datagram Protocol (w/o checksum)"""
    TCP = 7
    """Transmission Control Protocol (w/o checksum)"""
    LLC = 8
    """Logic Link Control"""
    SNAP = 9
    """Subnetwork Access Protocol"""
    GTP = 10
    """GPRS Tunnelling Protocol"""
    ICMP = 11
    """Internet Control Message Protocol"""
    RTP = 12
    """Real-time Transport Protocol"""
    RTCP = 13
    """RTP Control Protocol"""
    STP = 14
    """Spanning Tree Protocol"""
    SCTP = 15
    """Stream Control Transmission Protocol"""
    MACCTRL = 16
    """MAC Control"""
    MPLS = 17
    """Multiprotocol Label Switching"""
    PBBTAG = 18
    """Provider Backbone Bridge tag"""
    FCOE = 19
    """Fibre Channel over Ethernet"""
    FC = 20
    """Fibre Channel"""
    FCOETAIL = 21
    """Fibre Channel over Ethernet (tail)"""
    IGMPV3L0 = 22
    """IGMPv3 Membership Query L=0"""
    IGMPV3L1 = 23
    """IGMPv3 Membership Query L=1"""
    UDPCHECK = 24
    """User Datagram Protocol (w/ checksum)"""
    IGMPV2 = 25
    """Internet Group Management Protocol v2"""
    MPLS_TP_OAM = 26
    """MPLS-TP, OAM Header"""
    GRE_NOCHECK = 27
    """Generic Routing Encapsulation (w/o checksum)"""
    GRE_CHECK = 28
    """Generic Routing Encapsulation (w/ checksum)"""
    TCPCHECK = 29
    """Transmission Control Protocol (w/ checksum)"""
    GTPV1L0 = 30
    """GTPv1 (no options), GPRS Tunneling Protocol v1"""
    GTPV1L1 = 31
    """GTPv1 (w/ options), GPRS Tunneling Protocol v1"""
    GTPV2L0 = 32
    """GTPv2 (no options), GPRS Tunneling Protocol v2"""
    GTPV2L1 = 33
    """GTPv2 (w/ options), GPRS Tunneling Protocol v2"""
    IGMPV1 = 34
    """Internet Group Management Protocol v1"""
    PWETHCTRL = 35
    """PW Ethernet Control Word"""
    VXLAN = 36
    """Virtual eXtensible LAN"""
    ETHERNET_8023 = 37
    """Ethernet 802.3"""
    NVGRE = 38
    """Generic Routing Encapsulation (Network Virtualization)"""
    DHCPV4 = 39
    """Dynamic Host Configuration Protocol (IPv4)"""
    GENEVE = 40
    """Generic Network Virtualization Encapsulation"""
    XENA_TPLD = 41
    XENA_TPLD_PI = 42
    XENA_MICROTPLD = 43
    ETHERNET_FCS = 44
    MACCTRLPFC = 45
    """MAC Control for PFC"""
    ECPRI = 46
    """Enhanced Common Public Radio Interface"""
    ROE = 47
    """Radio over Ethernet"""
    ETHERTYPE = 48
    """EtherType"""
    
    # Generat RAW form 1...64 bytes
    _ignore_ = 'ProtocolOption i'
    ProtocolOption = vars()
    for i in range(1, 65):
        ProtocolOption['RAW_%d' % i] = 256 - i # type: ignore

class ModifierAction(IntEnum):
    """Modifier action mode"""
    INC = 0
    """Incrementing"""
    DEC = 1
    """Decrementing"""
    RANDOM = 2
    """Random"""


class LengthType(IntEnum):
    """Packet length type"""
    FIXED = 0
    """Fixed"""
    INCREMENTING = 1
    """Incrementing"""
    BUTTERFLY = 2
    """Butterfly"""
    RANDOM = 3
    """Random"""
    MIX = 4
    """Mix"""


class PayloadType(IntEnum):
    """Packet payload type"""
    PATTERN = 0
    """Pattern"""
    INCREMENTING = 1
    """Incrementing"""
    PRBS = 2
    """PRBS"""
    RANDOM = 3
    """Random"""


class MDIXMode(IntEnum):
    """MDIX mode"""
    AUTO = 0
    """Auto"""
    MDI = 1
    """MDI"""
    MDIX = 2
    """MDIX"""


class LengthCheckType(IntEnum):
    AT_MOST = 0
    """At Most"""
    AT_LEAST = 1
    """At Least"""


class StartTrigger(IntEnum):
    """Capture start trigger"""
    ON = 0
    """From Traffic On"""
    FCSERR = 1
    """From FCS Error"""
    FILTER = 2
    """From Filter"""
    PLDERR = 3
    """From Payload Error"""


class StopTrigger(IntEnum):
    """Capture stop trigger"""
    FULL = 0
    """Until Capture Buffer Full"""
    FCSERR = 1
    """Until Receiving FCS Error"""
    FILTER = 2
    """Until Filter Matched"""
    PLDERR = 3
    """Until Receiving Payload Error"""
    USERSTOP = 4
    """Until User Stops"""


class PacketType(IntEnum):
    """Type of Packet to Keep in Capture Buffer"""
    ALL = 0
    """All Packets"""
    FCSERR = 1
    """With FCS Errors"""
    NOTPLD = 2
    """Without Test Payload"""
    TPLD = 3
    """With Test Payload"""
    FILTER = 4
    """Filtered Packets"""
    PLDERR = 5
    """With Payload Errors"""


class InjectErrorType(IntEnum):
    """Lane Injection Error Type"""
    HEADERERROR = 1
    """Header Error"""
    ALIGNERROR = 2
    """Alignment Error"""
    BIP8ERROR = 3
    """BIP8 Error"""


class HeaderLockStatus(IntEnum):
    """Physical Lane Header Lock Status"""
    HEADEROFF = 0
    """Header Lock Off"""
    HEADERON = 1
    """Header Lock On"""
    HEADEROFFUNSTABLE = 2
    """Header Lock Off and Unstable"""
    HEADERONUNSTABLE = 3
    """Header Lock On but Unstable"""


class AlignLockStatus(IntEnum):
    """Physical Lane Alignment Lock Status"""
    ALIGNOFF = 0
    """Alignment Lock Off"""
    ALIGNON = 1
    """Alignment Lock On"""
    ALIGNUNSTABLE = 3
    """Alignment Lock Unstable"""


class PRBSLockStatus(IntEnum):
    """Physical Lane PRBS Lock Status"""
    PRBSOFF = 0
    """PRBS Lock Off"""
    PRBSON = 1
    """PRBS Lock On"""
    PRBSOFFUNSTABLE = 2
    """PRBS Lock Off and Unstable"""
    PRBSONUNSTABLE = 3
    """PRBS Lock On but Unstable"""


class MulticastOperation(IntEnum):
    """IGMPv2 Request Type"""
    OFF = 0
    """Off"""
    ON = 1
    """On"""
    JOIN = 2
    """Join"""
    LEAVE = 3
    """Leave"""


class MulticastExtOperation(IntEnum):
    """IGMPv2/v3Request Type"""
    OFF = 0
    """Off"""
    ON = 1
    """On"""
    JOIN = 2
    """Join"""
    LEAVE = 3
    """Leave"""
    INCLUDE = 4
    """Include"""
    EXCLUDE = 5
    """EXclude"""
    LEAVE_TO_ALL = 6
    """Leave To All"""
    GENERAL_QUERY = 7
    """General Query"""
    GROUP_QUERY = 8
    """Group Query"""


class IGMPVersion(IntEnum):
    """IGMP Version"""
    IGMPV2 = 0
    """IGMP Version 2"""
    IGMPV3 = 1
    """IGMP Version 3"""


class TXMode(IntEnum):
    """Port TX Mode"""
    NORMAL = 0
    """Normal"""
    STRICTUNIFORM = 1
    """Strict Uniform"""
    SEQUENTIAL = 2
    """Sequential"""
    BURST = 3
    """Burst"""


class PayloadMode(IntEnum):
    """Payload Mode"""
    NORMAL = 0
    """Normal"""
    EXTPL = 1
    """Extend Payload"""
    CDF = 2
    """Custom Data Field"""


class BRRMode(IntEnum):
    """BRR Mode"""
    SLAVE = 0
    """Slave Mode"""
    MASTER = 1
    """Master Mode"""


class TXClockSource(IntEnum):
    """TX Clock Source"""
    MODULELOCALCLOCK = 0
    """Module Local Clock"""
    SMAINPUT = 1
    """SMA Input"""
    P0RXCLK = 2
    """Port 0 RX Clock"""
    P1RXCLK = 3
    """Port 1 RX Clock"""
    P2RXCLK = 4
    """Port 2 RX Clock"""
    P3RXCLK = 5
    """Port 3 RX Clock"""
    P4RXCLK = 6
    """Port 4 RX Clock"""
    P5RXCLK = 7
    """Port 5 RX Clock"""
    P6RXCLK = 8
    """Port 6 RX Clock"""
    P7RXCLK = 9
    """Port 7 RX Clock"""


class TXClockStatus(IntEnum):
    """TX Clock Status"""
    OK = 0
    """Clock OK"""
    NOVALIDTXCLK = 1
    """No Valid TX Clock"""


class LoopBandwidth(IntEnum):
    """Loop Bandwidth"""
    BW103HZ = 1
    """Loop Bandwidth = 103 Hz"""
    BW207HZ = 2
    """Loop Bandwidth = 207 Hz"""
    BW416HZ = 3
    """Loop Bandwidth = 416 Hz"""
    BW1683HZ = 4
    """Loop Bandwidth = 1683 Hz"""
    BW7019HZ = 5
    """Loop Bandwidth = 7019 Hz"""


class MediaType(IntEnum):
    """Module Media Type"""
    CFP4 = 0
    """CFP4"""
    QSFP28 = 1
    """QSFP28"""
    CXP = 2
    """CXP"""
    SFP28 = 3
    """SFP28"""
    QSFP56 = 4
    """QSFP56"""
    QSFP_DD = 5
    """QSFP DD"""
    SFP56 = 6
    """SFP56"""
    SFP_DD = 7
    """SFP DD"""
    QSFP_DD_NRZ = 9
    """QSFP DD (NRZ)"""
    QSFP28_PAM4 = 10
    """QSFP DD (PAM4)"""
    CFP = 99
    """CFP"""
    BASE_T1 = 100
    """BASE-T1"""
    BASE_T1S = 101
    """BASE-T1S"""


class TXHState(IntEnum):
    """Recent Change in EEE State on TX"""
    TXH_NA = 0
    """Leaving or Going Into"""
    TXH_X = 1
    """No Activity"""


class RXHState(IntEnum):
    """Recent Change in EEE State on RX"""
    RXH_NA = 0
    """Leaving or Going Into"""
    RXH_X = 1
    """No Activity"""


class TXCState(IntEnum):
    """TX EEE State"""
    TXC_ACTIVE = 0
    """Active"""
    TXC_LPI = 1
    """Low Power"""


class RXCState(IntEnum):
    """RX EEE State"""
    RXC_ACTIVE = 0
    """Active"""
    RXC_LPI = 1
    """Low Power"""


class LinkState(IntEnum):
    """Low Power Mode Link State"""
    LINK_DOWN = 0
    """Link Down"""
    LINK_UP = 1
    """Link Up"""


class FaultSignaling(IntEnum):
    """Fault Signaling Behavior"""
    NORMAL = 0
    """Normal"""
    FORCE_LOCAL = 1
    """Forced to Local"""
    FORCE_REMOTE = 2
    """Forced to Remote"""
    DISABLED = 3
    """Disabled"""


class LocalFaultStatus(IntEnum):
    """Local Fault Status"""
    OK = 0
    """OK"""
    LOCAL_FAULT = 1
    """Local Fault"""


class RemoteFaultStatus(IntEnum):
    """Remote Fault Status"""
    OK = 0
    """OK"""
    REMOTE_FAULT = 1
    """Remote Fault"""


class TPLDMode(IntEnum):
    """Test Payload Mode"""
    NORMAL = 0
    """Normal"""
    MICRO = 1
    """Micro"""


class SerdesStatus(IntEnum):
    """Serdes Status"""
    STOPPED = 0
    """Stopped"""
    STARTED = 1
    """Started"""
    INITIALIZING = 2
    """Initializing"""
    PLOTTING = 3
    """Plotting"""


class FECMode(IntEnum):
    """FEX Mode"""
    OFF = 0
    """Off"""
    ON = 1
    """On"""
    RS_FEC = 2
    """RS FEC"""
    FC_FEC = 3
    """Firecode FEC"""
    RS_FEC_KR = 4
    """RS FEC KR"""
    RS_FEC_KP = 5
    """RS FEC KP"""


class PRBSInsertedType(IntEnum):
    """PRBS Type"""
    CAUI_VIRTUAL = 0
    """CAUI Virtual"""
    PHY_LINE = 1
    """PHY Line"""
    PHY_HOST = 2
    """PHY Host"""
    TCVR = 3
    """Tranceiver"""


class PRBSPolynomial(IntEnum):
    """PRBS Polynomial"""
    PRBS7 = 0
    """PRBS-7"""
    PRBS9 = 1
    """PRBS-9"""
    PRBS11 = 2
    """PRBS-11"""
    PRBS15 = 3
    """PRBS-15"""
    PRBS23 = 4
    """PRBS-23"""
    PRBS31 = 5
    """PRBS-31"""
    PRBS58 = 6
    """PRBS-58"""
    PRBS49 = 7
    """PRBS-49"""
    PRBS10 = 8
    """PRBS-10"""
    PRBS20 = 9
    """PRBS-20"""
    PRBS13 = 10
    """PRBS-13"""


class PRBSInvertState(IntEnum):
    """PRBS Invert State"""
    NON_INVERTED = 0
    """Non-inverted"""
    INVERTED = 1
    """Inverted"""


class PRBSStatisticsMode(IntEnum):
    """PRBS Statistics Mode"""
    ACCUMULATIVE = 0
    """Accumulative"""
    PERSECOND = 1
    """Per Second"""


class AutoNegMode(IntEnum):
    """Auto Neg Mode"""
    ANEG_OFF = 0
    """Auto Neg Off"""
    ANEG_ON = 1
    """Auto Neg On"""


class AutoNegTecAbility(IntEnum):
    """Auto Neg Technical Abilities"""
    DEFAULT_TECH_MODE = 0
    """Default Tech Mode"""
    IEEE_10G_KR = 4
    """IEEE 10G KR"""
    IEEE_40G_CR4 = 16
    """IEEE 40G CR4"""
    IEEE_100G_KR4 = 128
    """IEEE 100G KR4"""
    IEEE_100G_CR4 = 256
    """IEEE 100G CR4"""
    IEEE_25GBASE_CRS_KRS = 512
    """IEEE 25GBASE CRS KRS"""
    IEEE_25GBASE_CR_KR = 1024
    """IEEE 25GBASE CR KR"""
    IEEE_50GBASE_CR_KR = 8192
    """IEEE 50GBASE CR KR"""
    IEEE_100GBASE_CR2_KR2 = 16384
    """IEEE 100GBASE CR2 KR2"""
    IEEE_200GBASE_CR4_KR4 = 32768
    """IEEE 200GBASE CR4 KR4"""
    EC_25GBASE_KR1 = 16777216
    """EC 25GBASE KR1"""
    EC_25GBASE_CR1 = 33554432
    """EC 25GBASE CR1"""
    EC_50GBASE_KR2 = 67108864
    """EC 50GBASE KR2"""
    EC_50GBASE_CR2 = 134217728
    """EC 50GBASE CR2"""
    EC_400GGBASE_KR8 = 268435456
    """EC 400GGBASE KR8"""
    EC_50G_CR1_KR1 = 503
    """EC 50G CR1 KR1"""
    BAM_50G_CR1_KR1 = 504
    """BAM 50G CR1 KR1"""
    BAM_50G_CR2_KR2 = 505
    """BAM 50G CR2 KR2"""
    BAM_100G_CR2_KR2 = 1002
    """BAM 100G CR2 KR2"""
    BAM_100G_CR4_KR4 = 1003
    """BAM 100G CR4 KR4"""
    BAM_200G_CR2_KR2 = 2002
    """BAM 200G CR2 KR2"""
    BAM_400G_CR8_KR8 = 4001
    """BAM 400G CR8 KR8"""


class AutoNegFECOption(IntEnum):
    """Auto Neg FEC Options"""
    DEFAULT_FEC = 0
    """Default FEC"""
    NO_FEC = 1
    """No FEC"""
    FCFEC = 2
    """Firecode FEC"""
    RSFEC_CL91 = 4
    """RS FEC Cl91"""
    RS528 = 256
    """RS 528"""
    RS544 = 512
    """RS 544"""
    RS272 = 1024
    """RS 272"""


class PauseMode(IntEnum):
    """Pause Mode"""
    NO_PAUSE = 0
    """No Pause"""
    SYM_PAUSE = 1
    """Symmetric Pause"""
    ASYM_PAUSE = 2
    """Asymmetric Pause"""


class AutoNegFECType(IntEnum):
    """Auto Neg FEC Type"""
    PENDING = 0
    """Pending"""
    NOFEC = 1
    """No FEC"""
    RS_FEC = 513
    """RS FEC"""
    FC_FEC = 257
    """Firecode FEC"""


class AutoNegStatus(IntEnum):
    """Auto Neg Status"""
    UNKNOWN = 0
    """Unknown"""
    ENABLE = 1
    """Enabled"""
    TRANSMIT_DISABLE = 2
    """Transmit Disabled"""
    ABILITY_DETECT = 3
    """Ability Detected"""
    ACKNOWLEDGE_DETECT = 4
    """Acknowledge Detected"""
    COMPLETE_ACKNOWLEDGE = 5
    """Complete Acknowledge"""
    NEXT_PAGE_WAIT = 6
    """Next Page Wait"""
    AN_GOOD_CHECK = 7
    """AN Good Check"""
    AN_GOOD = 8
    """AN Good"""


class AutoNegFECStatus(IntEnum):
    """Auto Neg FEC Status"""
    DEFAULT_FEC = 0
    """Default FEC"""
    NO_FEC = 1
    """No FEC"""
    FC_FEC = 2
    """Firecode FEC"""
    RSFEC_CL91 = 4
    """RS FEC Cl91"""
    RS528 = 256
    """RS 528"""
    RS544 = 512
    """RS 544"""
    RS272 = 1024
    """RS 272"""


class LinkTrainingMode(IntEnum):
    """Link Training Mode"""
    AUTO = 0
    """Auto"""
    FORCE_ENABLE = 1
    """Forced Enable"""


class PAM4FrameSize(IntEnum):
    """PAM4 Frame Size"""
    N16K_FRAME = 0
    N4K_FRAME = 1


class LinkTrainingInitCondition(IntEnum):
    """Link Training Intialization Condition"""
    NO_INIT = 0
    """No Intialization"""
    INIT_ENABLED = 1
    """Intialization Enabled"""


class NRZPreset(IntEnum):
    """NRZ Preset"""
    NRZ_NO_PRESET = 0
    """NRZ without Preset"""
    NRZ_WITH_PRESET = 1
    """NRZ with Preset"""


class TimeoutMode(IntEnum):
    DEFAULT_TIMEOUT = 0
    TIMEOUT_DISABLED = 255


class LinkTrainingStatusMode(IntEnum):
    DISABLED = 0
    ENABLED = 1


class LinkTrainingStatus(IntEnum):
    """Link Training Status"""
    NOT_TRAINED = 0
    """Not Trained"""
    TRAINED = 1
    """Trained"""


class LinkTrainingFailureType(IntEnum):
    """Link Training Failure Type"""
    NO_FAILURE = 0
    """No Failure"""
    FRAME_LOCK_ERROR = 1
    """Frame Lock Error"""
    SNR_BELOW_THRESHOLD = 2
    """SNR Below Threshold"""
    TIME_OUT_FAILURE = 3
    """Timeout Failure"""


class Role(IntEnum):
    CLIENT = 0
    SERVER = 1


class Timescale(IntEnum):
    MSECS = 0
    SECONDS = 1
    MINUTES = 2
    HOURS = 3


class MSSType(IntEnum):
    FIXED = 0
    INCREMENT = 1
    RANDOM = 2


class RTOType(IntEnum):
    STATIC = 0
    DYNAMIC = 1


class CongestionType(IntEnum):
    NONE = 0
    RENO = 1
    NEW_RENO = 2


class IsEnabled(IntEnum):
    DISABLE = 0
    ENABLE = 1


class AlgorithmMethod(IntEnum):
    RFC5681 = 0
    RFC2581 = 1
    FIXED_FACTOR = 2


class AutoOrManual(IntEnum):
    AUTOMATIC = 0
    MANUAL = 1


class EmbedIP(IntEnum):
    DONT_EMBED_IP = 0
    EMBED_IP = 1


class ApplicationLayerBehavior(IntEnum):
    NONE = 0
    RAW = 1
    REPLAY = 2


class TrafficScenario(IntEnum):
    DOWNLOAD = 0
    UPLOAD = 1
    BOTH = 2
    ECHO = 3


class PayloadGenerationMethod(IntEnum):
    FIXED = 0
    INCREMENT = 1
    RANDOM = 2
    LONGRANDOM = 3


class InfiniteOrFinite(IntEnum):
    INFINITE = 0
    FINITE = 1


class WhoClose(IntEnum):
    NONE = 0
    CLIENT = 1
    SERVER = 2


class LifecycleMode(IntEnum):
    ONCE = 0
    IMMORTAL = 1
    REINCARNATE = 2


class L47IPVersion(IntEnum):
    IPV4 = 4
    IPV6 = 6


class L47ProtocolType(IntEnum):
    TCP = 0
    UDP = 1


class L47TrafficState(IntEnum):
    OFF = 0
    ON = 1
    STOP = 2
    PREPARE = 3
    PRERUN = 4


class L47PortState(IntEnum):
    OFF = 0
    PREPARE = 1
    PREPARE_RDY = 2
    PREPARE_FAIL = 3
    PRERUN = 4
    PRERUN_RDY = 5
    RUNNING = 6
    STOPPING = 7
    STOPPED = 8


class L47PortSpeed(IntEnum):
    AUTO = 0
    F100M = 1
    F1G = 2
    F2_5G = 3
    F5G = 4
    F10G = 5
    F25G = 6
    F40G = 7
    F50G = 8
    F100G = 9


class CaptureSize(IntEnum):
    FULL = 0
    SMALL = 1


class ReplayParserState(IntEnum):
    OFF = 0
    PARSING = 1


class IsPresent(IntEnum):
    NOT_PRESENT = 0
    PRESENT = 1


class LicenseSpeed(IntEnum):
    UNDEFINED = 0
    F1G = 1
    F2_5G = 2
    F5G = 3
    F10G = 4
    F25G = 5
    F40G = 6
    F50G = 7
    F100G = 8


class TLSVersion(IntEnum):
    SSLV3 = 0
    TLS10 = 1
    TLS11 = 2
    TLS12 = 3


class HeaderFormat(IntEnum):
    NOHDR = 0
    VLAN = 1


# class Infinite(IntEnum):
#     INFINITE = 0


class CorruptionType(IntEnum):
    OFF = 0
    ETH = 1
    IP = 2
    UDP = 3
    TCP = 4
    BER = 5


class PolicerMode(IntEnum):
    L1 = 0
    L2 = 1


class EthernetInfo(IntEnum):
    OFF = 0
    AND = 1


class Clude(IntEnum):
    EXCLUDE = 0
    INCLUDE = 1


class L2PlusPresent(IntEnum):
    NA = 0
    VLAN1 = 1
    VLAN2 = 2
    MPLS = 3


class L3PlusPresent(IntEnum):
    NA = 0
    IP4 = 1
    IP6 = 2


class FlowMode(IntEnum):
    """Impairment Flow Mode"""
    BASIC = 0
    """Basic Mode"""
    EXTENDED = 1
    """Extended Mode"""


class TimeKeeperLicenseFileState(IntEnum):
    NA = 0
    INV = 1
    VALID = 2


class TimeKeeperLicenseType(IntEnum):
    UNDEF = 0
    CLIENT = 1
    SERVER = 2


class TimeKeeperLicenseError(IntEnum):
    NO_LICENSE_ERROR = 0
    INVALID_SERIALNO = 1
    INVALID_CHASSISTYPE = 2


class SystemUpdateStatus(IntEnum):
    OK = 0
    FAILED_SCRIPT = 1
    FAILED_PREP = 10
    FAILED_FILENAME = 11
    FAILED_DECRYPT = 12
    FAILED_UNPACK = 13
    FAILED_VERIFY = 14
    FAILED_MOVE = 15


class TimeKeeperServiceStatus(IntEnum):
    STOPPED = 0
    STARTED = 1
    NA = 2


class TimeKeeperServiceAction(IntEnum):
    STOP = 0
    START = 1
    RESTART = 2


class CustomDefaultCommand(IntEnum):
    SET = 0
    CLEAR = 1


class CustomDefaultScope(IntEnum):
    ALL = 0
    INSTANCE = 1


class ImpairmentLatencyMode(IntEnum):
    NORMAL = 0
    EXTENDED = 1


class ResourceAllocationMode(IntEnum):
    SIMPLE = 0
    ADVANCED = 1


class ReplaySchedulingMode(IntEnum):
    BANDWIDTH = 0
    TIME = 1


class ReplaySyncBasedOn(IntEnum):
    PER_CONN = 0
    PER_USER = 1


class TrafficError(IntEnum):
    NOT_PREPARED = 0
    RATE_LENGTH_ERROR = 1
    PREPARED_OK = 2


class PRBSOnOff(IntEnum):
    PRBSOFF = 0
    PRBSON = 1


class ErrorOnOff(IntEnum):
    ERRORSOFF = 0
    ERRORSON = 1


class PRBSPattern(IntEnum):
    PRBS7 = 0
    PRBS9 = 1
    PRBS11 = 2
    PRBS15 = 3
    PRBS23 = 4
    PRBS31 = 5


class PHYSignalStatus(IntEnum):
    NO_SIGNAL = 0
    NO_CDRLOCK = 2
    LOCKED = 3


class ShadowWorkingSelection(IntEnum):
    SHADOW = 0
    WORKING = 1


class TSNConfigProfile(IntEnum):
    AUTOMOTIVE = 0
    IEEE1588V2 = 1


class TSNPortRole(IntEnum):
    GRANDMASTER = 0
    SLAVE = 1


class TSNDeviationMode(IntEnum):
    FIXED = 0


class TSNTimeSource(IntEnum):
    ATOMIC = 0x10
    GPS = 0x20
    TERRESTRIAL = 0x30
    PTP = 0x40
    NTP = 0x50
    HAND_SET = 0x60
    OTHER = 0x90
    INTERNAL_OSC = 0xA0


class TSNSource(IntEnum):
    DRIFT = 0
    DRIFTPRE = 1
    PDELAY = 2
    NRR = 3


class TSNClearStatistics(IntEnum):
    ALL = 0
    PACKETCOUNT = 1
    OFFSET = 2
    PDELAY = 3
    SYNCRATE = 4


class PFCMode(IntEnum):
    VLAN_PCP = 128


class OnOffDefault(IntEnum):
    OFF = 0
    ON = 1
    DEFAULT = 2


class ImpairmentTypeIndex(IntEnum):
    DROP = 0
    MISORDER = 1
    DELAYJITTER = 2
    DUPLICATION = 3
    CORRUPTION = 4
    POLICER = 5
    SHAPER = 6


class FilterType(IntEnum):
    SHADOWN = 0  # “shadow-copy”
    WORKING = 1  # “working-copy”


class VlanType(IntEnum):
    INNER = 0  # VLAN1 (0) (INNER VLAN Tag is specified for the filter – used also when only 1 VLAN), indicates single/inner VLAN-TPID=0x8100
    OUTER = 1  # VLAN2 (1) (OUTER VLAN Tag is specified for the filter), indicates outer VLAN-TPID=0x88A8


class LatencyType(IntEnum):
    INTERPACKET_DISTRIBUTION = 0
    LATENCY_DISTRIBUTION = 1
