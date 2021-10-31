QEMU Launcher
=============

QEMU Launcher is a script designed to simplify QEMU virtual machine management.  It is licensed under the GPLv3.  It not available under a prior or future version of the GPL.

Prerequisites
-------------

Command Line Operation

* qemu
* spice (qemu may pull this in)
* tigervnc (for vncviewer)
* parted (for disk partition listings)


Operation
---------

### System options:

      --nokvm|--nohvf       Disable KVM/HVF accelleration
      --cpu <cpu>           Specify the CPU to emulate
      --cores               Specify number of cores (default = [cores+1]/2)
      --efi <bits>          Boot using <bits>-bit UEFI instead of BIOS
      --win2k               Enable Win2K hack (solves disk full bug, slows IDE)
      --legacy              Use legacy hardware*
      --ram <MiB>           Specify RAM available to VM
      --sound               Enable sound
      --term <term-bin>     Launch QEMU in <term-bin> in background
      --mouse               Use USB mouse instead of tablet device
      --gpu <card>          Specify the GPU_CARD device to use

      *i440FX + PIIX + Cirrus VGA + AMD PCNet NIC + drives on IDE (no VirtIO)

### Drive options:

      --drive <file>:<floppy|ide|scsi|ahci|virtio>

### Network options:

      --forward <port:port> Forward host's <port> to guest's <port>
      --pcnet               Use an AMD PCNet NIC instead of VirtIO
      --ne2k                Use an NE2000-compatible NIC instead of VirtIO

### Display options:

      The default is to start a VNC host and launch a VNC viewer.

      --gtk             Use a GTK window (QEMU default)
      --qxl <port>      Use QXL/SPICE instead of VNC
      --daemon          Don't launch SPICE/vncviewer directly
      --xport           Specify X11 listening port number

### Utilties:

      -h|--help         This help text.

