%define svn_rev r133

%define libname %mklibname lomoco 0
%define libnamed %mklibname lomoco -d

Name:           lomoco
Version:        1.0
Release:        %mkrel 10
Summary:        Logitech mouse control tool
License:        GPL
Group:          System/Configuration/Hardware
URL:            http://www.lomoco.org/
Source0:        http://www.lomoco.org/lomoco-%{svn_rev}.tar.bz2
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libusb-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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

%package -n %{libname}
Summary:        Main library for lomoco 
Group:          System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with lomoco.

%package -n %{libnamed}
Summary:        Development files for lomoco
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Obsoletes:      %{mklibname lomoco 0 -d} < %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{libnamed}
This package contains the files needed to develop programs 
linked with lomoco.

%prep
%setup -q -n lomoco-trunk
%{__rm} -r build

%build
export CFLAGS="%{optflags} -fPIC"
%{cmake} -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir}
%{make}
%{make} doc
                                                        
%install
%{__rm} -rf %{buildroot}

cd build
%{makeinstall_std}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -a client/lomoco %{buildroot}%{_bindir}/lomoco
%{_bindir}/chrpath -d %{buildroot}%{_bindir}/lomoco
cd ..

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/lomoco
%{_usr}/%{_sysconfdir}/lomoco.ini

%files -n %{libname}
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_libdir}/*.so.*

%files -n %{libnamed}
%defattr(0644,root,root,0755)
%doc build/doc/html/*
%{_includedir}/*
%attr(0755,root,root) %{_libdir}/*.so


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-10mdv2011.0
+ Revision: 620255
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.0-9mdv2010.0
+ Revision: 433629
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.0-7mdv2009.0
+ Revision: 251399
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Feb 08 2008 David Walluck <walluck@mandriva.org> 1.0-5mdv2008.1
+ Revision: 164318
- update URL
- remove old source tarball

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 22 2007 David Walluck <walluck@mandriva.org> 1.0-4mdv2008.1
+ Revision: 101271
- update to SVN 133
- new lib policy

* Sun Jul 22 2007 David Walluck <walluck@mandriva.org> 1.0-3mdv2008.0
+ Revision: 54386
- BuildRequires: cmake
- SVN r131
- Import lomoco



* Sun Sep 03 2006 David Walluck <walluck@mandriva.org> 1.0-2mdv2007.0
- rebuild
- use /%%{_lib}/udev not /lib/udev

* Wed Mar 1 2006 Austin Acton <austin@mandriva.org> 1.0-1mdk
- initial package
