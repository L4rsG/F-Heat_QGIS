Overview of F|Heat
===============================

F|Heat is composed of several core components that work together to facilitate energy planning:

- **F|Heat.map**: Manages data related to buildings and roads, focusing on the visualization and analysis of heat planning data.
- **F|Heat.net**: Focuses on designing and visualizing heating networks, including cost estimations.
- **F|Heat.tec**: Aggregates and visualizes annual heat demands, network areas, and supports storage calculations.
- **F|Heat.ai**: QGIS plugin for merging and making the system components usable with an explanatory user interface as an initial step.

These components are provided together in a package, whereby each system component covers a sub-area of the planning and includes different development stages and will go through them in the future (see table in :ref:`dev_roadmap`).
The initial user interface is called F|Heat.ai and this also formulates the requirement for future development, namely that the individual components interact with and on top of each other with AI support and enable chatbot and AI-supported planning.

F|Heat.map
----------

**F|Heat.map** is responsible for the procurement, enrichment, aggregation, and visualization of building and road data in compliance with federal guidelines. It allows for:

- Automated process based on NRW's data structure.
- Mapping potentials such as areas for solar thermal energy and geothermal energy.
- Determining and visualizing the "socio-economically best solution" for the analyzed municipality.

F|Heat.net
----------

**F|Heat.net** handles the conceptual design, layout, and visualization of heating networks. It includes:

- Design of radiant heating networks with specific flow temperatures.
- Cost estimation for pipe construction.
- Future improvements such as meshed grids, multiple feeders, and anergy networks.

F|Heat.tec
----------

**F|Heat.tec** aggregates and visualizes annual heat demand data and network areas. It provides tools for:

- Automated storage calculation.
- Suggestions for storage locations based on annual values.
- Integration with other components of the F|Heat.ai system for comprehensive planning.

F|Heat.ai
----------

As an initial state the QGIS plugin serves for merging and utilising the system components with an explanatory user interface.

.. _dev_roadmap:

Development Roadmap
-------------------

Release version 0.9.0
^^^^^^^^^^^^^^^^^^^^^

+-----------------+--------------------------------------------------------+
| **Component**   | **Release version 0.9.0**                              |
+=================+========================================================+
| F|Heat.map      | Procurement, enrichment, aggregation and               |
|                 | visualisation of building and street data in           |
|                 | accordance with federal guidelines for heat planning   |
+-----------------+--------------------------------------------------------+
| F|Heat.net      | Design (radiant) heating network with flow temperatures|
|                 | of 80°C (max.) and 65°C (min.).                        |
|                 | Specification of costs for pipe construction           |
|                 | (without cicil engineering costs)                      |                        
+-----------------+--------------------------------------------------------+
| F|Heat.tec      | Aggregation and visualisation of the annual heat demand|
|                 | of the designed grid area (incl. simultaneity) as      |
|                 | annual values                                          |
+-----------------+--------------------------------------------------------+
| F|Heat.ai       | QGIS plugin for merging and utilising the system       |
|                 | components with an explanatory user interface          |
+-----------------+--------------------------------------------------------+

Version 1.0.0
^^^^^^^^^^^^^

+-----------------+----------------------------------------------------------------------------------+
| **Component**   | **Version 1.0.0**                                                                |
+=================+==================================================================================+
| F|Heat.map      | 1. Expansion to other federal states, possibly Lower Saxony, Schleswig-Holstein  |
|                 |                                                                                  |
|                 | 2. Mapping of potentials: Areas for ground-mounted solar thermal energy,         |
|                 | geothermal energy, water thermal energy, underground reservoirs                  |
|                 |                                                                                  |
|                 | 3. Determination and visualisation of the "socio-economically best solution"     |
|                 | as supply areas in the municipality under consideration                          |
+-----------------+----------------------------------------------------------------------------------+
| F|Heat.net      | Improved network design (dimensioning and routing)                               |
+-----------------+----------------------------------------------------------------------------------+
| F|Heat.tec      | (automated) storage calculation                                                  |
+-----------------+----------------------------------------------------------------------------------+
| F|Heat.ai       | Anpassung des Gesamtsystems auf dänisches Modell                                 |
+-----------------+----------------------------------------------------------------------------------+

Future version(s)
^^^^^^^^^^^^^^^^^

+-----------------+---------------------------------------------------+
| **Component**   | **Future version(s)**                             |
+=================+===================================================+
| F|Heat.map      | Automated demand modelling of buildings in the    |
|                 | planning region.                                  |
+-----------------+---------------------------------------------------+
| F|Heat.net      | Intermeshed grids, multiple feeders / prosumers,  |
|                 | substitutions / different temperature levels,     |
|                 | anergy grids.                                     |
+-----------------+---------------------------------------------------+
| F|Heat.tec      | Various heat storage options and suggestions for  |
|                 | storage locations.                                |
+-----------------+---------------------------------------------------+
| F|Heat.ai       | Online version with ChatBot to develop the system.|
+-----------------+---------------------------------------------------+

