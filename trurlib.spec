Summary:	C library with some useful data structures and routines
Summary(pl.UTF-8):   Biblioteka w C z użytecznymi strukturami danych i procedurami
Name:		trurlib
Version:	0.44.0
Release:	0.1
License:	LGPL
Group:		Libraries
# Source taken from poldek-0.18.6/trurlib
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	eb4cf29b05891711f6b9227ace34cc31
Patch0:		%{name}-POSIX.patch
Patch1:		%{name}-missing_includes.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TRURL library contains some useful data structures and routines:
- dynamic array
- linked list (both with Perl-like interface)
- hash table
- some string functions
- xmalloc()s

and some other stuff.

%description -l pl.UTF-8
Biblioteka TRURL zawiera trochę użytecznych struktur danych i
procedur:
- dynamiczne tablice
- listy (z interfejsem perlopodobnym)
- tablice mieszające
- funkcje do stringów
- xmalloc() itp.

i inne.

%package devel
Summary:	trurlib headers and documentation
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja trurlib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Trurlib headers and documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja trurlib.

%package static
Summary:	Static trurl library
Summary(pl.UTF-8):   Statyczna biblioteka trurl
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static trurl library.

%description static -l pl.UTF-8
Statyczna biblioteka trurl.

%if %{_os} == linux
%define _libglob %attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%else
%define _libglob %attr(755,root,root) %{_libdir}/lib*.so.*
%endif

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_libglob}

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/trurl

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
