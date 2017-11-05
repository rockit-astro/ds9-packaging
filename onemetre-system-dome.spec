Name:      onemetre-system-dome
Version:   0.9.1
Release:   0
Url:       https://github.com/warwick-one-metre/
Summary:   Metapackage for the dome computer
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  onemetre-vaisala-server, onemetre-vaisala-client
Requires:  onemetre-roomalert-server, onemetre-roomalert-client
Requires:  onemetre-environment-server, onemetre-environment-client
Requires:  onemetre-dome-server, onemetre-dome-client
Requires:  onemetre-power-server, onemetre-power-client
Requires:  onemetre-operations-server, onemetre-operations-client
Requires:  onemetre-raindetector-server, onemetre-raindetector-client
Requires:  observatory-superwasp-client, observatory-tng-client, observatory-netping-client
#Requires:  onemetre-camera-client, onemetre-pipeline-client, onemetre-tel-client
Requires:  ds9

%description
Metapackage that installs dependencies for the onemetre dome computer.

%build

%files

%changelog
