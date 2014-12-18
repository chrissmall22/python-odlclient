#!/usr/bin/env python
#
#   Copyright 2014 Hewlett-Packard Development Company, L.P.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from odlclient.tests import base
from odlclient.v2 import datatypes

OF10_DPID = '00:00:00:00:00:00:00:03'
OF13_DPID = '00:00:00:00:00:00:00:04'


class TestOfFlowManager(base.ClientTestCase):
    def setUp(self):
        super(TestOfFlowManager, self).setUp()

    def tearDown(self):
        super(TestOfFlowManager, self).tearDown()

    def test_list_flows(self):
        flow_json = '{"name":"flow_list", "node": ' \
                    '{"id":"00:00:00:00:00:00:00:03", ' \
                    '"type":"OF"}, "etherType": "0x800",' \
                    '"protocol": "6", "tpDst": "80", ' \
                    '"nwSrc": "10.10.10.20", ' \
                    '"priority":"100","actions":["DROP"]}'

        self.client.flows.add_flow('OF', OF10_DPID,
                                   "flow_list", flow_json)
        data = self.client.flows.list_flows()
        # Cleanup flow
        self.client.nodes.delete_flow_json('OF', OF10_DPID, 'flow_list')
        self.assertTrue(data)

    def test_list_flows_node(self):
        flow_json = '{"name":"flow_list_node", "node": ' \
                    '{"id":"00:00:00:00:00:00:00:03", ' \
                    '"type":"OF"}, "etherType": "0x800",' \
                    '"protocol": "6", "tpDst": "80", ' \
                    '"nwSrc": "10.10.10.30", ' \
                    '"priority":"100","actions":["DROP"]}'
        self.client.flows.add_flow('OF', OF10_DPID,
                                   "flow_list_node", flow_json)
        data = self.client.flows.list_flows_node('OF', OF10_DPID)

        self.client.nodes.delete_flow('OF', OF10_DPID, 'flow_list_node')
        self.assertTrue(data)

    def test_add_flow_json(self):
        flow_json = '{"name":"flow_add", "node": ' \
                    '{"id":"00:00:00:00:00:00:00:03", ' \
                    '"type":"OF"}, "etherType": "0x800",' \
                    '"protocol": "6", "tpDst": "80", ' \
                    '"nwSrc": "10.10.10.40", ' \
                    '"priority":"100","actions":["DROP"]}'

        data = self.client.flows.add_flow('OF', OF10_DPID,
                                          "flow_add", flow_json)

        self.client.nodes.delete_flow('OF', OF10_DPID, 'flow_add')

        self.assertTrue(data)

    def test_del_flow_json(self):
        flow_json = '{"name":"flow_del", "node": ' \
                    '{"id":"00:00:00:00:00:00:00:03", ' \
                    '"type":"OF"}, "etherType": "0x800",' \
                    '"protocol": "6", "tpDst": "80", ' \
                    '"nwSrc": "10.10.10.50", ' \
                    '"priority":"100","actions":["DROP"]}'
        data = self.client.flows.add_flow('OF', OF10_DPID,
                                          "flow_del", flow_json)
        self.assertTrue(data)

        data2 = self.client.nodes.delete_flow('OF', OF10_DPID,
                                              'flow_del')
        self.assertFalse(data2)

    def test_add_flow_OF13(self):

        #create the action objects
        match = datatypes.Match(eth_type="ipv4", ipv4_src="10.0.0.1",
                                ipv4_dst="10.0.0.22", ip_proto="tcp",
                                tcp_dst="80")
        instr = datatypes.Instruction(apply_actions='DROP')

        #create the flows
        flow1 = datatypes.Flow(priority=30000, idle_timeout=30,
                               match=match, instructions=instr)

        data = self.client.flows.add_flow('OF', OF13_DPID,
                                          "flow_of13", flow1)

        self.client.nodes.delete_flow('OF', OF13_DPID,
                                      'flow_of13')
        self.assertTrue(data)

    def test_add_flow_OF10(self):

        #create the action objects
        match = datatypes.Match(eth_type="ipv4", ipv4_src="10.0.0.1",
                                ipv4_dst="10.0.0.22", ip_proto="tcp",
                                tcp_dst="80")
        output1 = datatypes.Action(output=1)

        #create the flows
        flow1 = datatypes.Flow(priority=30000, idle_timeout=30,
                               match=match, actions=output1)

        data = self.client.flows.add_flow('OF', OF10_DPID,
                                          "flow_of10", flow1)
        #pprint.pprint(flow_json)
        self.client.nodes.delete_flow('OF', OF10_DPID, 'flow_of10')

        self.assertTrue(data)
