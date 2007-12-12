%define name	pxmutils
%define version	0.7.0
%define release 1mdk

%define major	3
%define libname %mklibname %name %major

%define __libtoolize /bin/true

Name: 	 	%{name}
Summary: 	A library that's used by the polyxmass framework.
Version: 	%{version}
Release: 	%{release}

Source:		lib%{name}-%{version}.tar.bz2
URL:		http://polyxmass.org/libpxmutils
License:	GPL
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libxml2-devel gettext glib2-devel

%description
%{name} is a handy library of helper functions. This C library is
designed to provide a number of useful functionalities which the
programs in the polyxmass(TM) mass spectrometry framework require.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
Provides:	%name
Obsoletes:	%name = %version-%release

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release} 
Obsoletes: 	%name-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n lib%{name}-%{version}

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -fr $RPM_BUILD_ROOT/%{_docdir}/lib%{name}

%find_lang lib%name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname} -f lib%{name}.lang
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING NEWS README TODO
%{_includedir}/lib%name
%{_mandir}/man1/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

