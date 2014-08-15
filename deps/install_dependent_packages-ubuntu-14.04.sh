#!/bin/bash

set -e
set -x

#Assume Ubuntu
#TODO Add a check

sudo apt-get update

#Below the 'automake' line are "devel" packages, but we'll break that out after the Hivex revisions are upstream.
sudo apt-get install \
  automake  \
  g++ \
  libssl-dev \
  libtool \
  libxml2-dev \
  libxml2-utils \
  python-dev \
  python3-hivex \
  sqlite3 \
  autoconf \
  autopoint \
  gettext \
  libtool \
  ocaml \
  python-dateutil
