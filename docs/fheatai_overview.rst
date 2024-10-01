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



#. Start F|Heat. The User Interface will open with the `introduction` tab. Simultaneously the layer groups for the individual steps of the planning proces will be created automatically.

    .. figure:: images//example/2start.png
        :alt: 2start.png
        :width: 100 %
        :align: center

    (If you have not installed the required python packages yet, check out the :ref:`Package-Installationn` section.)


#. Switch to the `Download Files` Tab. Here you can download the basic shapefiles needed for the planning process. Select a City from the dropdown list.

    .. figure:: images//example/3download1.png
        :alt: 3download1.png
        :width: 100 %
        :align: center



#. You can select wether you want to download the shape files of a city or a single district by toggling the buttons on the left. Once a city is selected, you can select a district of that city by clicking the second dropdown list. Here we select the district Burgsteinfurt of the city Steinfurt.

    .. figure:: images//example/3download2.png
        :alt: 3download2.png
        :width: 100 %
        :align: center



#. Next you need to set directories for the shapefiles by clicking the (...) button. This will open the directory of your QGIS project, where you can enter a file name.

    .. figure:: images//example/3download3.png
        :alt: 3download3.png
        :width: 100 %
        :align: center



#. When all directories are set and a city or district is chosen you can start the download by pressing **`Start Download`**. The progress bar below will show the progress of the process.

    .. figure:: images//example/3download4.png
        :alt: 3download4.png
        :width: 100 %
        :align: center



#. All layers are loaded in the `Basic Data` group once the download is completed.

    .. figure:: images//example/3download4.png
        :alt: 3download4.png
        :width: 100 %
        :align: center



#. You can also download optional `Zensus2022` data that provides insight on the heating type and energy source in your city or district. This may by helpful in the planning process but it is not necessary. Scroll down or extend the window to get to the zensus data download.

    .. figure:: images//example/4zensus.png
        :alt: 4zensus.png
        :width: 100 %
        :align: center