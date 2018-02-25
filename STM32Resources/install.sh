#!/usr/bin/env bash

if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo:"
    echo "sudo $0 $*"
    exit 1
fi

# Determine what distribution of Linux the user has
DISTRO = $(. /etc/os-release; echo $NAME)

# Install files according to Linux distribution that the user has
if [ "$DISTRO" = "Ubuntu" ]; then
    apt-get -y install build-essential git libsane:i386 ia32-libs-multiarch autoconf libusb-1.0-0-dev lib32ncurses5 libncurses5:i386 software-properties-common pkg-config cmake

elif [ "$DISTRO" = "Fedora" ]; then
    # Install necessary 32-bit compliant packages
    dnf install --skip-broken glibc.i686 arts.i686 audiofile.i686 bzip2-libs.i686 cairo.i686 cyrus-sasl-lib.i686 dbus-libs.i686 directfb.i686 esound-libs.i686 fltk.i686 freeglut.i686 gtk2.i686 hal-libs.i686 imlib.i686 lcms-libs.i686 lesstif.i686 libacl.i686 libao.i686 libattr.i686 libcap.i686 libdrm.i686 libexif.i686 libgnomecanvas.i686 libICE.i686 libieee1284.i686 libsigc++20.i686 libSM.i686 libtool-ltdl.i686 libusb.i686 libwmf.i686 libwmf-lite.i686 libX11.i686 libXau.i686 libXaw.i686 libXcomposite.i686 libXdamage.i686 libXdmcp.i686 libXext.i686 libXfixes.i686 libxkbfile.i686 libxml2.i686 libXmu.i686 libXp.i686 libXpm.i686 libXScrnSaver.i686 libxslt.i686 libXt.i686 libXtst.i686 libXv.i686 libXxf86vm.i686 lzo.i686 mesa-libGL.i686 mesa-libGLU.i686 nas-libs.i686 nss_ldap.i686 cdk.i686 openldap.i686 pam.i686 popt.i686 pulseaudio-libs.i686 sane-backends-libs-gphoto2.i686 sane-backends-libs.i686 SDL.i686 svgalib.i686 unixODBC.i686 zlib.i686 compat-expat1.i686 compat-libstdc++-33.i686 openal-soft.i686 alsa-oss-libs.i686 redhat-lsb.i686 alsa-plugins-pulseaudio.i686 alsa-plugins-oss.i686 alsa-lib.i686 nspluginwrapper.i686 libXv.i686 libXScrnSaver.i686 qt.i686 qt-x11.i686 pulseaudio-libs.i686 pulseaudio-libs-glib2.i686 alsa-plugins-pulseaudio.i686

    # Install cmake
    dnf install cmake

    # Install libusb library
    dnf install libusbx-devel-1.0.21-2.fc26.x86_64  #This is a 64 bit compliant package
    dnf install libusbx-devel-1.0.21-2.fc26.i686    #This is a 32 bit compliant package
else
    echo "Sorry, your system is not supported!"
    exit 1
fi

# Install STLink
if ! type "st-flash" > /dev/null; then
    echo "*** Installing ST Link"
    git clone https://github.com/UCSolarCarTeam/stlink.git /opt/stlink
    mkdir /opt/stlink/build
    (cd /opt/stlink/build && cmake -DCMAKE_BUILD_TYPE=Debug .. && make -j4)
    ln -s /opt/stlink/build/st-flash /usr/local/bin/st-flash
    ln -s /opt/stlink/build/st-info /usr/local/bin/st-info
    ln -s /opt/stlink/build/src/gdbserver/st-util /usr/local/bin/st-util
    if [ "$DISTRO" = "Ubuntu" ]; then
        BASH_PROFILE = "~./profile"
    elif [ "$DISTRO" = "Fedora" ]; then
        BASH_PROFILE = "~./bashrc"
    fi
    echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/opt/stlink/build" >> $BASH_PROFILE
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/stlink/build
    echo "export PATH=\$PATH:/opt/stlink/build" >> $BASH_PROFILE
    export PATH=$PATH:/opt/stlink/build
    cp ~/.bashrc /root/
else
    echo "*** ST Link already installed"
fi

# Install CubeMX2Makefile
if ! type "CubeMX2Makefile" > /dev/null; then
    echo "*** Installing CubeMX2Makefile"
    git clone https://github.com/UCSolarCarTeam/CubeMX2Makefile.git --depth 1
    mv CubeMX2Makefile /opt/CubeMX2Makefile
    echo "#!/usr/bin/env bash" >> /usr/local/bin/CubeMX2Makefile
    echo "ABS_PATH=\"\$(readlink -f \$1)\"" >> /usr/local/bin/CubeMX2Makefile
    echo "(cd /opt/CubeMX2Makefile && python CubeMX2Makefile.py \$ABS_PATH)" >> /usr/local/bin/CubeMX2Makefile
    chmod +x /usr/local/bin/CubeMX2Makefile
    if [ "$DISTRO" = "Ubuntu" ]; then
        BASH_PROFILE = "~./profile"
    elif [ "$DISTRO" = "Fedora" ]; then
        BASH_PROFILE = "~./bashrc"
    fi
    echo "export PATH=\$PATH:/opt/CubeMX2Makefile" >> $BASH_PROFILE
    export PATH=$PATH:/opt/CubeMX2Makefile
else
    echo "*** CubeMX2Makefile already installed"
fi

# Install arm compiler
if [ ! -d "/opt/gcc4mbed" ]; then
    echo "*** Installing arm compiler"
    git clone https://github.com/UCSolarCarTeam/gcc4mbed.git /opt/gcc4mbed --depth 1
    (cd /opt/gcc4mbed && \
        chmod +x linux_install && \
        sed -i '108d;109d;110d;147d' linux_install && \
        ./linux_install)
    if [ "$DISTRO" = "Ubuntu" ]; then
        BASH_PROFILE = "~./profile"
    elif [ "$DISTRO" = "Fedora" ]; then
        BASH_PROFILE = "~./bashrc"
    fi
    if ! grep "export PATH=\$PATH:/opt/gcc4mbed/gcc-arm-none-eabi/bin/" $BASH_PROFILE; then
        echo "export PATH=\$PATH:/opt/gcc4mbed/gcc-arm-none-eabi/bin/" >> $BASH_PROFILE
    fi
    export PATH=$PATH:/opt/gcc4mbed/gcc-arm-none-eabi/bin/
else
    echo "*** ARM compiler already installed"
fi

# Sourcing
if [ "$DISTRO" = "Ubuntu" ]; then
    BASH_PROFILE = "~./profile"
elif [ "$DISTRO" = "Fedora" ]; then
    BASH_PROFILE = "~./bashrc"
fi
source $BASH_PROFILE    #sourcing the appropriate profile
