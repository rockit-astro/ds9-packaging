Name:      ds9
Version:   7.5
Release:   0
Url:       http://ds9.si.edu/site/Home.html
Summary:   Custom packaging of CentOS ds9 binary from the official website.
License:   GPL-3.0
Group:     Unspecified
BuildArch: x86_64

%description
Custom packaging of CentOS ds9 binary from the official website.

%build

mkdir -p %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/ds9 %{buildroot}%{_bindir}

%files
%defattr(0755,root,root,-)
%{_bindir}/ds9

%changelog
