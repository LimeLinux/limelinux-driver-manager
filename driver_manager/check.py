import os
import sys
import glob

devices = "/sys/bus/pci/devices/"
driver304 = open("/usr/share/limelinux-dm/data/304.lst").read().split("\n")
driver340 = open("/usr/share/limelinux-dm/data/340.lst").read().split("\n")
driver_current = open("/usr/share/limelinux-dm/data/current.lst").read().split("\n")


class DriverChecker(object):

    def __init__ (self):
        super().__init__()

        self.driver_packages = {
            "vbox": "module-virtualbox",
            "intel": "xorg-video-intel",
            "radeon": "xorg-video-radeon",
            "amdgpu": ("module-amdgpu", "xorg-video-amdgpu"),
            "nvidia-current": ("module-nvidia-current", "xorg-video-nouveau"),
            "nvidia304": ("module-nvidia304", "xorg-video-nouveau"),
            "nvidia340": ("module-nvidia340", "xorg-video-nouveau")
        }

    def driver_check(self):
        graphics_list = {}
        for boot_vga_file in glob.glob("{}/*/boot_vga".format(devices)):
            device_path = os.path.dirname(boot_vga_file)
            boot_vga = int(open(boot_vga_file).read().strip())
            vendor = open(os.path.join(device_path, "vendor")).read().strip()
            device = open(os.path.join(device_path, "device")).read().strip()
            #device_id = vendor[2:] + device[2:]

            # nvidia
            if vendor[2:] == "10de":
                if device[2:] in driver304:
                    graphics_list["nvidia"] = (self.driver_packages["nvidia304"], boot_vga)

                elif device[2:] in driver340:
                    graphics_list["nvidia"] = (self.driver_packages["nvidia340"], boot_vga)

                elif device[2:] in driver_current:
                    graphics_list["nvidia"] = (self.driver_packages["nvidia-current"], boot_vga)

            # intel
            if vendor[2:] == "8086":
                graphics_list["intel"] = (self.driver_packages["intel"], boot_vga)

            # virtualbox
            if vendor[2:] == "80ee":
                graphics_list["vbox"] = ("", boot_vga)

            # amdgpu

        return graphics_list

asd = DriverChecker()
print(asd.driver_check())