%define svn_rev r133

%define major 0
%define libname %mklibname lomoco %{major}
%define devname %mklibname lomoco -d

Summary:	Logitech mouse control tool
Name:		lomoco
Version:	1.0
Release:	12
License:	GPLv2+
Group:		System/Configuration/Hardware
Url:		http://www.lomoco.org/
Source0:	http://www.lomoco.org/lomoco-%{svn_rev}.tar.bz2
Patch0:		lomoco-trunk-config.patch
BuildRequires:	chrpath
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	pkgconfig(libusb)

%description
Lomoco can configure vendor-specific options on Logitech USB mice (or
dual-personality mice plugged into the USB port). A number of recent devices
are supported. The program is mostly useful in setting the resolution to 800
cpi or higher on mice that boot at 400 cpi (such as the MX500, MX510, MX1000
etc.), and disabling SmartScroll or Cruise Control for those who would rather
use the two extra buttons as ordinary mouse buttons.

Supported devices:

Cordless Mouse Receiver
Cordless MouseMan Optical
Cordless Optical Mouse
Cordless TrackMan Wheel
G3 Gaming Laser Mouse
G5 Gaming Laser Mouse
MX Revolution Mouse
MX1000 Laser Cordless Mouse
MX300 Optical Mouse
MX310 Optical Mouse
MX500 Optical Mouse
MX510 Optical Mouse
MX518 Optical Mouse
MX900 Cordless Mouse
MouseMan Dual Optical
MouseMan Traveler
Optical Wheel Mouse
USB Receiver
UltraX Optical Mouse
V200 Cordless Notebook Mouse
VX Revolution Mouse
Wheel Mouse Optical
diNovo Media Desktop Receiver
iFeel Mouse

%files
%{_bindir}/lomoco
%{_sysconfdir}/lomoco.ini

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for lomoco
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with lomoco.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for lomoco
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the files needed to develop programs
linked with lomoco.

%files -n %{devname}
%doc build/doc/html/*
%{_includedir}/*
%{_libdir}/lib%{name}.so

#----------------------------------------------------------------------------

%prep
%setup -q -n lomoco-trunk
%patch0 -p1

%build
export CFLAGS="%{optflags} -fPIC"
%cmake -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir}
%make
%make doc

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_bindir}
install -m 0755 build/client/lomoco %{buildroot}%{_bindir}/lomoco
%{_bindir}/chrpath -d %{buildroot}%{_bindir}/lomoco

mkdir -p %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_prefix}%{_sysconfdir}/lomoco.ini %{buildroot}%{_sysconfdir}/lomoco.ini

