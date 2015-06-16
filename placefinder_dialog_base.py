# -*- coding: utf-8 -*-

"""
Module implementing PlaceFinderDialogBase.
"""
import ast

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PyQt4.QtNetwork import *

from qgis.gui import *
from qgis.core import *

from Ui_placefinder_dialog_base import Ui_PlaceFinderDialogBase

class PlaceFinderDialogBase(QDialog, Ui_PlaceFinderDialogBase):
    """
    Do everything that is needed to get the place and extent to it.
    """
    def __init__(self, iface, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.searchButton.setAutoDefault(True)
        self.searchButton.setDefault(True)
        self.iface = iface
        self.manager = QgsNetworkAccessManager.instance()
        self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
        self.checkboxes = {}
    
    def set_text(self,  text):
        """
        Set the text of the searchbox.
        """
        self.searchLine.setText(text)
        
    def request_finished(self):
        """
        Wait for the search to be finished and ignore if the string is empty.
        """
        try:
            self.datas = ast.literal_eval(self.reply.readAll().data())
            self.listWidget.clear()
            self.add_filter()
        except SyntaxError,  ValueError:
            True
        
    def json_search(self):
        """
        Get request from OSM.
        """
        url =  "http://nominatim.openstreetmap.org/search/?format=json&q="
        url += self.searchLine.text()
        request = QNetworkRequest()
        request.setUrl(QUrl(url))
        self.reply = self.manager.get(request)
        
        self.reply.finished.connect(self.request_finished)
    
    def add_filter(self):
        i = 0
        if self.checkboxes:
            for checkbox in self.checkboxes:
                self.filterlayout.removeWidget(self.checkboxes[checkbox])
                self.checkboxes[checkbox].hide()
            self.checkboxes.clear()
        
        for data in self.datas:
            if not data['type'] in self.checkboxes:
                self.checkBox = QCheckBox(self.scrollAreaWidgetContents)
                self.checkBox.setLayoutDirection(Qt.LeftToRight)
                self.checkBox.setFixedWidth(80)
                self.checkBox.setObjectName(data['type'])
                self.filterlayout.setWidget(i, 0, self.checkBox)
                self.checkBox.setText(data['type'])
                self.checkBox.stateChanged.connect(self.checkCheckboxes)
                self.checkboxes.setdefault(data['type'], self.checkBox)
                i += 1
        self.fill_List()
            
    def fill_List(self):
        self.listWidget.clear()
        
        for data in self.datas:
            self.list_add(data)
        
    def list_add(self, data):
        if not self.listWidget.findItems(data['display_name'], Qt.MatchExactly):
            self.listWidget.addItem(data['display_name'])
        
    def list_update(self, types):
        self.listWidget.clear()
        for data in self.datas:
            for type in types:
                if type == data['type']:
                        self.list_add(data)
                        
        for data in self.datas:
            if data['type'] == type:
                self.list_add(data)
    
    def checkCheckboxes(self):
        i=0
        activeboxes = []
        for checkbox in self.checkboxes:
            if self.checkboxes[checkbox].isChecked():
                i += 1
                activeboxes.append(checkbox)
        if i:
            self.list_update(activeboxes)
        else:
            #Falls nichts ausgewählt wurde wird die komplette Liste ausgegeben.
            self.fill_List()
    
    @pyqtSignature("")
    def on_button_box_accepted(self):
        """
        The function to zoom to the searched place.
        """
        canvas = self.iface.mapCanvas()
        item = self.listWidget.currentItem().text()
        print item
        for data in self.datas:
            text = data['display_name'].decode('unicode-escape')
            print text
            if text == item:
                y0, y1, x0, x1 = data['boundingbox']
                rect = QgsRectangle(float(x0), float(y0), float(x1), float(y1))
                crssrc = QgsCoordinateReferenceSystem(4326)
                crsdst = self.iface.mapCanvas().mapSettings().destinationCrs()
                xform = QgsCoordinateTransform(crssrc, crsdst)
                rect = xform.transformBoundingBox(rect)
                canvas.setExtent(rect)
        self.close()
    
    @pyqtSignature("")
    def on_button_box_rejected(self):
        """
        You can close the dialog.
        """
        self.close()
    
    @pyqtSignature("")
    def on_searchButton_clicked(self):
        """
        If you want to search manually you can still use this button.
        """
        self.json_search()
    
    @pyqtSignature("QListWidgetItem*")
    def on_listWidget_itemDoubleClicked(self, item):
        """
        If you double click on an item you go to the place.
        """
        self.on_button_box_accepted()
    
    @pyqtSignature("QString")
    def on_searchLine_textChanged(self, p0):
        """
        If the text in the searchbox has changed you get the results immediatly.
        """
        self.json_search()
    
    @pyqtSignature("QListWidgetItem*")
    def on_listWidget_itemActivated(self, item):
        """
        If an Item of the list is activated you can now search the place.
        """
        self.button_box.button(QDialogButtonBox.Ok).setEnabled(True)
    
    @pyqtSignature("")
    def on_listWidget_itemSelectionChanged(self):
        """
        If no item of the list is activated you shouldn't be able to search it.
        """
        self.button_box.button(QDialogButtonBox.Ok).setEnabled(False)
    
    @pyqtSignature("bool")
    def on_city_clicked(self, checked):
        """
        Slot documentation goes here.
        """
        self.json_search()
