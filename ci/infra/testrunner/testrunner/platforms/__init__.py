from testrunner.platforms.openstack import Openstack
from testrunner.platforms.platform import Platform
from testrunner.platforms.vmware import VMware

def get_platform(conf, platform):
    if platform.lower() == "openstack":
        platform = Openstack(conf)
    elif platform.lower() == "vmware":
        platform = VMware(conf)
    elif platform.lower() == "libvirt":
         platform = Libvirt(conf) 
    elif platform.lower() == "bare-metal":
        raise Exception("bare-metal is not available")
    else:
        raise Exception("Platform Error: {} is not recognized".format(platform))

    return platform
