Name:     moos
Version:  10.0.2.a
Release:  1%{?dist}
Summary:  Mission Oriented Operating Suite

License:  GPLv2+
URL:      http://www.robots.ox.ac.uk/~mobile/MOOS/wiki/pmwiki.php/Main/HomePage
Source0:  https://github.com/themoos/core-moos/archive/%{version}-release/core-moos-%{version}-release.tar.gz

Patch0:   add-install-config.patch
Patch1:   add-shared-library.patch
Patch2:   install-versioned-libs.patch
Patch3:   add-gnuinstalldirs.patch

BuildRequires: cmake, gcc-c++, quilt
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Light, fast, cross-platform middle-ware for robotics. CoreMOOS is the most
fundamental layer, providing a very robust network based communications
architecture (two libraries and a lightweight communications hub called
MOOSDB) which for very little effort lets you build applications which
communicate with each other.


%package devel
Summary:  Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for developing applications that use %{name}.


%package libs
Summary:  Libraries for %{name}

%description libs
Libraries for running %{name} applications.


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

%files devel
%{_includedir}/MOOS/
%{_libdir}/cmake/MOOS/
%{_libdir}/*.so

%files libs
%license Core/GPLCore.txt
%{_libdir}/*.so.*

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig


%changelog
* Fri Sep 22 2017 Kyle Fazzari <kyrofa@ubuntu.com> - 10.0.2.a-1
- Initial version of the package
