Name:      ds9
Version:   8.5b1
Release:   0
Url:       http://ds9.si.edu/site/Home.html
Summary:   Custom packaging of CentOS ds9 binary from the official website.
License:   GPL-3.0
Group:     Unspecified
BuildArch: x86_64 aarch64

%ifarch aarch64
Source:    https://ds9.si.edu/download/fedora36arm64/ds9.fedora36arm64.%{version}.tar.gz
%else
Source:    https://ds9.si.edu/download/centos8/ds9.centos8.%{version}.tar.gz
%endif

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
