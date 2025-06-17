RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)/build" \
        --define "_build_id_links none" \
        --undefine=_disable_source_fetch

ds9:
	mkdir -p build
	${RPMBUILD} -ba ds9.spec
	mv build/*/*.rpm .
	rm -rf build
