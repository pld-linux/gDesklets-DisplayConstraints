%define		pname	DisplayConstraints
%define		fname	displayconstraints
Summary:	This sensor allows a user to set maximum constraints on a display
Summary(pl):	Ten czujnik pozwala na ustawienie maksymalnych rozmiarów wy¶wietlacza
Name:		gDesklets-%{pname}
Version:	0.1.0
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{fname}-%{version}.tar.bz2
# Source0-md5:	a36a563797dfd8c8f112323300661d02
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=61
BuildRequires:	python >= 1:2.3
BuildRequires:	python-pygtk-gtk >= 1.99.18
Requires:	gDesklets
%pyrequires_eq	python-libs
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sensorsdir	%{_datadir}/gdesklets/Sensors

%description
This sensor allows a user to set maximum constraints on a display.

%description -l pl
Ten czujnik pozwala na ustawienie maksymalnych rozmiarów wy¶wietlacza.

%prep
%setup -q -n %{pname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sensorsdir}

./Install_%{pname}_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{pname}/README
%{_sensorsdir}/*
