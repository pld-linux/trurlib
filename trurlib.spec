Summary:	C library with some useful data structures and routines
Name:		trurlib
Version:	0.43
Release:	1
License:	LGPL
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root-%(id -u -n)

%description
TRURL library contains some useful data structures and routines:
- dynamic array 
- linked list 
 (both with Perl-like interface)
- hash table
- some string functions
- xmalloc()s 

and some other n stuff.

%package	devel
Summary:	trurlib headers and documentation
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
trurlib headers and documentation

%package	static
Summary:	Static trurl library 
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
Static trurl library

%prep 
%setup -q 

%build
%configure --enable-shared
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.la
%attr(644,root,root) %{_libdir}/lib*.so
%{_includedir}/trurl

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
