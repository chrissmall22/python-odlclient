# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Author: Endre Karlson <endre.karlson@hp.com>
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
import logging
import pprint
import os

from odlclient.v2 import client as odlclient

logging.basicConfig(level='DEBUG')

controller = os.getenv("ODL_CONTROLLER")
user = os.getenv("ODL_USER")
password = os.getenv("ODL_PASS")

url = 'http://' +  controller + ':8080'


http = odlclient.HTTPClient(url,
    username=user,
    password=password)

client = odlclient.Client(http)

connections = client.connection_manager.list()
for n in connections:
    if n.type == 'OVS':
        print("Getting OVSDB bridges")
        rows = client.ovsdb.list(n.type, n.id, 'open_vswitch')
        for r in rows.values():
            pprint.pprint(r)
