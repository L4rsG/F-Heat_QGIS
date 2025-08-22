---
title: 'F|HEAT: An ecosystem for municipal heatplanning'
tags:
  - Python
  - QGIS
  - District Heating Network
  - Heat Planning
  # - More tags?
authors:
  - name: Hinnerk Willenbrink
    # orcid: 0000-0000-0000-0000 (add id if available)
    equal-contrib: true
    affiliation: 1
  - name: Lars Goray
    # orcid: 0000-0000-0000-0000 (add id if available)
    equal-contrib: true # (This is how you can denote equal contributions between multiple authors)
    affiliation: 1
  - name: Philipp Sommer
    orcid: 0009-0009-1097-4435
    equal-contrib: true
    corresponding: true # (This is how to denote the corresponding author)
    affiliation: 1 # (Multiple affiliations must be quoted)
#   - name: Victor Jagdt
#     corresponding: true # (This is how to denote the corresponding author)
#     affiliation: "1, 2" # (Multiple affiliations must be quoted)
affiliations:
 - name: FH Münster University of Applied Sciences, Department of Energy, Building Services and Environmental Engineering, Germany
   index: 1
#    ror: 00hx57361 (Research Organization Registry identifier?)
#  - name: RWT Jagdt, Germany
#    index: 2
#  - name: Independent Researcher, Country
#    index: 3
date:  April 2025
bibliography: paper.bib

# # Optional fields if submitting to another journal too, see this blog post:
# # https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
# aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
# aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

F|Heat is a software ecosystem designed for the planning of sector-coupled decarbonized energy systems, particularly in small to medium-sized towns and cities in rural regions. The free open-source plugin for QGIS enables users to conduct an inventory analysis and design an initial heat network. The plugin basically provides the basic data for municipal heat planning in accordance with §§ 14-15 of the german heat planning law [@wpg:2024]. It is also suitable for designing a local heating network and the associated technology for the planning area within a municipality. The tool is not designed for detailed planning, but provides results in a few minutes so that different scenarios and network routes can be quickly analysed. The results can then form the basis for further detailed planning. The plugin simplifies heat planning by automating tasks such as downloading data, customizing files, and visualizing grid areas. Users can customize network areas and routes to suit their planning needs.

# Statement of need

`F|HEAT` is a `QGIS` plugin Python package for municipal heatplanning. The methodology behind F|Heat involves several key steps:

- Data Loading: Downloading shape(.shp)-files for buildings, parcels, and streets. The plugin starts at the very beginning of the planning process by first downloading the shape files of the buildings, parcels and streets of the city or district to be analysed. The city name is selected from a drop-down list.

- Customization: Preparing the files for further calculations with added attributes.

- Status quo Analysis: The heat line density [kWh/m * a] is added to the street shape file. The parcels of neighbouring buildings are then merged into a larger polygon and supplemented with attributes that make it easier to find suitable areas for heat networks. Both layers are automatically given a style that makes high heat densities [kWh/ha * a] easily recognisable. Heat line densities and heat densities are labelled in accordance with federal guidelines for heat planning.

- Network Analysis: The user can manually draw a polygon that acts as a supply area for a pipe-bound supply via a heating network. This polygon defines the buildings to be taken into account. Without a polygon, all buildings loaded in the project are taken into account in the network design and connected. The user must add a heat source as a point layer at a possible location for a heating centre. In addition, the user can select streets in the street file that are not to be included in the grid analysis, i.e. where no grid is to run and no buildings are to be connected. The tool generates a radiant network with the function of defining the shortest route to the heat source. The resulting heat requirements per route metre and year are used to determine the required pipe dimensions. The resulting network is saved as a shape file and a summary of the network is also saved.

<!-- `F|HEAT` was designed to be used by both researchers and by
students in the context of municipal heatplanning. It has already been
used in a number of scientific publications [@Pearson:2017] and has also been
used in graduate courses on Galactic dynamics to, e.g., provide interactive
visualizations of textbook material [@Binney:2008]. -->

# Plugin description

F|Heat is composed of several core components that work together to facilitate energy planning:

- `F|Heat.map`: Manages data related to buildings and roads, focusing on the visualization and analysis of heat planning data.

- `F|Heat.net`: Focuses on designing and visualizing heating networks, including cost estimations.

- `F|Heat.tec`: Aggregates and visualizes annual heat demands, network areas, and supports storage calculations.

<!-- - `F|Heat.ai`: QGIS plugin for merging and making the system components usable with an explanatory user interface as an initial step. -->

These components are provided together in a package, whereby each system component covers a sub-area of the planning and includes different development stages and will go through them in the future.

`F|HEAT` comes with a [detailed documentation](https://f-heat-qgis.readthedocs.io/en/latest/index.html), including step-by-step instructions, explanations of all modeling methods, data usage and troubleshooting with known application errors.

<!-- 
Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.
-->

# Conclusion and outlook

<!-- Further instructions for "citations" and including "figures". Delete sections after editing-->
<!-- # Citations -->

<!-- Citations to entries in paper.bib should be in
[rMarkdown](https://bookdown.org/yihui/rmarkdown-cookbook/bibliography.html) format.

For example [Pearson:2017] from example entry `paper.bib`. Items can be cited directly within the paper using the syntax @key where key is the citation key in the first line of the entry, e.g., @R-base. To put citations in parentheses, use [@key]. To cite multiple entries, separate the keys by semicolons, e.g., [@key-1; @key-2; @key-3]. To suppress the mention of the author, add a minus sign before @, e.g., [-@R-base].

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"
- ``

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figures/fheat_logo.png)
and referenced from text using \autoref{fig:example}. -->

<!-- Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figures/fheat_logo.png){ width=20% } -->

<!-- Add acknowledgements and references should stay empty-->
# Acknowledgements

<!-- We acknowledge contributions from -->

# References