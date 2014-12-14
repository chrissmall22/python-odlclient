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

from odlclient.v2 import client as odlclient
import unittest


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.http_client = odlclient.HTTPClient('http://10.10.10.10:8080',
                                                username='admin',
                                                password='admin')

    def test_client(self):

        http_client = self.http_client

        api = odlclient.Client(http_client)
        self.assertTrue(
            isinstance(api.bridge_domain,
                       odlclient.bridge_domain.BridgeDomainManager))
        self.assertTrue(
            isinstance(api.connection_manager,
                       odlclient.connection_manager.ConnectionManager))
        self.assertTrue(isinstance(api.nodes,
                                   odlclient.node.NodeManager))
        self.assertTrue(isinstance(api.ovsdb,
                                   odlclient.ovsdb.OvsdbManager))
        self.assertTrue(isinstance(api.subnets,
                                   odlclient.subnet.SubnetManager))
        self.assertTrue(isinstance(api.staticroutes,
                                   odlclient.staticroute.StaticRouteManager))
        self.assertTrue(isinstance(api.neutron,
                                   odlclient.neutron.NeutronManagers))

    def test_httpclient(self):
        http_client = self.http_client

        self.assertEqual(http_client.endpoint, 'http://10.10.10.10:8080')
        self.assertEqual(http_client.username, 'admin')
        self.assertEqual(http_client.password, 'admin')
