Introduction
============

This is the Juju charm for [openstack/networking-generic-switch](https://git.openstack.org/cgit/openstack/networking-generic-switch).


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

`[genericswitch]` blocks should follow the syntax described in [networking-generic-switch documentation](https://git.openstack.org/cgit/openstack/networking-generic-switch/tree/README.rst)


Limitations
===========

Since neutron-api-genericswitch is not part of Ubuntu Cloud Archive, the package has to be built
manually. Build instructions exist in a [manufacturer's specific extension](https://bitbucket.org/kci1/openstack-networking-generic-switch-fastpath) of generic switch.


Deploying locally
=================

    cd src
    charm build

    juju deploy $PATH_TO_CHECKOUT/src/builds/neutron-api-genericswitch \
        --resource genericswitch-ml2-config=/full/path/to/switchconfig.ini \
        --resource package=/full/path/to/neutron-api-genericswitch.deb
        
    juju add-relation neutron-api neutron-api-genericswitch
