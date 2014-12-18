# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Author: Christopher Small <christopher.small@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json

KEYWORDS = ["self"]

CLASS_MAP = {'ControllerStats': {'lost': 'Counter',
                                 'packet_in': 'Counter',
                                 'packet_out': 'Counter'},
             'Team': {'systems': 'TeamSystem'},
             'Flow': {'match': 'Match',
                      'actions': 'Action',
                      'instructions': 'Instruction'},
             'Stats': {'port_stats': 'PortStats',
                       'group_stats': 'GroupStats',
                       'meter_stats': 'MeterStats'},
             'Packet': {'eth': 'Ethernet',
                        'ip': 'Ip',
                        'ipv6': 'Ipv6',
                        'udp': 'Udp',
                        'tcp': 'Tcp',
                        'dhcp': 'Dhcp',
                        'icmp': 'Icmp',
                        'icmpv6': 'Icmpv6'}
             }


class JsonObjectFactory(object):

    factories = {}

    @staticmethod
    def add_factory(id, factory):
        JsonObjectFactory.factories[id] = factory

    @staticmethod
    def create(id, data):
        for key in data:
            if key in KEYWORDS:
                new_key = key + "_"
                data[new_key] = data.pop(key)
        if id not in JsonObjectFactory.factories:
            JsonObjectFactory.add_factory(id, eval(id))
        return JsonObjectFactory.factories[id].factory(data)


class JsonObject(object):

    """This is the base class for all HP SDN Client data types."""

    def __str__(self):
        return self.to_json_string()

    def to_json_string(self):
        tmp = self.to_dict()
        return json.dumps(tmp, sort_keys=True,
                          indent=4, separators=(',', ': '))

    def to_dict(self):
        data = {}
        attributes = [attr for attr in dir(self)
                      if not callable(getattr(self, attr))
                      and not attr.startswith("__")]
        for attr in attributes:
            if getattr(self, attr) is not None:
                value = getattr(self, attr)
                if isinstance(value, list):
                    tmp = []
                    for list_item in value:
                        if isinstance(list_item, JsonObject):
                            tmp.append(list_item.to_dict())
                        else:
                            tmp.append(list_item)
                    data[attr.__str__()] = tmp
                elif isinstance(value, JsonObject):
                    data[attr.__str__()] = value.to_dict()
                elif type(value):
                    data[attr.__str__()] = value
        return data

    @classmethod
    def factory(cls, data):
        try:
            cm = CLASS_MAP[cls.__name__]
            for key in data:
                if key in cm and isinstance(data[key], list):
                    l = []
                    for d in data[key]:
                        l.append(JsonObjectFactory.create(cm[key], d))
                    data[key] = l
                elif key in cm:
                    data[key] = JsonObjectFactory.create(cm[key], data[key])
        except KeyError:
            pass

        return cls(**data)

    def __eq__(self, other):
        attributes = [attr for attr in dir(self)
                      if not callable(getattr(self, attr))
                      and not attr.startswith("__")]
        for attr in attributes:
            try:
                if self.__getattribute__(attr) == other.__getattribute__(attr):
                    continue
                else:
                    return False
            except AttributeError:
                return False
        else:
            return True


class Match(JsonObject):
    """Match (JsonObject)

        A python representation of the Match object

    """
    def __init__(self, **kwargs):
        self.in_port = kwargs.get('in_port', None)
        self.in_phy_port = kwargs.get('in_phy_port', None)
        self.metadata = kwargs.get('metadata', None)
        self.tunnel_id = kwargs.get('tunnel_id', None)
        self.eth_dst = kwargs.get('eth_dst', None)
        self.eth_src = kwargs.get('eth_src', None)
        self.eth_type = kwargs.get('eth_type', None)
        self.ip_proto = kwargs.get('ip_proto', None)
        self.icmpv6_type = kwargs.get('icmpv6_type', None)
        self.ipv6_nd_sll = kwargs.get('ipv6_nd_sll', None)
        self.ipv6_nd_tll = kwargs.get('ipv6_nd_tll', None)
        self.vlan_vid = kwargs.get('vlan_vid', None)
        self.mode = kwargs.get('mode', None)
        self.vlan_pcp = kwargs.get('vlan_pcp', None)
        self.ip_dscp = kwargs.get('ip_dscp', None)
        self.ip_ecn = kwargs.get('ip_ecn', None)
        self.icmpv4_code = kwargs.get('icmpv4_code', None)
        self.icmpv6_code = kwargs.get('icmpv6_type', None)
        self.mpls_tc = kwargs.get('mpls_tc', None)
        self.mpls_bos = kwargs.get('mpls_bos', None)
        self.arp_op = kwargs.get('arp_op', None)
        self.ipv6_flabel = kwargs.get('ipv6_flabel', None)
        self.mpls_label = kwargs.get('mpls_label', None)
        self.pbb_isisd = kwargs.get('pbb_isisd', None)
        self.ipv4_src = kwargs.get('ipv4_src', None)
        self.ipv4_dst = kwargs.get('ipv4_dst', None)
        self.arp_spa = kwargs.get('arp_spa', None)
        self.arp_tpa = kwargs.get('arp_tpa', None)
        self.ipv6_src = kwargs.get('ipv6_src', None)
        self.ipv6_dst = kwargs.get('ipv6_dst', None)
        self.ipv6_nd_target = kwargs.get('ipv6_nd_target', None)
        self.tcp_src = kwargs.get('tcp_src', None)
        self.tcp_dst = kwargs.get('tcp_dst', None)
        self.udp_src = kwargs.get('udp_src', None)
        self.udp_dst = kwargs.get('udp_dst', None)
        self.sctp_src = kwargs.get('sctp_src', None)
        self.sctp_dst = kwargs.get('sctp_dst', None)
        self.icmpv4_type = kwargs.get('icmpv4_type', None)
        self.ipv6_exthdr = kwargs.get('ipv6_exthdr', None)

    def to_dict(self):
        """to_dict (self)

            Creates a representation of the class as a dictionary
            Overrides the parent method as all members variables of
            this class are strings

        """
        data = []
        attributes = [attr for attr in dir(self)
                      if not callable(getattr(self, attr))
                      and not attr.startswith("__")]
        for attr in attributes:
            if getattr(self, attr):
                tmp = {}
                tmp[attr.__str__()] = getattr(self, attr)
                data.append(tmp)
        return data


