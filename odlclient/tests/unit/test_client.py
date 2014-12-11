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

import json
import unittest
try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock

import requests


from odlclient.v2 import client as odlclient


class ClientTests(unittest.TestCase):
    def setUp(self):

        http = odlclient.HTTPClient('http://10.10.10.10:8080',
                                    username='admin',
                                    password='admin')

        self.client = odlclient.Client(http)
        response_ok = requests.Response()
        response_ok.status_code = 200
        self.response_ok = response_ok

    def test_post(self):
        self.client.post = MagicMock(name="post",
                                     return_value=self.response_ok)

        r = self.client.post('http://foo.bar', json.dumps({"some": "data"}))

        self.client.post.assert_called_with('http://foo.bar',
                                            json.dumps({"some": "data"}))

        self.assertTrue(isinstance(r, requests.Response))

    def test_put(self):
        self.client.put = MagicMock(name="put",
                                    return_value=self.response_ok)

        r = self.client.put('http://foo.bar', json.dumps({"some": "data"}))

        self.client.put.assert_called_with('http://foo.bar',
                                           json.dumps({"some": "data"}))

        self.assertTrue(isinstance(r, requests.Response))

    def test_delete_data(self):
        self.client.delete = MagicMock(name="delete",
                                       return_value=self.response_ok)

        r = self.client.delete('http://foo.bar', json.dumps({"some": "data"}))

        self.client.delete.assert_called_with('http://foo.bar',
                                              json.dumps({"some": "data"}))

        self.assertTrue(isinstance(r, requests.Response))

    def test_delete_no_data(self):
        self.client.delete = MagicMock(name="delete",
                                       return_value=self.response_ok)

        r = self.client.delete('http://foo.bar')

        self.client.delete.assert_called_with('http://foo.bar')

        self.assertTrue(isinstance(r, requests.Response))

    def test_head(self):
        self.client.head = MagicMock(name="head",
                                     return_value=self.response_ok)
        #self.raise_errors = MagicMock(name="raise_errors")

        r = self.client.head('http://foo.bar')

        self.client.head.assert_called_with('http://foo.bar')

        self.assertTrue(isinstance(r, requests.Response))
