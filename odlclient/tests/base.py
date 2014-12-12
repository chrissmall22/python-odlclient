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

import os
import unittest


CTL = os.getenv("ODL_CONTROLLER")
USER = os.getenv("ODL_USER")
PASS = os.getenv("ODL_PASS")

url = 'http://' + CTL + ':8080'


class ClientTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        http_client = odlclient.HTTPClient(url, username=USER, password=PASS)
        cls.http_client = http_client

        cls.client = odlclient.Client(http_client)

    @classmethod
    def tearDownClass(cls):
        cls.http_client = None
        cls.client = None