class Action(JsonObject):
    """Action (JsonObject)

        A python representation of the Action object

    """
    def __init__(self, **kwargs):
        self.output = kwargs.get('output', None)
        self.copy_ttl_out = kwargs.get('copy_ttl_out', None)
        self.copy_ttl_in = kwargs.get('copy_ttl_in', None)
        self.set_mpls_ttl = kwargs.get('set_mpls_ttl', None)
        self.dec_mpls_ttls = kwargs.get('dec_mpls_ttls', None)
        self.push_vlan = kwargs.get('push_vlan', None)
        self.pop_vlan = kwargs.get('pop_vlan', None)
        self.push_mpls = kwargs.get('push_mpls', None)
        self.pop_mpls = kwargs.get('pop_mpls', None)
        self.set_queue = kwargs.get('set_queue', None)
        self.group = kwargs.get('group', None)
        self.set_nw_ttl = kwargs.get('set_nw_ttl', None)
        self.dec_nw_ttl = kwargs.get('dec_nw_ttl', None)
        self.set_field = kwargs.get('set_field', None)
        self.push_pbb = kwargs.get('push_pbb', None)
        self.pop_pbb = kwargs.get('pop_pbb', None)
        self.experimenter = kwargs.get('experimenter', None)
        self.data = kwargs.get('data', None)

    def to_dict(self):
        """to_dict (self)

            Creates a representation of the class as a dictionary
            Overrides the parent method as all members variables of
            this class are strings

        """
        data = []
        attributes = [attr for attr in dir(self)
                      if not callable(getattr(self, attr))
                      and not attr.startswith("__")]
        for attr in attributes:
            if attr == "output":
                output = getattr(self, attr)
                if type(output) == list:
                    for port in output:
                        tmp = {}
                        tmp[attr.__str__()] = port
                        data.append(tmp)
                elif output:
                    tmp = {}
                    tmp[attr.__str__()] = getattr(self, attr)
                    data.append(tmp)
            else:
                if getattr(self, attr):
                    tmp = {}
                    tmp[attr.__str__()] = getattr(self, attr)
                    data.insert(0, tmp)
        return data


class Instruction(JsonObject,):
    """Instruction (JsonObject)

        A python representation of the Instruction object

    """
    def __init__(self, **kwargs):
        self.clear_actions = kwargs.get('clear_actions', None)
        self.write_actions = kwargs.get('write_actions', [])
        self.apply_actions = kwargs.get('apply_actions', [])
        self.write_metadata = kwargs.get('write_metadata', None)
        self.mask = kwargs.get('mask', None)
        self.meter = kwargs.get('meter', None)
        self.experimenter = kwargs.get('experimenter', None)


class Flow(JsonObject):
    """Flow (JsonObject)

        A python representation of the Flow object

    """
    def __init__(self, **kwargs):
        self.table_id = kwargs.get('table_id', None)
        self.priority = kwargs.get('priority', None)
        self.match = kwargs.get('match', None)
        self.duration_sec = kwargs.get('duration_sec', None)
        self.duration_nsec = kwargs.get('duration_nsec', None)
        self.idle_timeout = kwargs.get('idle_timeout', None)
        self.hard_timeout = kwargs.get('hard_timeout', None)
        self.packet_count = kwargs.get('packet_count', None)
        self.byte_count = kwargs.get('byte_count', None)
        self.cookie = kwargs.get('cookie', None)
        self.cookie_mask = kwargs.get('cookie_mask', None)
        self.buffer_id = kwargs.get('buffer_id', None)
        self.out_port = kwargs.get('out_port', None)
        self.flow_mod_cmd = kwargs.get('flow_mod_cmd', None)
        self.flow_mod_flags = kwargs.get('flow_mod_flags', [])
        self.instructions = kwargs.get('instructions', [])
        self.actions = kwargs.get('actions', [])
