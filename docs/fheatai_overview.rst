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

+-----------------+----------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------+
| **Component**   | **Release version 0.9**                            | **Version 1.0**                                   | **Future version(s)**                                                  |
+=================+====================================================+===================================================+========================================================================+
| F|Heat.map      | Beschaffung, Anreicherung, Aggregation und         | Ausweitung auf Bundesländer: ggf. Niedersachsen,  | Automatisierte Bedarfsmodellierung der Gebäude in der Planungsregion   |
|                 | Visualisierung von Gebäuden und Straßen etc.       | Schleswig-Holstein...                             |                                                                        |
+-----------------+----------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------+
| F|Heat.net      | Konzeptionierung, Auslegung und Visualisierung     | Verbesserte Netzauslegung (Dimensionierung und    | Vermaschte Netze, multiple Einspeiser, Prosumer, Substationen etc.     |
|                 | eines Wärmenetzes mit Vorlauf von 80°C (max) und   | Routenfindung)                                    |                                                                        |
+-----------------+----------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------+
| F|Heat.tec      | Aggregation und Visualisierung                     | (automatisierte) Speicherberechnung               | Verschiedene Speicher, Vorschläge zur Speicherstandorte...             |
+-----------------+----------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------+
| F|Heat.ai       | QGIS-Plugin zur Zusammenführung und Nutzung        | Anpassung des Gesamtsystems auf dänisches Modell  | Online Version mit Chatbot zur Entwicklung des Systems                 |
+-----------------+----------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------+


Example
-------

.. note::
    A detailed example will be added here.
