Name:	qucs	
Version: 0.0.19S	
Release:	1%{?dist}
Summary:	Qucs-S is unified GUI for SPICe and non-SPICE circuit simulators

Group:		Education
License:	GPL
URL:		https://ra3xdh.github.io/
Source0:	https://github.com/ra3xdh/qucs/releases/download/0.0.19S/qucs-0.0.19S.tar.gz

BuildRequires:	gcc, gcc-c++, qt, qt-devel, cmake
Requires:	qt

%description
Qucs-S provides an unified GUI, circuit capture, and component libraries to launch SPICE circuit simulators like Ngspice, Xyce, and SpiceOpus. It also supports non-SPICE simulators like Qucsator.

%prep
%setup -q


%build
cmake -DWITH_SPICE=ON -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?_smp_mflags}


%install
%make_install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(0755,root,root) %{_bindir}/qucs-s
%attr(0755,root,root) %{_bindir}/qucs-sfilter
%attr(0755,root,root) %{_bindir}/qucs-sactivefilter
%attr(0755,root,root) %{_bindir}/qucs-slib

%attr(0644,root,root) %{_datadir}/qucs-s
%attr(0644,root,root) %{_datadir}/applications
%attr(0644,root,root) %{_datadir}/icons
%doc %{_datadir}/man


%changelog

* Tue Oct 17 2017 Vadim Kuznetsov <ra3xdh@gmail.com>
- First version of SPEC

