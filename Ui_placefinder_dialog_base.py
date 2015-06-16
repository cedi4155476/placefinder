# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cch/.qgis2/python/plugins/PlaceFinder/placefinder_dialog_base.ui'
#
# Created: Wed May 27 13:48:58 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PlaceFinderDialogBase(object):
    def setupUi(self, PlaceFinderDialogBase):
        PlaceFinderDialogBase.setObjectName(_fromUtf8("PlaceFinderDialogBase"))
        PlaceFinderDialogBase.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(PlaceFinderDialogBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.searchButton = QtGui.QPushButton(PlaceFinderDialogBase)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout.addWidget(self.searchButton, 1, 1, 1, 1)
        self.searchLine = QtGui.QLineEdit(PlaceFinderDialogBase)
        self.searchLine.setObjectName(_fromUtf8("searchLine"))
        self.gridLayout.addWidget(self.searchLine, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.listWidget = QtGui.QListWidget(PlaceFinderDialogBase)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.button_box = QtGui.QDialogButtonBox(PlaceFinderDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.frame = QtGui.QFrame(PlaceFinderDialogBase)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.scrollArea = QtGui.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 110, 272))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.filterlayout = QtGui.QFormLayout()
        self.filterlayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.filterlayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filterlayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.filterlayout.setObjectName(_fromUtf8("filterlayout"))
        self.gridLayout_4.addLayout(self.filterlayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(PlaceFinderDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), PlaceFinderDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), PlaceFinderDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(PlaceFinderDialogBase)

    def retranslateUi(self, PlaceFinderDialogBase):
        PlaceFinderDialogBase.setWindowTitle(_translate("PlaceFinderDialogBase", "placefinder", None))
        self.searchButton.setText(_translate("PlaceFinderDialogBase", "suchen", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PlaceFinderDialogBase = QtGui.QDialog()
    ui = Ui_PlaceFinderDialogBase()
    ui.setupUi(PlaceFinderDialogBase)
    PlaceFinderDialogBase.show()
    sys.exit(app.exec_())

