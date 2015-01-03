# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'block_picker.ui'
#
# Created: Sat Dec 20 04:12:51 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(693, 739)
        Form.setMinimumSize(QtCore.QSize(0, 600))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.searchField = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchField.sizePolicy().hasHeightForWidth())
        self.searchField.setSizePolicy(sizePolicy)
        self.searchField.setEditable(True)
        self.searchField.setObjectName("searchField")
        self.horizontalLayout.addWidget(self.searchField)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtGui.QListWidget(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(211, 219, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 219, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.listWidget.setPalette(palette)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setResizeMode(QtGui.QListView.Adjust)
        self.listWidget.setViewMode(QtGui.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.tabBar = QTabBar(Form)
        self.tabBar.setObjectName("tabBar")
        self.horizontalLayout_2.addWidget(self.tabBar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.brightnessLabel = QtGui.QLabel(Form)
        self.brightnessLabel.setObjectName("brightnessLabel")
        self.gridLayout.addWidget(self.brightnessLabel, 3, 1, 1, 1)
        self.rendertypeLabel = QtGui.QLabel(Form)
        self.rendertypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rendertypeLabel.setObjectName("rendertypeLabel")
        self.gridLayout.addWidget(self.rendertypeLabel, 3, 2, 1, 1)
        self.cancelButton = QtGui.QPushButton(Form)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 3, 2, 1)
        self.opacityLabel = QtGui.QLabel(Form)
        self.opacityLabel.setObjectName("opacityLabel")
        self.gridLayout.addWidget(self.opacityLabel, 1, 1, 2, 1)
        self.selectButton = QtGui.QPushButton(Form)
        self.selectButton.setObjectName("selectButton")
        self.gridLayout.addWidget(self.selectButton, 0, 3, 2, 1)
        self.internalNameLabel = QtGui.QLabel(Form)
        self.internalNameLabel.setEnabled(False)
        self.internalNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.internalNameLabel.setObjectName("internalNameLabel")
        self.gridLayout.addWidget(self.internalNameLabel, 1, 2, 2, 1)
        self.nameLabel = QtGui.QLabel(Form)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 0, 1, 1, 1)
        self.idLabel = QtGui.QLabel(Form)
        self.idLabel.setEnabled(False)
        self.idLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.idLabel.setObjectName("idLabel")
        self.gridLayout.addWidget(self.idLabel, 0, 2, 1, 1)
        self.blockThumb = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blockThumb.sizePolicy().hasHeightForWidth())
        self.blockThumb.setSizePolicy(sizePolicy)
        self.blockThumb.setMinimumSize(QtCore.QSize(48, 48))
        self.blockThumb.setText("")
        self.blockThumb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.blockThumb.setObjectName("blockThumb")
        self.gridLayout.addWidget(self.blockThumb, 0, 0, 4, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.searchField, self.listWidget)
        Form.setTabOrder(self.listWidget, self.selectButton)
        Form.setTabOrder(self.selectButton, self.cancelButton)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Choose Block", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Search:", None, QtGui.QApplication.UnicodeUTF8))
        self.brightnessLabel.setText(QtGui.QApplication.translate("Form", "Brightness: x", None, QtGui.QApplication.UnicodeUTF8))
        self.rendertypeLabel.setText(QtGui.QApplication.translate("Form", "RenderType", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Form", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.opacityLabel.setText(QtGui.QApplication.translate("Form", "Opacity: x", None, QtGui.QApplication.UnicodeUTF8))
        self.selectButton.setText(QtGui.QApplication.translate("Form", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.internalNameLabel.setText(QtGui.QApplication.translate("Form", "minecraft:xxxxx", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("Form", "BlockName", None, QtGui.QApplication.UnicodeUTF8))
        self.idLabel.setText(QtGui.QApplication.translate("Form", "(xx:xx)", None, QtGui.QApplication.UnicodeUTF8))

from qtabbar import QTabBar