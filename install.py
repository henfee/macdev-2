#!/usr/bin/env python

import os


def linkFiles(sourceDir, destDir, startPattern, fPrefix, ignoreList):
    print "Linking all {0}* files in {1} to {2}".format(startPattern, sourceDir, destDir)
    for linkFile in os.listdir(sourceDir):
        if linkFile.startswith(startPattern) and linkFile not in ignoreList:
            sname = os.path.join(sourceDir, linkFile)
            dname = os.path.join(homeDir, "{0}{1}".format(fPrefix, linkFile))
            if not os.path.exists(dname):
                os.symlink(sname, dname)
                print "Linked {0} -> {1}".format(sname, dname)
            else:
                print "{0} already exists".format(dname)
    print


dirName = os.path.dirname(__file__)
dirName = os.path.abspath(dirName)
homeDir = os.path.expanduser('~')
homeDir = os.path.abspath(homeDir)

ignoreList = {'.git'}

# Create a symlink for dotfiles in the user's home dir
dotFilesDir = os.path.join(dirName, 'dotfiles')
linkFiles(dotFilesDir, homeDir, '.', '', ignoreList)

# Create a symlink for prezto as .zprezto in user's home dir
preztoDir = os.path.join(dirName, 'prezto')
preztoLink = os.path.join(homeDir, '.zprezto')
if not os.path.exists(preztoLink):
    os.symlink(preztoDir, preztoLink)
    print "Linked {0} -> {1}".format(preztoDir, preztoLink)
else:
    print "{0} already exists".format(preztoLink)

# Create a symlink for z* files in prezto/runcoms to user's home dir
runComsDir = os.path.join(preztoDir, 'runcoms')
linkFiles(runComsDir, homeDir, 'z', '.', ignoreList)
