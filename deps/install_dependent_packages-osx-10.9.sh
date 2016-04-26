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

if [ ! -x `which port` ]; then
  echo "Error: \`port' not found. Download and install MacPorts." >&2
  exit 1
fi

set -e
set -x

sudo port selfupdate
sudo port install \
  autoconf \
  automake \
  getopt \
  libtool \
  libxml2 \
  ocaml \
  pkgconfig \
  python33

#Thanks to Jim Meyering for the dirlist tip for dealing with PKG_CHECK_MODULES not being found.
PKGM4=$(find /opt/local /usr -name 'pkg.m4' | head -n1 2>/dev/null)
if [ ! -r "$PKGM4" ]; then
  echo "Error: pkg.m4 file not found; hivex will fail to build." >&2
  exit 1
fi
ACLOCALDIRLIST=$(aclocal --print-ac-dir)/dirlist
if [ ! -r "$ACLOCALDIRLIST" -o ! $(grep "$(dirname "$PKGM4")" "$ACLOCALDIRLIST" | wc -l) -gt 0 ]; then
  echo "Note: Augmenting aclocal path with m4 directories." >&2
  sudo bash -c "printf '%s/share/aclocal\n' /opt/local /usr >>$(aclocal --print-ac-dir)/dirlist"
fi
test $(cat $(aclocal --print-ac-dir)/dirlist | xargs -I YY find YY -type f 2>/dev/null | grep 'pkg.m4' | wc -l) -gt 0 ;
echo Done.
