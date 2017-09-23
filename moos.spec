Name:     moos
Version:  10.0.2.a
Release:  1
Summary:  Mission Oriented Operating Suite
License:  GPLv2+
URL:      http://www.robots.ox.ac.uk/~mobile/MOOS/wiki/pmwiki.php/Main/HomePage
Source0:  https://github.com/themoos/core-moos/archive/%{version}-release.tar.gz
Patch0:   add-install-config.patch
Patch1:   add-shared-library.patch
Patch2:   install-versioned-libs.patch
Patch3:   add-gnuinstalldirs.patch
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires: cmake, gcc-c++, quilt

%description
Light, fast, cross-platform middle-ware for robotics. CoreMOOS is the most
fundamental layer, providing a very robust network based communications
architecture (two libraries and a lightweight communications hub called
MOOSDB) which for very little effort lets you build applications which
communicate with each other.

%prep
%autosetup -n core-moos-%{version}-release -S quilt

%build
%cmake
%make_build

%install
%make_install


%files
%{_bindir}/MOOSDB
%{_bindir}/ktm
%{_bindir}/mqos
%{_bindir}/mtm
%{_bindir}/umm


%changelog
* Fri Sep 22 2017 Kyle Fazzari <kyrofa@ubuntu.com> - 10.0.2.a-1
- Initial version of the package


%package devel
Summary:  Mission Oriented Operating Suite - development files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Light, fast, cross-platform middle-ware for robotics. CoreMOOS is the most
fundamental layer, providing a very robust network based communications
architecture (two libraries and a lightweight communications hub called
MOOSDB) which for very little effort lets you build applications which
communicate with each other.

%files devel
%{_includedir}/MOOS
%{_libdir}/cmake
%{_libdir}/*.so


%package libs
Summary:  Mission Oriented Operating Suite - shared libraries

%description libs
Light, fast, cross-platform middle-ware for robotics. CoreMOOS is the most
fundamental layer, providing a very robust network based communications
architecture (two libraries and a lightweight communications hub called
MOOSDB) which for very little effort lets you build applications which
communicate with each other.

%files libs
%{_libdir}/*.so.*

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig
