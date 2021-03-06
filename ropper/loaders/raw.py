# coding=utf-8
#
# Copyright 2014 Sascha Schirra
#
# This file is part of Ropper.
#
# Ropper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ropper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ropper.loaders.loader import *
from ropper.common.error import LoaderError
from ropper.arch import x86

class Raw(Loader):

    def __init__(self, filename, arch=x86):
        self.__codeSection = None
        super(Raw, self).__init__(filename)
        self.arch = arch

    @property
    def entryPoint(self):
        return 0x0

    def _getImageBase(self):
        return 0x0

    @property    
    def type(self):
        return Type.RAW

    @property
    def executableSections(self):
        return [self.__codeSection]

    @property
    def dataSections(self):
        return []

    def getSection(self, name):
        raise RopperError('No such secion: %s' % name) 

    def _parseFile(self):
        self.__codeSection = Section('bytes', self._bytes, 0x0, 0x0)

    def _loadDefaultArch(self):
        return None

  
    def setNX(self, enable):
        raise LoaderError('Not available for raw files')


    def setASLR(self, enable):
        raise LoaderError('Not available for raw files')

        
    def checksec(self):
        raise LoaderError('Not available for raw files')


    @classmethod
    def isSupportedFile(cls, fileName):
        return True

