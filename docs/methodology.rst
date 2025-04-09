Methodology
===========

The methodology behind F|Heat involves several key steps:

1. **Data Loading**: Downloading shape(.shp)-files for buildings, parcels, and streets. The plugin starts at the very beginning of the planning process by first downloading the shape files of the buildings, parcels and streets of the city or district to be analysed. The city name is selected from a drop-down list.
2. **Customization**: Preparing the files for further calculations with added attributes.
3. **Status quo Analysis**: The heat line density [kWh/m*a] is added to the street shape file. The parcels of neighbouring buildings are then merged into a larger polygon and supplemented with attributes that make it easier to find suitable areas for heat networks. Both layers are automatically given a style that makes high heat densities [kWh/ha*a] easily recognisable. Heat line densities and heat densities are labelled in accordance with federal guidelines for heat planning.
4. **Network Analysis**: The user can manually draw a polygon that acts as a supply area for a pipe-bound supply via a heating network. This polygon defines the buildings to be taken into account. Without a polygon, all buildings loaded in the project are taken into account in the network design and connected. The user must add a heat source as a point layer at a possible location for a heating centre. In addition, the user can select streets in the street file that are not to be included in the grid analysis, i.e. where no grid is to run and no buildings are to be connected. The tool generates a radial network with the function of defining the shortest route to the heat source. The resulting heat requirements per route metre and year are used to determine the required pipe dimensions. The resulting network is saved as a shape file and a summary of the network is also saved.

The result is a shape file and a tabular summary, which can be used for further detailed planning.

.. note::
    A scientific publication is in progress.

Current Datasources
-------------------
The current database is based on open data sources that are freely accessible.

- Shape files of the house perimeters with heat demand and street centre line (NRW): `OpenGeodata.NRW <https://opengeodata.nrw.de/produkte/umwelt_klima/klima/kwp/>`_
- Shape files of the parcels: `WFS NRW <https://www.wfs.nrw.de/geobasis/wfs_nw_inspire-flurstuecke_alkis>`_
- Velocity in the pipes adopted from Nussbaumer and Thalmann [1]_.
- Internal diameter and U-values (Values from various manufacturer specifications):
    - `Rehau <https://www.rehau.com/downloads/99896/rauthermex-rauvitherm-technische-information.pdf>`_
    - `Isoplus <https://www.isoplus.de/fileadmin/data/downloads/documents/germany/products/Doppelrohr-8-Seiten_DEUTSCH_Web.pdf>`_
    - `Logstor <https://www.logstor.com/media/7318/kingspan-logstor-product-catalogue-specifications-de-eur.pdf>`_
    - `Logstor Calculator <http://calc.logstor.com/de/energitab/>`_

.. 
    TODO: Add RWT Jagdt table description in next version

Load Profiles
-------------

Oemof's sub-library `demandlib <https://demandlib.readthedocs.io/en/latest/>`_ 
can be used for the estimation of heat and electricity demands of different 
consumer groups, as based on German standard load profiles (SLP).
These profiles are used to estimate the resulting heat demand and peak load in step 4.

The following heat standard load profiles of the Association of Energy and Water Management (BDEW) can be used:

+---------+----------------------------------------------------------------+
| Profile | House Type                                                     |
+=========+================================================================+
| efh     | single family house                                            |
+---------+----------------------------------------------------------------+
| mfh     | multi family house                                             |
+---------+----------------------------------------------------------------+
| gmk     | metal and automotive                                           |
+---------+----------------------------------------------------------------+
| gha     | retail and wholesale                                           |
+---------+----------------------------------------------------------------+
| gko     | Local authorities, credit institutions and insurance companies |
+---------+----------------------------------------------------------------+
| gbd     | other operational services                                     |
+---------+----------------------------------------------------------------+
| gga     | restaurants                                                    |
+---------+----------------------------------------------------------------+
| gbh     | accommodation                                                  |
+---------+----------------------------------------------------------------+
| gwa     | laundries, dry cleaning                                        |
+---------+----------------------------------------------------------------+
| ggb     | horticulture                                                   |
+---------+----------------------------------------------------------------+
| gba     | bakery                                                         |
+---------+----------------------------------------------------------------+
| gpd     | paper and printing                                             |
+---------+----------------------------------------------------------------+
| gmf     | household-like business enterprises                            |
+---------+----------------------------------------------------------------+
| ghd     | Total load profile Business/Commerce/Services                  |
+---------+----------------------------------------------------------------+

In addition, the location of the building and whether the building is located 
in a "windy" or "non-windy" area are taken into account for the application 
of heat standard load profiles.

The following electrical standard load profiles of the Association 
of the Electricity Industry (VDEW) could be used but it is not yet implemented:

+--------+---------------------------------------------------+
| Profile| Consumer Group                                    |
+========+===================================================+
|   h0   | households                                        |
+--------+---------------------------------------------------+
|   g0   | commercial general                                |
+--------+---------------------------------------------------+
|   g1   | commercial on weeks 8-18 h                        |
+--------+---------------------------------------------------+
|   g2   | commercial with strong consumption in the evening |
+--------+---------------------------------------------------+
|   g3   | commercial continuous                             |
+--------+---------------------------------------------------+
|   g4   | shop/hairdresser                                  |
+--------+---------------------------------------------------+
|   g5   | bakery                                            |
+--------+---------------------------------------------------+
|   g6   | weekend operation                                 |
+--------+---------------------------------------------------+
|   l0   | agriculture general                               |
+--------+---------------------------------------------------+
|   l1   | agriculture with dairy industry/animal breeding   |
+--------+---------------------------------------------------+
|   l2   | other agriculture                                 |
+--------+---------------------------------------------------+

The use of standard load profiles has the disadvantage that they only represent 
the average of a larger number of households (> 200). Load peaks of individual 
households (e.g. through the use of hair dryers or electric kettles) are filtered 
out by this procedure.

To take this into account, stochastic profiles can be used or the VDI 4655 guideline can be used for residential buildings which is primarily intended for use in evaluating decentralized energy systems, like CHP (Combined Heat and Power), heat pumps, etc..
The reference load profiles address the residential building types of single-family (SFH) and multi-family houses (MFH) based on the `TABULA <https://webtool.building-typology.eu/#bm>`_ classification, which is also used by the NRW heat demand model.
These reference profiles are also available from Oemofs sub-library `demandlib <https://demandlib.readthedocs.io/en/latest/>`_.


Limitations
-----------
The content of the download is designed for NRW, as there is no standardised nationwide data source yet.
The further steps of the plugin can also be carried out for other federal states, provided that the data structure is the same and the attributes have the same names.
Unlike many other planning software programmes, the plugin is free and open source. 
These are also developed for detailed planning and do not offer the possibility of carrying out rough designs in just a few minutes. Tools such as nPro, for example, are also primarily developed for neighbourhood planning and not for municipal heat planning.


References
----------

.. [1] Nussbaumer, T., Thalmann S. (2016). Influence of system design on heat distribution costs in district heating. Energy, 230, 496–505. https://doi.org/10.1016/j.energy.2016.02.062.
..
    additional references here if needed like LANUV or KWW