Summary:	Debugger and gdb proxy for MSP430 MCUs
Name:		mspdebug
Version:	0.23
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		https://mspdebug.sourceforge.net/
Source0:	https://downloads.sourceforge.net/project/mspdebug/mspdebug-%{version}.tar.gz
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(libusb)

%description
A a free debugger for use with MSP430 MCUs. It supports FET430UIF,
eZ430, RF2500 and TI Chronos devices. It can be used as a proxy for
gdb or as an independent debugger with support for programming,
disassembly and reverse engineering.

%files
%doc AUTHORS COPYING
%{_bindir}/mspdebug
%{_mandir}/man1/mspdebug.1*
%{_libdir}/%{name}/*.ihex

#----------------------------------------------------------------------------

%prep
%setup -q

%build
# add -DDEBUG_GDB to CFLAGS for gdb debugging output
#make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"
%make GCC_CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall_std PREFIX=%{_prefix} LIBDIR=%{_libdir}

