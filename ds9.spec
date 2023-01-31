Name:      ds9
Version:   8.4.1
Release:   0
Url:       http://ds9.si.edu/site/Home.html
Summary:   Custom packaging of CentOS ds9 binary from the official website.
Source:    https://ds9.si.edu/download/centos8/ds9.centos8.%{version}.tar.gz
License:   GPL-3.0
Group:     Unspecified
BuildArch: x86_64

%description

%prep
%setup -q -c

%build

mkdir -p %{buildroot}%{_bindir}
%{__install} ds9 %{buildroot}%{_bindir}

%files
%defattr(0755,root,root,-)
%{_bindir}/ds9

%changelog
