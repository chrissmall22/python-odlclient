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

from odlclient.openstack.common.apiclient import base


LOG = logging.getLogger(__name__)


class Manager(base.ManagerWithFind):
    base = None
    has_container = False

    def _url(self, *args, **kw):
        parts = []
        if self.base is not None:
            parts.append(self.base)

        if self.has_container:
            container = kw.pop('container', None) or 'default'
            parts.append(container)

        parts.extend(args)
        url = "/".join([i for i in parts if i is not None])
        LOG.debug("Returning url %s", url)
        return url
