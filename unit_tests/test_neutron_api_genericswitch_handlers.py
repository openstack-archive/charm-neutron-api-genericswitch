# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import print_function

import mock

import reactive.neutron_api_genericswitch_handlers as handlers
import charm.openstack.neutron_api_genericswitch as neutron_api_genericswitch

import charms_openstack.test_utils as test_utils


class TestRegisteredHooks(test_utils.TestRegisteredHooks):
    def test_hooks(self):
        defaults = [
            'charm.installed',
            'config.changed',
            'update-status']
        hook_set = {
            'when': {
                'configure_plugin': (
                    'neutron-plugin-api-subordinate.connected',),
                'remote_restart': (
                    'neutron-plugin-api-subordinate.connected',),
            },
            'when_file_changed': {
                'remote_restart': (
                    neutron_api_genericswitch.ML2_CONF,),
            },
        }
        # test that the hooks were registered via the
        # reactive.barbican_handlers
        self.registered_hooks_test_helper(handlers, hook_set, defaults)


class TestHandlers(test_utils.PatchHelper):
    def test_configure_plugin(self):
        napi_gs_charm = mock.MagicMock()
        self.patch_object(handlers.charm, 'provide_charm_instance',
                          new=mock.MagicMock())
        self.provide_charm_instance().__enter__.return_value = napi_gs_charm

        handlers.configure_plugin('arg1')
        napi_gs_charm.configure_plugin.assert_called_once_with('arg1')

    def test_remote_restart(self):
        principle_interface = mock.MagicMock()
        handlers.remote_restart(principle_interface)
        principle_interface.request_restart.assert_called_once_with()
