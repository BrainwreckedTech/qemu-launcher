QEMU Launcher
=============

QEMU Launcher is a script designed to simplify QEMU virtual machine management.

Invoking it can be as short and sweet as:

    sudo qcl --drive /path/to/drive.img:virtio

...which will allocate 4 threads and 4 GiB of RAM on a PC with a 16-thread CPU
and 16 GiB of RAM.  Automated allocations aren't a simple 25% of your resources,
but will scale with the resources available.

License
-------

QEMU Launcher is licensed under the GPLv3.  It is not available under a prior
or future version of the GPL.

Prerequisites
-------------

Command Line Operation

* qemu
* spice (qemu may pull this in)
* tigervnc (for vncviewer)

Operation
---------

### System options

    --nokvm|--nohvf          Disable KVM/HVF accelleration
    --efi <bits>             Boot using <bits>-bit UEFI instead of BIOS
    --pcfrom <year>          Emulate hardware from <year>
    --ram <MiB>              Specify RAM available to VM
    --sound                  Enable sound
    --xport <1..99>          Port offset for VNC, SPICE, and telnet
    --monitor <monitor>      Specify how qemu-monitor is accessed

       <monitor> is one of the following:

       stdio     (default)   Start monitor in current console
       telnet                Start monitor at telnet:localhost:61<port>
       unix                  Start monitor as a unix socket
       <bin>                 Start monitor in a new console process

       If <monitor> is not stdio, telnet, or unix, then the argument
       is assumed to be the binary of a terminal emulator.

### CPU options:

    --cores <n>              Emulate <n> cores.  Default is ([cores+2]/3)
    --cpu <cpu>              Emulate <cpu> model.  Default is host.

        <cpu> is one of the following:

        pentium             opteron            core-gen1|nehalem
        pentium2            core2duo           westmere
        pentium3            penryn             core-gen2|sandybridge
        pentium4|coreduo    atom64|denverton   core-gen3|ivybridge
        atom32|n270                            core-gen4|haswell
                                               core-gen5|broadwell

### Drive options:

    --drive <file>:<interface>

        <interface> is one of floppy, ide, scsi, ahci, or virtio

        If <interface> is not specified then qcl will guess based on the file
        extension and machine type.

        Note that ahci cannot be combined with type=pc.  There is no AHCI
        controller for the i440FX chipset.  PIIX provides IDE (ATA) only.

        SATA is only a connector type --  drives still used the ATA (IDE) protocol
        until Intel released AHCI in 2002.

### Pointing device options:

    QCL will use a PS/2 mouse up until --pcfrom 1999, and usb-tablet with
    --pcfrom 2000 and later.  VirtIO setups will use virtio-tablet-pci.

    --mouse <qemu-pointer>

        <qemu-pointer> can be anything QEMU accepts, plus "PS/2"
        Common pointers relevant to QCL are:

           ps/2               The standard PS/2 QEMU normally presents the guest
           usb-mouse          Standard USB mouse
           usb-tablet         Standard USB tablet device
           usb-wacom-tablet   QEMU PenPartner Tablet
           vmmouse            ISA bus VM mouse

        Additionally, there are VirtIO devices

           virtio-mouse-pci    Mouse device utilizing VirtIO
           virtio-tablet-pci   USB tablet device utilizing VirtIO

### GPU options

    QCL uses cirrus-vga up to --pcfrom 2001 and VGA from --pcfrom 2002 forward

    --gpu <qemu-gpu>

        <qemu-gpu> can be anything QEMU accepts.
        Common GPUs relevant to QCL are:

            cirrus[-vga]       Cirrus Logic GD-5446
            rage128pro         ATI Rage 128 Pro
            radeon7000         ATI Radeon 7000
            VGA                Standard VESA VGA device
            vmware[-svga]      VMWare SVGA device

### Network options:

    --forward <port:port> Forward host's <port> to guest's <port>

    --nic <qemu-nic>

        <qemu-nic> can be one of the following

            e1000              Intel Gigabit e1000-82540em
            intel              An alias for e1000
            pcnet              AMD PCnet Fast Ethernet Card
            ne2k               An NE2000-compatible Ethernet Card
            tulip              A DEC 21x4x-compatible Ethernet Card
            realtek            An alias for rtl8139
            rtl8139            Realtek 8139 Ethernet Card

    --vtap <mac-address>  Use macvtap with <mac-address>

        <mac-address> can be set to 'random' if you want a random MAC
        address or just don't want to be bothered choosing an address.

### Display options:

    The default is to start a VNC host and launch a VNC viewer.

    --gtk                    Use a GTK window (QEMU default)
    --qxl                    Use QXL/SPICE instead of VNC
    --daemon                 Don't launch SPICE/vncviewer directly
