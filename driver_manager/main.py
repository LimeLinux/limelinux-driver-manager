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

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy,
                             QRadioButton, QDesktopWidget, QButtonGroup, QGroupBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from .check import DriverChecker


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle(self.tr("Driver Manager"))
        self.setLayout(QVBoxLayout())
        self.setFixedSize(750, 450)
        x, y = ((QDesktopWidget().availableGeometry().width() - self.width()) / 2,
               (QDesktopWidget().availableGeometry().height() - self.height()) / 2)
        self.move(x, y)

        self.groupbox = QGroupBox()
        self.groupbox.setLayout(QVBoxLayout())
        self.layout().addWidget(self.groupbox)

        # Content
        self.driverTitle()

        self.groupbox.layout().addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding))


        # Footer
        hlayout = QHBoxLayout()
        self.layout().addLayout(hlayout)

        hlayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Preferred))

        revert = QPushButton()
        revert.setText(self.tr("Revert"))
        hlayout.addWidget(revert)

        apply = QPushButton()
        apply.setText(self.tr("Apply"))
        hlayout.addWidget(apply)


    def driverTitle(self):
        layout = QHBoxLayout()
        self.groupbox.layout().addLayout(layout)

        logo = QLabel()
        logo.setScaledContents(True)
        logo.setPixmap(QPixmap(":/images/nvidia.svg"))
        logo.setFixedSize(32, 32)
        layout.addWidget(logo)

        self.title = QLabel()
        self.title.setText("Nvidia")
        layout.addWidget(self.title)

        grup = QButtonGroup()

        button1 = QRadioButton()
        button1.setText("Hebele")
        grup.addButton(button1)
        self.groupbox.layout().addWidget(button1)

        button1 = QRadioButton()
        button1.setText("Hebele")
        grup.addButton(button1)
        self.groupbox.layout().addWidget(button1)