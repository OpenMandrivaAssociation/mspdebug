Name:		mspdebug
Version:	0.18
Release:	1
Summary:	Debugger and gdb proxy for MSP430 MCUs
Group:		Development/Other
License:	GPLv2+
URL:		http://mspdebug.sourceforge.net/
Source0:	https://downloads.sourceforge.net/project/mspdebug/mspdebug-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libusb-devel
BuildRequires:	readline-devel

%description
A a free debugger for use with MSP430 MCUs. It supports FET430UIF,
eZ430, RF2500 and TI Chronos devices. It can be used as a proxy for
gdb or as an independent debugger with support for programming,
disassembly and reverse engineering.

%prep
%setup -q

%build
# add -DDEBUG_GDB to CFLAGS for gdb debugging output
#make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"
%make

%install
#make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} INSTALL="install -p"
%makeinstall_std PREFIX=%{_prefix} LIBDIR=%{_libdir}

%files
%doc AUTHORS COPYING
%{_bindir}/mspdebug
%{_mandir}/man1/mspdebug.1*
%{_libdir}/%{name}/*.ihex
