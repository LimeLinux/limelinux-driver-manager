#
#
#  Copyright 2017 Metehan Özbek <mthnzbk@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
from setuptools import setup, find_packages
from os import listdir, system
import glob


langs = []
for l in listdir('languages'):
    if l.endswith('ts'):
        system('lrelease languages/%s' % l)
        langs.append(('languages/%s' % l).replace('.ts', '.qm'))


system('pyrcc5 dm.qrc -o driver_manager/resource.py')

datas = [('/usr/share/applications', ['data/limelinux-dm.desktop']),
         ('/usr/share/icons/hicolor/scalable/apps', ['images/limelinux-dm.svg']),
         ('/usr/share/limelinux-dm/languages', langs),
         ('/usr/share/limelinux-dm/data', glob.glob("data/*.lst"))
         ]

setup(
    name = "limelinux-dm",
    scripts = ["limelinux-dm"],
    packages = find_packages(),
    version = "1.0",
    license = "GPL v3",
    description = "Lime GNU/Linux Driver Manager",
    author = "Metehan Özbek",
    author_email = "mthnzbk@gmail.com",
    url = "https://github.com/LimeLinux/limelinux-driver-manager",
    keywords = ["PyQt5"],
    data_files = datas
)