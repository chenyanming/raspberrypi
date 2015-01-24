#!/bin/bash
mount -t nfs -o intr,nolock,rsize=1024,wsize=1024 192.168.0.101:/home/ming/Raspberry/nfs /mnt
