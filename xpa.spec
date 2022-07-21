Name:      xpa
Version:   2.1.20
Release:   0
Url:       http://ds9.si.edu/site/Home.html
Summary:   Custom packaging of CentOS ds9 binary from the official website.
Source:    https://ds9.si.edu/download/centos8/xpa.centos8.2.1.20.tar.gz 
License:   GPL-3.0
Group:     Unspecified
BuildArch: x86_64

%description

%prep
%setup -q -c

%build

mkdir -p %{buildroot}%{_bindir}
%{__install} xpa* %{buildroot}%{_bindir}

%files
%defattr(0755,root,root,-)
%{_bindir}/xpa*

%changelog
