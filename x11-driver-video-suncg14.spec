ExclusiveArch:	sparc sparc64
Name: x11-driver-video-suncg14
Version: 1.1.1
Release: %mkrel 4
Summary: X.org driver for sun cg14 Cards
Group: System/X11
URL: https://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-suncg14-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-suncg14 is the X.org driver for sun cg14 Cards.

%prep
%setup -q -n xf86-video-suncg14-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/suncg14_drv.la
%{_libdir}/xorg/modules/drivers/suncg14_drv.so
%{_mandir}/man4/suncg14.*
