Name:      onemetre-system-tcs
Version:   1.0.0
Release:   0
Url:       https://github.com/warwick-one-metre/
Summary:   Metapackage for the dome computer
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  ds9
Requires: onemetre-talon
Requires:  onemetre-telescope-server, onemetre-telescope-client
Requires:  onemetre-camera-server, onemetre-camera-client
Requires:  onemetre-pipeline-server, onemetre-pipeline-client
Requires:  onemetre-diskspace-server, onemetre-diskspace-client
Requires:  onemetre-vaisala-client, onemetre-roomalert-client, onemetre-environment-client
Requires:  onemetre-operations-client, onemetre-dome-client, onemetre-power-client
Requires:  observatory-vaisala-client, onemetre-raindetector-client
Requires:  observatory-superwasp-client, observatory-tng-client, observatory-netping-client

%description
Metapackage that installs dependencies for the onemetre tcs computer.

%build

%files

%changelog
