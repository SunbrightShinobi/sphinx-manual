:orphan:

-----------------------------------------------
**Diagrams.Net** or **drawio** Extension
-----------------------------------------------

.. important::


    This will fail of build on AlpineWSL due to there is not a Alpine Linux compatible installer for DrawIO Desktop. So it is recommended to use the ``:download:`filename.html``` or SVG method

*   Requirements:

    * Install: ``sphinxcontrib-drawio`` extension via Python :program:`pip` (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment)
    * Add ``sphinxdrawio.drawio`` to Sphinx extensions in conf.py (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment via defaults.py)

This is your *.rst* file code example to import **DrawIO Diagram(s)**  `<http://https://www.diagrams.net/>`_ into your generated documentation. It is also my personal preference to add a direct download link to original file using ``:download:`filename.drawio``` 

    ``.. drawio:: path/filename.drawio``

    .. tabularcolumns:: |p{\dimexpr 0.2\linewidth-2\tabcolsep}|
                          p{\dimexpr 0.6\linewidth-2\tabcolsep}|

    .. list-table:: *DrawIO* Options
        :header-rows: 1
        :class: longtable

        * - **Option**
          - **Values**
        * - `:align:`
          - *left*, *center* or *right*
        * - `:scale:`
          - *1-10* 1 is original
        * - `:transparency:`
          - *true|false* For PNG output only
        * - `:format:`
          - *svg|png|jpg* Output format, can override default setting (Broken), if set (SVG looks sharpest and does not require headless configuration)
        * - `:alt:`
          - *text* for alternative text in html
        * - `:page-index:`
          - *number* Index number of drawing page. You can only display 1 sheet. Repeat directive for additional sheets.

    ``:download:`path/filename.drawio (Download) <./path/filename.drawio>```

*   Rendered:

.. code-block:: none

    .. drawio:: drawio_example.drawio
        :align: center
        :alt: Example DrawIO File, Sheet 1
        :page-index: 0
        :scale: 1

    .. drawio:: drawio_example.drawio
        :align: center
        :alt: Example DrawIO File, Sheet 2
        :page-index: 1
        :scale: 1

.. only:: html

    :download:`drawio_example.drawio (Download) <./drawio_example.drawio>`

.. raw:: latex

    \newpage
