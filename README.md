Getting started
===============

Generate a config ini file with switch configuration, similar to the one below:

    [ml2]
    mechanism_drivers = openvswitch,hyperv,genericswitch
    
    [genericswitch:my_switch]
    device_type = netmiko_cisco
    ip = 192.168.1.12
    port = 22
    username = admin
    password = admin


Deploying locally
=================

    cd src
    charm build

    juju deploy $PATH_TO_CHECKOUT/src/builds/neutron-api-genericswitch --resource genericswitch-ml2-config=/full/path/to/switchconfig.ini
    juju add-relation neutron-api neutron-api-genericswitch
