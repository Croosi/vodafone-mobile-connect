# -*- coding: utf-8 -*-
# Copyright (C) 2010  Vodafone España, S.A.
# Author: Andrew Bird
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

from vmc.common.hardware.ericsson import (EricssonCustomizer,
                                          EricssonDBusDevicePlugin)


class EricssonF3607gw(EricssonDBusDevicePlugin):
    """L{vmc.common.plugin.DBusDevicePlugin} for Ericsson's F3607gw"""
    name = "Ericsson F3607gw"
    version = "0.1"
    author = u"Andrew Bird"
    custom = EricssonCustomizer

    __remote_name__ = "F3607gw"

    __properties__ = {
        'usb_device.vendor_id': [0x0bdb],
        'usb_device.product_id': [0x1904, 0x1906],
    }


ericssonF3607gw = EricssonF3607gw()
