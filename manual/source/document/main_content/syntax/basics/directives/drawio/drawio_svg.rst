:orphan:

.. jinja::

    -------------------------------------------------
    **Diagrams.Net** or **drawio** via exported SVG
    -------------------------------------------------

    *   You can also add an DrawIO file that is saved as an editable SVG file. *Tested that the editable HTML file cannot be used as a svg*

        *   Syntax:

            * ``:height: 100px`` In pixels
            * ``:width: 100px`` In pixels
            * ``:scale: %`` Integer Percentage Value of image
            * ``:alt: Alternate Text``
            * ``:align: left|center|right``
            * ``:figwidth: %`` Integer Percentage Value of entire figure
            * ``:figclass:`` Class attribute value of figure

            .. code-block:: none

                .. figure:: path/filename.svg
                    :scale: 10
                    :alt: Example DrawIO File, Sheet 1
                    :align: center

                    Example DrawIO File, Sheet 1

        *   Rendered:

            .. figure:: drawio_example.svg
                :scale: 80
                :alt: Example DrawIO File, Sheet 1
                :align: center
                :target: /_images/drawio_example.svg

                Example DrawIO File, Sheet 1

    .. raw:: latex

        \newpage
