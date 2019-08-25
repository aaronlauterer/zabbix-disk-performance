#!/usr/bin/python
import os
import json
import re

if __name__ == "__main__":
    # Iterate over all block devices, but ignore them if they are in the
    # skippable set
    # skip /dev/sda1 in favour of /dev/sda
    # skip: sda1/nvme0n1p1/xvdg1  , keep: sda/nvme0n1/xvdg
    skippable = (
        r"^(sr|loop|ram|fd)",
        r"^(sd\w|hd\w|nvme\d+n\d+p|zd\d+p|xvd\w|vd\w)\d+$",
    )
    devices = (
        device
        for device in os.listdir("/sys/class/block")
        if not any(re.search(ignore, device) for ignore in skippable)
    )
    data = [{"{#DEVICENAME}": device} for device in devices]
    print(json.dumps({"data": data}, indent=4))
