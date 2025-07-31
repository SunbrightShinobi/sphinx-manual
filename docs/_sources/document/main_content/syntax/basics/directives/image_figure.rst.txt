---------------------------
Image & Figure Directives
---------------------------

*   This is how you add a image

    *   Syntax:

        * ``:height: 100px`` In pixels
        * ``:width: 100px`` In pixels
        * ``:scale: %`` Integer Percentage Value
        * ``:alt: Alternate Text``
        * ``:align: left|center|right``

        .. code-block:: none

            .. image:: /images/sphinxlogo.png
                :scale: 80
                :alt: Sphinx Logo
                :align: center

    *   Rendered:

        .. image:: /images/sphinxlogo.png
            :scale: 80
            :alt: Sphinx Logo
            :align: center


.. raw:: latex

    \newpage


*   This is how you add a figure

    *   Syntax:

        * ``:height: 100px`` In pixels
        * ``:width: 100px`` In pixels
        * ``:scale: %`` Integer Percentage Value of image
        * ``:alt: Alternate Text``
        * ``:align: left|center|right``
        * ``:figwidth: %`` Integer Percentage Value of entire figure
        * ``:figclass:`` Class attribute value of figure

        .. code-block:: none

            .. figure:: /images/sphinxlogo.png
                :scale: 80
                :alt: Sphinx Logo
                :align: center

                This is the caption of the figure. So you can give a paragraph description of the image you linked. You could also include a table or a legend with multiple other images but ensure there is a blank link between them.

    *   Rendered:

        .. figure:: /images/sphinxlogo.png
            :scale: 80
            :alt: Sphinx Logo
            :align: center

            This is the caption of the figure. So you can give a paragraph description of the image you linked. You could also include a table or a legend with multiple other images but ensure there is a blank link between them.


.. raw:: latex

    \newpage
