# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Authors: Endre Karlson <endre.karlson@hp.com>
#          Christopher Small <christopher.small@hp.com>
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

from odlclient.openstack.common.apiclient import base
from odlclient.v2 import base as v2_base
import uuid


class Flow(base.Resource):
    @property
    def name(self):
        if self._info['name'] is None:
            name = uuid.uuid1()
        else:
            name = self._info['name']
        return name

    @property
    def match(self):
        data = self._info['match']['value']
        return None if data == 'None' else data

    @property
    def action(self):
        data = self._info['action']['value']
        return None if data == 'None' else data

    def json(self):
        data = json.dumps(self._info)
        return data


class FlowManager(v2_base.Manager):
    base = 'controller/nb/v2/flowprogrammer'
    has_container = True
    resource_class = Flow

    def list(self):
        return self.list_flows()

    def list_flows(self, container=None):
        url = self._url(container=container)
        return self._list(url, response_key='flowConfig')

    def list_flows_node(self, node_type, node_id, container=None):
        url = self._url('node', node_type, node_id, container=container),
        self._list(url, response_key='flowConfig')

    def get_flow(self, node_type, node_id, name, container=None):
        url = self._url('node', node_type, node_id, name, container=container)
        return self._get(url)

    def add_flow_json(self, node_type, node_id, name, json_flow,
                      container=None):
        url = self._url('node', node_type, node_id, 'staticFlow',
                        name, container=container)
        return self._put(url, json_flow)

    def delete_flow(self, node_type, node_id, name, container=None):
        url = self._url('node', node_type, node_id, 'staticFlow',
                        name, container=container)
        return self._delete(url)

    def add_flow(self, node_type, node_id, name, flow, container=None):
        url = self._url('node', node_type, node_id, 'staticFlow',
                        name, container=container)
        return self._put(url, flow.json())
