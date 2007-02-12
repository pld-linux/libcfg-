#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	Command line and configuration file parsing library
Summary(pl.UTF-8):   Biblioteka do analizy linii poleceń i plików konfiguracyjnych
Name:		libcfg+
Version:	0.6.2
Release:	2
License:	GPL
Group:		Libraries
#Source0Download: http://platon.sk/projects/release_list_page.php?project_id=3
Source0:	http://platon.sk/upload/_projects/00003/%{name}-%{version}.tar.gz
# Source0-md5:	e117a2d054c5f5831fdb5ed27c26d767
Patch0:		%{name}-make.patch
URL:		http://platon.sk/projects/libcfg+/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcfg+ is a C library that features multi- command line and
configuration file parsing. It is possible to set up various special
properties such as quoting characters, deliminator strings, file
comment prefixes, multi-line postfixes, and more. It supports many
data types such as booleans, integers, decimal numbers, strings with
many additional data type flags (such as multiple values for a single
option).

%description -l pl.UTF-8
libcfg+ to biblioteka w C do analizy linii poleceń i plików
konfiguracyjnych. Można ustawiać różne specjalne własności, takie jak
znaki cytowania, łańcuch ograniczające, prefiksy komentarzy w plikach,
wieloliniowe postfiksy i inne. Biblioteka obsługuje wiele typów
danych, takich jak logiczne, liczby całkowite, liczby dziesiętne,
łańcuchy z wieloma dodatkowymi flagami typów (takimi jak wiele
wartości dla jednej opcji).

%package devel
Summary:	Header files for libcfg+ library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libcfg+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcfg+ library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcfg+.

%package static
Summary:	Static libcfg+ library
Summary(pl.UTF-8):   Statyczna biblioteka libcfg+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcfg+ library.

%description static -l pl.UTF-8
Statyczna biblioteka libcfg+.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%{__autoheader}
CFLAGS="%{rpmcflags} -fPIC"
%configure \
	%{!?with_static_libs:--enable-static=no}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/platon
%{_includedir}/cfg*.h
%{_mandir}/man3/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
