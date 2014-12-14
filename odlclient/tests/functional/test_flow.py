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

from odlclient.tests.base import ClientTestCase

OF10_DPID = '00:00:00:00:00:00:00:03'
INT_DPID = '3'


class TestOfFlowManager(ClientTestCase):
    def setUp(self):
        super(TestOfFlowManager, self).setUp()

    def tearDown(self):
        super(TestOfFlowManager, self).tearDown()

    def test_list_flows(self):
        data = self.client.flows.list_flows()
        self.assertTrue(data)

    def test_list_flows_node(self):
        data = self.client.flows.list_flows_node('OF', OF10_DPID)
        self.assertTrue(data)

    def test_add_flow_json(self):
        flow_json = '{"nwSrc": "10.10.10.10", "actions": [ "OUTPUT=2" ]}'

        data = self.client.flows.add_flow_json('OF', OF10_DPID,
                                               "flow1", flow_json)
        self.assertTrue(data)

    def test_del_flow_json(self):
        flow_json = '{"nwSrc": "10.10.10.11", "actions": [ "OUTPUT=2" ]}'

        data = self.client.flows.add_flow_json('OF', OF10_DPID,
                                               "flow2", flow_json)
        self.assertTrue(data)

        data2 = self.client.nodes.delete_flow_json('OF', OF10_DPID,
                                                   'flow2')
        self.assertFalse(data2)
