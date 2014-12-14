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
import pprint

OF10_DPID = '00:00:00:00:00:00:00:03'
INT_DPID = '3'


class TestOfNodeManager(base.ClientTestCase):
    def setUp(self):
        super(TestOfNodeManager, self).setUp()

    def tearDown(self):
        super(TestOfNodeManager, self).tearDown()

    def test_list(self):
        data = self.client.nodes.list()
        self.assertTrue(data)

    #def test_save(self):
    #    data = self.client.nodes.save()
    #    self.assertTrue(data)

    def test_list_connectors(self):
        data = self.client.nodes.list_connectors('OF', OF10_DPID)
        pprint.pprint(data)
        self.assertTrue(data)

    def test_property(self):
        data = self.client.nodes.create_property('OF', OF10_DPID,
                                                 'description', 'Switch3')
        self.assertFalse(data)

        data2 = self.client.nodes.delete_property('OF', OF10_DPID,
                                                  'description', 'Switch3')
        self.assertFalse(data2)

"""
    def test_connector_property(self):
        data = self.client.nodes.create_connector_property('OF', OF10_DPID,
                                                           'OF', '1',
                                                           'name', 'Port1')
        pprint.pprint(data)
        self.assertTrue(data)

        data2 = self.client.nodes.delete_connector_property('OF', OF10_DPID,
                                                           'OF', '1',
                                                           'name', 'Port1')
        pprint.pprint(data2)
        self.assertFalse(data2)
"""
