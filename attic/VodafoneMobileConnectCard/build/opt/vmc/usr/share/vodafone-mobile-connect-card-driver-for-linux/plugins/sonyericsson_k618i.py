# -*- coding: utf-8 -*-
# Copyright (C) 2006-2008  Vodafone España, S.A.
# Author:  Pablo Martí
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

__version__ = "$Rev: 1203 $"

from vmc.common.hardware.sonyericsson import SonyEricssonCustomizer
from vmc.common.plugin import RemoteDevicePlugin

class SonyEricssonK618i(RemoteDevicePlugin):
    """L{vmc.common.plugin.RemoteDevicePlugin} for SonyEricsson's K618i"""
    name = "SonyEricsson K618i"
    version = "0.1"
    author = u"Pablo Martí"
    custom = SonyEricssonCustomizer

    __remote_name__ = "AAD-3022042-BV"

sonyericsson_k618i = SonyEricssonK618i()
