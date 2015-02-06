%define name	pxmutils
%define version	0.7.0
%define release 8

%define major	3
%define libname %mklibname %name %major

%define __libtoolize /bin/true

Name: 	 	%{name}
Summary: 	A library that's used by the polyxmass framework
Version: 	%{version}
Release: 	%{release}

Source:		lib%{name}-%{version}.tar.bz2
URL:		http://polyxmass.org/libpxmutils
License:	GPL
Group:		Sciences/Chemistry
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
%makeinstall
rm -fr %{buildroot}/%{_docdir}/lib%{name}

%find_lang lib%name


%files -n %{libname} -f lib%{name}.lang
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING NEWS README TODO
%{_includedir}/lib%name
%{_mandir}/man1/*
%{_libdir}/*.so
%{_libdir}/*.a
/usr/lib/pkgconfig/*.pc



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.7.0-7mdv2010.0
+ Revision: 433735
- rebuild
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7.0-4mdv2009.0
+ Revision: 259378
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7.0-3mdv2009.0
+ Revision: 247249
- rebuild
- fix summary-ended-with-dot

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.7.0-1mdv2008.1
+ Revision: 136445
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - adjust file list for x86_64
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import pxmutils


* Mon Feb 16 2004 Austin Acton <austin@mandrake.org> 0.7.0-1mdk
- 0.7.0
- major 3
- configure 2.5
- libtoolize

* Tue Dec 30 2003 Franck Villaume <fvill@freesurf.fr> 0.6.0-2mdk
- delete pkgconfig BuildRequires
- add glib2-devel BuildRequires

* Sun Oct 12 2003 Austin Acton <aacton@yorku.ca> 0.6.0-1mdk
- initial package
