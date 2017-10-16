Name:	qucs	
Version: 0.0.19S	
Release:	1%{?dist}
Summary:	Qucs-S is unified GUI for SPICe and non-SPICE circuit simulators

Group:		Education
License:	GPL
URL:		https://ra3xdh.github.io/
Source0:	https://github.com/ra3xdh/qucs/releases/download/0.0.19S/qucs-0.0.19S.tar.gz

BuildRequires:	gcc, gcc-c++, qt, qt-devel
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



%changelog

