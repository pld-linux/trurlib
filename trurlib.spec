Summary:	Some useful data structures and routines
Name:		trurlib
Version:	0.42
Release:	1
License:	LGPL
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root-%(id -u -n)

%description
Library contains some useful data structures and routines:
dynamic array and linked list with Perl-like interface, 
hash table, some string functions, xmalloc()s
and other n stuff.
 
%package	devel
Summary:	Static library and header files of trurlib
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Static library and header files of trurlib

%prep 
%setup -q 

%build
CFLAGS="$RPM_OPT_FLAGS -fomit-frame-pointer -DNDEBUG"
make static modules=on CFLAGS="$CFLAGS"
make shared modules=on without_dbhash=1 CFLAGS="$CFLAGS"
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}
make install DESTDIR=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
%attr(644,root,root) %{_libdir}/lib*.so
%{_includedir}/trurl

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
