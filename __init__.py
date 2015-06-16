# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PlaceFinder
                                 A QGIS plugin
 This Plugin lets you search places.
                             -------------------
        begin                : 2015-05-19
        copyright            : (C) 2015 by Cédric Christen Sourcepole
        email                : cch@sourcepole.ch
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PlaceFinder class from file PlaceFinder.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .placefinder import PlaceFinder
    return PlaceFinder(iface)
