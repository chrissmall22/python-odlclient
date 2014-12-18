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

FLOW = {
    "duration_sec": 66,
    "duration_nsec": 825000000,
    "priority": 29999,
    "idle_timeout": 300,
    "hard_timeout": 0,
    "cookie": "0x2328",
    "packet_count": 2,
    "byte_count": 140,
    "match": [
        {
            "in_port": 3
        },
        {
            "eth_src": "be:f9:8c:b6:5b:9c"
        },
        {
            "eth_dst": "fe:b4:08:c5:23:fc"
        }
    ],
    "actions": [
        {
            "output": 2
        }
    ]
}

FLOW_MA = {
    "duration_sec": 66,
    "duration_nsec": 825000000,
    "priority": 29999,
    "idle_timeout": 300,
    "hard_timeout": 0,
    "cookie": "0x2328",
    "packet_count": 2,
    "byte_count": 140,
    "match": [
        {
            "in_port": 3
        },
        {
            "eth_src": "be:f9:8c:b6:5b:9c"
        },
        {
            "eth_dst": "fe:b4:08:c5:23:fc"
        }
    ],
    "actions": [
        {
            "output": 1
        },
        {
            "output": 2
        },
        {
            "output": 3
        }
    ]
}
