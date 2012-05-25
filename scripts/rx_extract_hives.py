#!/usr/bin/env python

# Copyright (c) 2012, Regents of the University of California
# All rights reserved.
#    
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#    
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# Neither the name of the University of California, Santa Cruz nor the
# names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.    

"""
For usage instructions, see the argument parser description below, or run this script without arguments.
"""

__version__ = "0.2.0"

import dfxml,fiwalk
import sys,os,datetime
import argparse

tally = 0

def proc_dfxml(fi):
    global tally
    global hivexml_command
    global imageabspath
    basename = os.path.basename(fi.filename()).lower()
    #Names noted in Carvey, 2011 (_Windows Registry Forensics_), page 18
    if fi.filename().lower().endswith(("ntuser.dat", "system32/config/sam", "system32/config/security", "system32/config/software", "system32/config/system", "system32/config/components", "local settings/application data/microsoft/windows/usrclass.dat")):
        outfilename = os.path.abspath(str(tally) + ".hive")
        print("\t".join(map(str, [
          outfilename,
          imageabspath,
          fi.filename(),
          fi.mtime(), fi.atime(), fi.ctime(), fi.crtime()
        ])))
        outfile = open(outfilename, "wb")
        outfile.write(fi.contents())
        outfile.close()
        if hivexml_command:
            command_string = hivexml_command + " " + outfilename + ">" + outfilename+".regxml" + " 2>" + outfilename + ".err.log"
            sysrc = os.system(command_string)
            if sysrc:
                sys.stderr.write("Error, see err.log: " + command_string + "\n")
        tally += 1

if __name__=="__main__":
    global hivexml_command
    global imageabspath

    parser = argparse.ArgumentParser(description="Find registry files in imagefile and dump hives to files in pwd in the order they're encountered, with a manifest printed to stdout.")
    parser.add_argument("-x", "--xml", dest="dfxml_file_name", help="Already-created DFXML file for imagefile")
    parser.add_argument("--hivexml", dest="hivexml_command", action="store_const", const="hivexml", default="",  help="Run hivexml command on each hive, producing output at <hive>.regxml, stderr at <hive>.err.log")
    parser.add_argument("imagefilename", help="Image file")
    args = parser.parse_args()
    
    hivexml_command = args.hivexml_command

    xmlfh = None
    if args.dfxml_file_name != None:
        xmlfh = open(args.dfxml_file_name, "r")
    imageabspath = os.path.abspath(args.imagefilename)

    fiwalk.fiwalk_using_sax(imagefile=open(imageabspath, "r"), xmlfile=xmlfh, callback=proc_dfxml)
