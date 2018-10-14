class RegrasFirewall():
    def __init__(self, dpid, id,src, dst, protocol, permission):
        self.dpid = dpid
        self.id = id
        self.src = self.netmask_prefix(src)
        self.dst = self.netmask_prefix(dst)
        self.protocol = protocol
        self.permission = permission

    def netmask_prefix(self, address):
        if address != 'any':
            ip = address.split("/")[0]
            vet_mask = address.split("/")[1].split(".")
            prefix = 0
            for oct in vet_mask:
                if int(oct) == 255:
                    prefix += 8
                elif int(oct) > 0 and int(oct) < 255:
                    b = bin(int(oct)).split("b")[1].count("1")
                    prefix += b
            addr = "%s/%s" %(ip,prefix)
            return addr
        else:
            return address



def applyRegras(src,prefix_src,dst, prefix_dst, proto, action):
    dic = {}

    if src != '' and prefix_src != '':
        dic['nw_src'] = "%s/%s" %(src, prefix_src.replace('/',''))

    if dst != '' and prefix_dst != '':
        dic['nw_dst'] = "%s/%s"%(dst, prefix_dst.replace('/',''))

    if proto != '':
        dic['nw_proto'] = proto.upper()
    
    if action.upper() != 'ALLOW':
        dic['actions'] = action.upper()

    return dic

class RegrasQos:
    def __init__(self, sw_id, prio, proto, port_dst, addr_dst, qos_id, action):
        self.sw_id = sw_id
        self.priority = prio
        self.protocol = proto
        self.port_dst = port_dst
        self.addr_dst = addr_dst
        self.qos_id = qos_id
        self.action = action


class SwitchConfQoS:
    def __init__(self, dpid, port):
        self.dpid = dpid
        self.port = port


class QoSQueue:
    def __init__(self, id,max_rate = '-',min_rate = "-"):
        self.id = id
        self.max_rate = max_rate
        self.min_rate = min_rate