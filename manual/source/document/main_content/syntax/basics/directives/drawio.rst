---------------------------
Image & Figure Directives
---------------------------

*   This is how you add a Draw.io Diagram as a converted to SVG

    *   Syntax:

        * ``:height: 100px`` In pixels
        * ``:width: 100px`` In pixels
        * ``:scale: %`` Integer Percentage Value of image
        * ``:alt: Alternate Text``
        * ``:align: left|center|right``
        * ``:figwidth: %`` Integer Percentage Value of entire figure
        * ``:figclass:`` Class attribute value of figure

        .. code-block:: none

            .. figure:: /_static/diagrams/drawio_example.svg
                :scale: 80
                :alt: Draw.io Example
                :align: center

                This is the caption of the exported Draw.io diagram as a SVG. 

    *   Rendered:

        .. figure:: /_static/diagrams/drawio_example.svg
            :scale: 80
            :alt: Drawio SVG Example
            :align: center

            This is the caption of the figure. So you can give a paragraph description of the image you linked. You could also include a table or a legend with multiple other images but ensure there is a blank link between them.


.. raw:: latex

    \newpage
