Summary:	C library with some useful data structures and routines
Summary(pl):	Biblioteka w C z u�ytecznymi strukturami danych i procedurami
Name:		trurlib
Version:	0.43.6
Release:	3
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.pld.org.pl/software/trurlib/%{name}-%{version}.tar.gz
# Source0-md5:	1722811fef166550220fe6cde211fada
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

%description -l pl
Biblioteka TRURL zawiera troch� u�ytecznych struktur danych i
procedur:
- dynamiczne tablice
- listy (z interfejsem perlopodobnym)
- tablice mieszaj�ce
- funkcje do string�w
- xmalloc() itp.

i inne.

%package devel
Summary:	trurlib headers and documentation
Summary(pl):	Pliki nag��wkowe i dokumentacja trurlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Trurlib headers and documentation.

%description devel -l pl
Pliki nag��wkowe i dokumentacja trurlib.

%package static
Summary:	Static trurl library
Summary(pl):	Statyczna biblioteka trurl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static trurl library.

%description static -l pl
Statyczna biblioteka trurl.

%prep
%setup -q

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/trurl

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