Example
-------

#. Create a folder for your project. Save your empty QGIS project in that folder

    .. figure:: images//example/1save_project.png
        :alt: 1save_project.png
        :width: 100 %
        :align: center



#. Start F|Heat. The user interface will open with the `introduction` tab. Simultaneously, the layer groups for the individual steps of the planning process will be created automatically.

    .. figure:: images//example/2start.png
        :alt: 2start.png
        :width: 100 %
        :align: center

    (If you have not installed the required python packages yet, check out the :ref:`Package-Installation` section.)


#. Switch to the `Download Files` tab. Here you can download the basic shapefiles needed for the planning process. Select a city from the dropdown list.

    .. figure:: images//example/3download1.png
        :alt: 3download1.png
        :width: 100 %
        :align: center



#. You can select whether you want to download the shapefiles for an entire city or a single district by toggling the buttons on the left. Once a city is selected, you can choose a district of that city by clicking the second dropdown list. In this example, we select the district Burgsteinfurt of the city Steinfurt. You can choose a different city and still follow along with this example.

    .. figure:: images//example/3download2.png
        :alt: 3download2.png
        :width: 100 %
        :align: center



#. Next you need to set the file path for the shapefiles by clicking the (...) button. This will open the directory of your QGIS project, where you can enter a file name.

    .. figure:: images//example/3download3.png
        :alt: 3download3.png
        :width: 100 %
        :align: center



#. When all file paths are set and a city or district is chosen, you can start the download by pressing `Start Download`. The progress bar below will show the progress of the process.

    .. figure:: images//example/3download4.png
        :alt: 3download4.png
        :width: 100 %
        :align: center



#. All layers are loaded into the `Basic Data` group once the download is complete.

    .. figure:: images//example/3download5.png
        :alt: 3download5.png
        :width: 100 %
        :align: center



#. You can also download optional `Zensus2022` data  that provides information about the type of heating and energy sources of the buildings in your city or district. This may be helpful in the planning process, but it is not necessary. Scroll down or extend the window to access the zensus data download.
    
    .. figure:: images//example/4zensus.png
        :alt: 4zensus.png
        :width: 100 %
        :align: center


#. For further calculations, the downloaded shapefiles of the buildings and streets must be adjusted. Toggle the dropdown lists to select the correct layers for streets, parcels and buildings.

    .. figure:: images//example/5adjust.png
        :alt: 5adjsut.png
        :width: 100 %
        :align: center


#. You can choose whether to overwrite the old files or save the adjusted files under a different name. Some building information that is not needed for the status and network analysis will be dropped during the adjustments; therefore, it can be useful to save the files under a different name if you need to check this information later.
    
    .. figure:: images//example/5adjust2.png
        :alt: 5adjsut2.png
        :width: 100 %
        :align: center


#. The new files will be added to the `Adjusted Files` layer group once the process is complete.

    .. figure:: images//example/5adjust3.png
        :alt: 5adjsut3.png
        :width: 100 %
        :align: center


#. In the `Status Analysis` tab, the heat line density and the heating demand per building block are added. Make sure you are using a projected coordinate system, such as UTM32N [EPSG:25832]. Otherwise, the area of the polygons may not be calculated in meters. Choose the newly adjusted streets and buildings.

    .. figure:: images//example/6status.png
        :alt: 6status.png
        :width: 100 %
        :align: center


#. Select the desired attribute of the buildings layer as heat demand. For the downloaded data, you can choose `RW_WW` where `RW` = Raumwärme(space heating) and  `WW` = Warmwasser(water heating) are combined. The attribute for thermal power is `Leistung_th`.

    .. figure:: images//example/6status2.png
        :alt: 6status2.png
        :width: 100 %
        :align: center


#. Set the file path for the heat density building blocks. The heat line attribute will be added to the adjusted streets.

    .. figure:: images//example/6status3.png
        :alt: 6status3.png
        :width: 100 %
        :align: center


#. Press start and wait for the process to complete. The layers will be added to the `Heat Density` group.

    .. figure:: images//example/6status4.png
        :alt: 6status4.png
        :width: 100 %
        :align: center


#. You can change the layer order and visibility by dragging the layers and toggling the checkboxes.

    .. figure:: images//example/6status5.png
        :alt: 6status5.png
        :width: 100 %
        :align: center

    .. figure:: images//example/6status6.png
        :alt: 6status6.png
        :width: 100 %
        :align: center


#. Before a heating network can be planned, you need to create a heat source and optionally define a planning area. You can create a new layer by selecting `Layer` > `Create Layer` > `New GeoPackage Layer...`.

    .. figure:: images//example/7source.png
        :alt: 7source.png
        :width: 100 %
        :align: center


