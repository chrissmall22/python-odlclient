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

import odlclient.tests.data as test_data
import odlclient.v2.datatypes as datatypes
import unittest


class FactoryTests(unittest.TestCase):
    """Tests the JsonObjectFactory."""

    def _test_type(self, data, datatype):
        """Tests that the provided data is cast to the correct class.
        If attributes within the class are also mapped to Python objects,
        these are also checked
        """

        type_name = datatype.__name__
        obj = datatypes.JsonObjectFactory.create(type_name, data)
        self.assertTrue(isinstance(obj, datatype))

        try:
            class_map = datatypes.CLASS_MAP[type_name]

            for key in class_map:
                if eval('obj.%s' % key) is None:
                    continue
                else:
                    attribute = eval('obj.%s' % key)
                    if type(attribute) is None:
                        break
                    elif type(attribute) == list:
                        for item in attribute:
                            cls = eval('datatypes.%s' % class_map[key])
                            self.assertTrue(isinstance(item, cls))

                    else:
                        cls = eval('datatypes.%s' % class_map[key])
                        self.assertTrue(isinstance(attribute, cls))
        except KeyError:
            pass

        return obj

    def test_create_flow(self):
        obj = self._test_type(test_data.FLOW, datatypes.Flow)
        self.assertEqual(obj.actions[0].output, 2)

    def test_create_flow_multiple_action(self):
        obj = self._test_type(test_data.FLOW_MA, datatypes.Flow)
        self.assertEqual(obj.actions[2].output, 3)
