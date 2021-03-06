#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.61)
AC_INIT(regxml_extractor, 0.4.0, ajnelson@cs.ucsc.edu)
AC_CONFIG_SRCDIR([scripts/regxml_extractor.sh.in])
AM_INIT_AUTOMAKE
AC_OUTPUT(Makefile deps/Makefile lib/Makefile scripts/Makefile)

# Checks for programs.

if test "$(uname -s)" = "Darwin"; then
  AC_CHECK_PROG(HAVE_GETOPT,getopt,yes,,/opt/local/bin)
  if test "$HAVE_GETOPT" = "yes"; then
    AC_SUBST(GNU_GETOPT,/opt/local/bin/getopt)
  else
    AC_MSG_ERROR([OS X environment detected, but GNU getopt not found; please install the MacPort package 'getopt'.  The BSD getopt included with OS X is known to be problematic.])
  fi
else
  AC_CHECK_PROG(HAVE_GETOPT,getopt,yes)
  if test "$HAVE_GETOPT" = "yes"; then
    AC_SUBST(GNU_GETOPT,getopt)
  else
    AC_MSG_ERROR([GNU getopt not found.])
  fi
fi

AC_CHECK_PROG(HAVE_HIVEXML,hivexml,yes)
if test "$HAVE_HIVEXML" != "yes"; then
  AC_MSG_ERROR([hivexml not found; refer to the README for Hivex compilation notes.])
fi

AC_CHECK_PROG(HAVE_ICAT,icat,yes)
if test "$HAVE_ICAT" != "yes"; then
  AC_MSG_ERROR([icat not found; refer to the README for Sleuth Kit compilation notes.])
fi

AC_CHECK_PROG(HAVE_FIWALK,fiwalk,yes)
if test "$HAVE_FIWALK" != "yes"; then
  AC_MSG_ERROR([fiwalk not found; refer to the README for Sleuth Kit compilation notes.])
fi

AC_CHECK_PROG(HAVE_XMLLINT,xmllint,yes)
if test "$HAVE_XMLLINT" != "yes"; then
  AC_MSG_ERROR([xmllint not found; refer to the README notes on xmllint.])
fi

AC_CHECK_PROG(HAVE_SQLITE3,sqlite3,yes)
if test "$HAVE_SQLITE3" != "yes"; then
  AC_MSG_ERROR([sqlite3 not found; please install it with your package manager (the package is most often named 'sqlite3').])
fi

AM_PATH_PYTHON(3.2)

AX_PYTHON_MODULE(argparse)
if test "$HAVE_PYMOD_ARGPARSE" != "yes"; then
  AC_MSG_ERROR([Argparse Python module not found; this can be installed with 'easy_install argparse'.])
fi

AX_PYTHON_MODULE(sqlite3)
if test "$HAVE_PYMOD_SQLITE3" != "yes"; then
  AC_MSG_ERROR([Sqlite3 Python module not found; you may need to install the sqlite3 development package and then rebuild your Python (see, e.g., the CentOS package script in deps/).])
fi

AC_CONFIG_FILES([
  scripts/regxml_extractor.sh
])

AC_OUTPUT