#. First we create the source. First set a file path by pressing the (...) button. Choose "Point" as geometry type. Make sure that you select the same coordinate reference system as your project. You can see your project's CRS in the bottom right corner.

    .. figure:: images//example/7source2.png
        :alt: 7source2.png
        :width: 100 %
        :align: center


#. After you press `OK`, the new layer is added to your layer tree. Then you can press the `Toggle Editing` button.

    .. figure:: images//example/7source3.png
        :alt: 7source3.png
        :width: 100 %
        :align: center


#. Press the `Add Point Feature` button and click on the map to place a point.

    .. figure:: images//example/7source4.png
        :alt: 7source4.png
        :width: 100 %
        :align: center


#. Simply press `OK` when the `Feature Attributes` window appears. Then exit edit mode and save the layer by pressing the `Toggle Editing` button again.

    .. figure:: images//example/7source5.png
        :alt: 7source5.png
        :width: 100 %
        :align: center


#. Create a new layer for the planning area.

    .. figure:: images//example/8area.png
        :alt: 8area.png
        :width: 100 %
        :align: center


#. This time, select "Polygon" as the geometry type. Again, set the correct CRS.

    .. figure:: images//example/8area2.png
        :alt: 8area2.png
        :width: 100 %
        :align: center


#. Press the `Toggle Editing` button and then select `Add Polygon Feature`.

    .. figure:: images//example/8area3.png
        :alt: 8area3.png
        :width: 100 %
        :align: center


#. The buildings you want in your planning area must be completely inside the polygon. Right-click to finish your polygon and press `OK` when the `Feature Attributes` window appears.

    .. figure:: images//example/8area4.png
        :alt: 8area4.png
        :width: 100 %
        :align: center


#. Exit edit mode and save the layer by pressing the `Toggle Editing` button again.

    .. figure:: images//example/8area5.png
        :alt: 8area5.png
        :width: 100 %
        :align: center


#. You can change the layer properties by double-clicking the layer. For example, you can adjust the color and opacity so that the buildings and streets remain visible. Alternatively, you can move the area layer down in the layer tree.
    
    .. figure:: images//example/8area6.png
        :alt: 8area6.png
        :width: 100 %
        :align: center


#. Now you can proceed with the planning in the `Network Analysis` tab. First, select the supply and return temperatures. The design is carried out for a district heating system within a specific temperature range. Anergy/LowEx networks and high-temperature/steam networks are not designed; therefore, for the flow temperature range, only values between 60 and 90 degrees Celsius can be selected. The return temperature must then be selected within the corresponding range.

    .. figure:: images//example/9netanalysis.png
        :alt: 9netanalysis.png
        :width: 100 %
        :align: center


#. Select your layers and attributes as in the previous steps.

    .. figure:: images//example/9netanalysis2.png
        :alt: 9netanalysis2.png
        :width: 100 %
        :align: center


#. Select your planning area. Optionally, you can also choose to connect all the buildings from the building layer to your network by toggling the button on the left.

    .. figure:: images//example/9netanalysis3.png
        :alt: 9netanalysis3.png
        :width: 100 %
        :align: center

#. Set the file paths for the net GIS file and the result Excel file.

    .. figure:: images//example/9netanalysis4.png
        :alt: 9netanalysis4.png
        :width: 100 %
        :align: center


#. A temperature profile is needed to create the load profile. You can select your own temperature data by ticking the box and choosing a file. Alternatively, a standard example temperature profile from the weather station 'Münster/Osnabrück' will be used.

    .. figure:: images//example/9netanalysis5.png
        :alt: 9netanalysis5.png
        :width: 100 %
        :align: center


#. Press `Start Network Analysis` to start the process.

    .. figure:: images//example/9netanalysis6.png
        :alt: 9netanalysis6.png
        :width: 100 %
        :align: center


#. You may encounter an error indicating that some points of the street network in your area are not connected to the source. A figure showing the network of streets, buildings, and the source will appear. You can zoom in by pressing the magnifying button and drawing a rectangle.

    .. figure:: images//example/9netanalysis7.png
        :alt: 9netanalysis7.png
        :width: 100 %
        :align: center


#. Here we can see the disconnected street. 

    .. figure:: images//example/9netanalysis8.png
        :alt: 9netanalysis8.png
        :width: 100 %
        :align: center


