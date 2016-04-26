#!/bin/bash

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

RE_HIVEX_CONFIGURE_EXTRA_FLAGS="LDFLAGS=-L/opt/local/lib CPPFLAGS=-I/opt/local/include" \
  INSTALL_DEPS=install_dependent_packages-osx-10.9.sh \
  ./_build_regxml_extractor.sh
