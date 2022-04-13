Name:      softflowd
Summary:   Network traffic analyser capable of Cisco NetFlow data export
Version:   1.0.0
Release:   1%{?dist}
Group:     System/Utilities
License:   BSD
URL:       http://www.mindrot.org/softflowd.html
Vendor:    mindrot.org

Source0: https://github.com/irino/softflowd/archive/refs/tags/softflowd-%{version}.tar.gz
Source1: %{name}.service
Source2: %{name}

BuildArch:     x86_64
BuildRequires: gcc >= 8.3
BuildRequires: make >= 4.2.1


%description
softflowd is a software implementation of a flow-based network traffic
monitor.  softflowd reads network traffic and gathers information about
active traffic flows.  A "traffic flow" is communication between two IP
addresses or (if the overlying protocol is TCP or UDP) address/port tuples.
The intended use of softflowd is as a software implementation of Cisco’s
NetFlow traffic account system.  softflowd supports data export using
versions 1, 5 or 9 of the NetFlow protocol.

%prep
%setup

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%{__install} -d -m 0755 %{buildroot}%{_unitdir}
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig/
%{__install} -m 0600 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%files
%license LICENSE
%doc LICENSE AUTHORS README NEWS ChangeLog TODO
%defattr(-, root, root,-)
%{_sbindir}/%{name}
#/usr/sbin/*
#/usr/share/man/*
%{_unitdir}/%{name}.service
%{_sysconfdir}/sysconfig/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Apr 12 2022 Edouard Camoin <edouard.camoin@gmail.com> 1.0.0
  - Initial spec file for softflowd

