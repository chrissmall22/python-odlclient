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

from odlclient.v2.client import BridgeDomainManager
from odlclient.v2.client import Client
from odlclient.v2.client import ConnectionManager

from odlclient.v2.client import HTTPClient
from odlclient.v2.client import NeutronManagers
from odlclient.v2.client import NodeManager
from odlclient.v2.client import OvsdbManager
from odlclient.v2.client import StaticRouteManager
from odlclient.v2.client import SubnetManager

import unittest


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.http_client = HTTPClient('http://10.10.10.10:8080',
                                      username='admin',
                                      password='admin')

    def test_client(self):

        http_client = self.http_client

        api = Client(http_client)
        self.assertTrue(isinstance(api.bridge_domain, BridgeDomainManager))
        self.assertTrue(isinstance(api.connection_manager, ConnectionManager))
        self.assertTrue(isinstance(api.nodes, NodeManager))
        self.assertTrue(isinstance(api.ovsdb, OvsdbManager))
        self.assertTrue(isinstance(api.subnets, SubnetManager))
        self.assertTrue(isinstance(api.staticroutes, StaticRouteManager))
        self.assertTrue(isinstance(api.neutron, NeutronManagers))

    def test_httpclient(self):
        http_client = self.http_client

        self.assertEqual(http_client.endpoint, 'http://10.10.10.10:8080')
        self.assertEqual(http_client.username, 'admin')
        self.assertEqual(http_client.password, 'admin')
