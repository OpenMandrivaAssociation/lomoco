%define name	lomoco
%define version	1.0
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Logitech mouse control tool
Version: 	%{version}
Release: 	%{release}

Source:		http://lomoco.linux-gamers.net/files/%{name}-%{version}.tar.bz2
URL:		http://lomoco.linux-gamers.net/
License:	GPL
Group:		System/Configuration/Hardware
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Lomoco can configure vendor-specific options on Logitech USB mice (or
dual-personality mice plugged into the USB port). A number of recent devices
are supported. The program is mostly useful in setting the resolution to 800
cpi or higher on mice that boot at 400 cpi (such as the MX500, MX510, MX1000
etc.), and disabling SmartScroll or Cruise Control for those who would rather
use the two extra buttons as ordinary mouse buttons.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x
%make
make udev-rules
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p %buildroot/%{_lib}/udev
cp udev/udev.lomoco %buildroot/%{_lib}/udev/lomoco
mkdir -p %buildroot/%_sysconfdir/udev/rules.d
cp udev/lomoco.rules %buildroot/%_sysconfdir/udev/rules.d/40-lomoco.rules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%name
%{_mandir}/man1/*
/%{_lib}/udev/lomoco
%{_sysconfdir}/udev/rules.d/*.rules
