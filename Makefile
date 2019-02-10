RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all: ds9 onemetre-system-dome onemetre-system-tcs observatory-system-gotoserver

ds9:
	curl -s -L -O http://ds9.si.edu/download/centos7/ds9.centos7.8.0.1.tar.gz
	tar xf ds9.centos7.8.0.1.tar.gz
	mkdir -p build
	${RPMBUILD} -ba ds9.spec
	mv build/x86_64/*.rpm .
	rm -rf build ds9.centos7.8.0.1.tar.gz ds9

onemetre-system-dome:
	mkdir -p build
	${RPMBUILD} -ba onemetre-system-dome.spec
	mv build/noarch/*.rpm .
	rm -rf build

onemetre-system-tcs:
	mkdir -p build
	${RPMBUILD} -ba onemetre-system-tcs.spec
	mv build/noarch/*.rpm .
	rm -rf build

observatory-system-gotoserver:
	mkdir -p build
	${RPMBUILD} -ba observatory-system-gotoserver.spec
	mv build/noarch/*.rpm .
	rm -rf build
