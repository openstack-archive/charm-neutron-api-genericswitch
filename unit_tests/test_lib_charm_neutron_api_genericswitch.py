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
import charms_openstack.test_utils as test_utils

import charm.openstack.neutron_api_genericswitch as neutron_api_genericswitch


class TestNeutronAPIGenericSwitchCharm(test_utils.PatchHelper):
    def test_all_packages(self):
        self.patch_object(neutron_api_genericswitch.ch_utils, 'os_release')
        self.os_release.return_value = 'newton'
        c = neutron_api_genericswitch.NewtonNeutronAPIGenericSwitchCharm()
        self.assertEqual(
            c.all_packages,
            ['neutron-common', 'neutron-plugin-ml2'])

    def test_configure_plugin(self):
        principle_interface = mock.MagicMock()
        self.patch_object(neutron_api_genericswitch.ch_utils, 'os_release')
        self.os_release.return_value = 'newton'
        c = neutron_api_genericswitch.NewtonNeutronAPIGenericSwitchCharm()
        c.configure_plugin(principle_interface)
        config_dict = {
            'neutron-api': {
                '/etc/neutron/neutron.conf': {'sections': {'DEFAULT': []}}}}
        principle_interface.configure_plugin.assert_called_once_with(
            neutron_plugin='genericswitch',
            core_plugin='neutron.plugins.ml2.plugin.Ml2Plugin',
            neutron_plugin_config='/etc/neutron/plugins/ml2/ml2_conf.ini',
            service_plugins=('router,firewall,vpnaas,metering,'
                             'neutron_lbaas.services.loadbalancer.'
                             'plugin.LoadBalancerPluginv2'),
            subordinate_configuration=config_dict)


class TestNeutronAPIGenericSwitchCharmOnQueens(test_utils.PatchHelper):
    def test_all_packages(self):
        self.patch_object(neutron_api_genericswitch.ch_utils, 'os_release')
        self.os_release.return_value = 'queens'
        c = neutron_api_genericswitch.NewtonNeutronAPIGenericSwitchCharm()
        self.assertEqual(
            c.all_packages,
            ['neutron-common', 'neutron-plugin-ml2'])

    def test_configure_plugin(self):
        principle_interface = mock.MagicMock()
        self.patch_object(neutron_api_genericswitch.ch_utils, 'os_release')
        self.os_release.return_value = 'queens'
        c = neutron_api_genericswitch.NewtonNeutronAPIGenericSwitchCharm()
        c.configure_plugin(principle_interface)
        config_dict = {
            'neutron-api': {
                '/etc/neutron/neutron.conf': {'sections': {'DEFAULT': []}}}}
        principle_interface.configure_plugin.assert_called_once_with(
            neutron_plugin='genericswitch',
            core_plugin='neutron.plugins.ml2.plugin.Ml2Plugin',
            neutron_plugin_config='/etc/neutron/plugins/ml2/ml2_conf.ini',
            service_plugins=('router,firewall,vpnaas,metering,'
                             'neutron_lbaas.services.loadbalancer.'
                             'plugin.LoadBalancerPluginv2'),
            subordinate_configuration=config_dict)