#. There are two options to fix this problem:

   a) Change the street's attribute to be a possible route. The street will then be neglected, and the building will be connected to the next closest street.
   
      Select the street layer and press the `Select Features` button to choose the disconnected street.

      .. figure:: images//example/9netanalysis9.png
          :alt: 9netanalysis9.png
          :width: 100 %
          :align: center

      Select the street and open the attribute table by right-clicking the layer or by pressing the `Open Attribute Table (Selected Features)` button.

      .. figure:: images//example/9netanalysis10.png
          :alt: 9netanalysis10.png
          :width: 100 %
          :align: center

      Toggle editing mode and change the value under `possible_route` from 1 to 0.

      .. figure:: images//example/9netanalysis11.png
          :alt: 9netanalysis11.png
          :width: 100 %
          :align: center

      Toggle editing mode again to save the changes to the layer.

      .. figure:: images//example/9netanalysis12.png
          :alt: 9netanalysis12.png
          :width: 100 %
          :align: center

   b) Connect the street to the street network.
   
      Select the streets layer and toggle editing mode.

      .. figure:: images//example/9netanalysis13.png
          :alt: 9netanalysis13.png
          :width: 100 %
          :align: center

      Make sure snapping is enabled! Otherwise, the street will not be connected properly. Then press `Add Line Feature` to draw a new line connecting the street to the rest of the street network.

      .. figure:: images//example/9netanalysis14.png
          :alt: 9netanalysis14.png
          :width: 100 %
          :align: center

      Connect the streets. Thanks to snapping, the street points will be highlighted when you move the cursor close to them.

      .. figure:: images//example/9netanalysis15.png
          :alt: 9netanalysis15.png
          :width: 100 %
          :align: center

      Right-click to exit drawing mode. The `Feature Attributes` Window will appear. Scroll down and enter a 1 for the `possible_route` attribute. Press OK and toggle the editing mode again to save the layer.

      .. figure:: images//example/9netanalysis16.png
          :alt: 9netanalysis16.png
          :width: 100 %
          :align: center


#. In this example, we have connected the street. Now we can start the network analysis again.

    .. figure:: images//example/9netanalysis17.png
            :alt: 9netanalysis17.png
            :width: 100 %
            :align: center

#. When the process is complete, the network is added to the layer tree.

    .. figure:: images//example/9netanalysis18.png
        :alt: 9netanalysis18.png
        :width: 100 %
        :align: center

#. You can check the network for paths that make little sense. Currently, the program only searches for the shortest path from the building centroid to the source, so some paths may not be optimal. Additionally, smaller streets may not be included in the street file and can be added manually. In this example, a path runs outside the network area. There are no buildings connected there, which makes this route very unfavorable.

    .. figure:: images//example/9netanalysis19.png
        :alt: 9netanalysis19.png
        :width: 100 %
        :align: center

#. `OpenStreetMap` can assist you in adding new streets to the street layer. It can be found in the browser under `XYZ Tiles`. Simply drag and drop it into your project.

    .. figure:: images//example/9netanalysis20.png
        :alt: 9netanalysis20.png
        :width: 100 %
        :align: center

#. Now you can see that there are streets not included in the street layer.

    .. figure:: images//example/9netanalysis21.png
        :alt: 9netanalysis21.png
        :width: 100 %
        :align: center

#. You can easily add new streets like earlier when connecting the street to the street network:
    * Select the streets layer
    * Toggle Editing mode
    * Make sure that snapping is active
    * Add a new line feature (street)

    .. figure:: images//example/9netanalysis22.png
        :alt: 9netanalysis22.png
        :width: 100 %
        :align: center

#. Follow the street and use snapping to connect it to a point in the street network.

    .. figure:: images//example/9netanalysis23.png
        :alt: 9netanalysis23.png
        :width: 100 %
        :align: center

#. Do not forget to enter 1 at `possible_route` in the feature attributes. 

    .. figure:: images//example/9netanalysis24.png
        :alt: 9netanalysis24.png
        :width: 100 %
        :align: center

#. In addition, we can select the nearby streets that we do not want to include as routes and enter 0 for their `possible_route` attribute. Do not forget to toggle the editing mode once you are finished to save the layer.

    .. figure:: images//example/9netanalysis25.png
        :alt: 9netanalysis25.png
        :width: 100 %
        :align: center

    .. figure:: images//example/9netanalysis26.png
        :alt: 9netanalysis26.png
        :width: 100 %
        :align: center

    There are many more operations you can perform in QGIS, such as splitting line features, but it would be too much to cover all of them in this example. For more information, please refer to the `QGIS Training Manual <https://docs.qgis.org/3.34/en/docs/training_manual/index.html>`_ for more information.

#. Then you can start the network analysis again.

    .. figure:: images//example/9netanalysis27.png
        :alt: 9netanalysis27.png
        :width: 100 %
        :align: center


#. When you are satisfied with your heat network, you can create the result file. Once completed, the Excel file will open automatically, where you can find a net summary, pipe costs, load profile, and building statistics.

    .. figure:: images//example/10result.png
        :alt: 10result.png
        :width: 100 %
        :align: center

    .. figure:: images//example/10result2.png
        :alt: 10result2.png
        :width: 100 %
        :align: center
