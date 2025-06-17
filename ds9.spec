Name:      ds9
Version:   8.6
Release:   1%{dist}
Url:       http://ds9.si.edu/site/Home.html
Summary:   Custom packaging of CentOS ds9 binary from the official website.
License:   GPL-3.0
Group:     Unspecified
BuildArch: x86_64 aarch64

%ifarch aarch64
Source:    https://ds9.si.edu/download/centos9arm64/ds9.centos9arm64.%{version}.tar.gz
%else
Source:    https://ds9.si.edu/download/centos9x86/ds9.centos9x86.%{version}.tar.gz
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
