:orphan:

-------------------------------------------------
**Diagrams.Net** or **drawio** HTML Extension
-------------------------------------------------

.. important::

    Currently as of *sphinxcontrib-drawio-html 0.1.2*, while this extension does have the feature to be able to print entire drawing, large portions of the conversion leaves items out for shapes. Unable to be installed in CentOS for some reason right now, broken link to pythonhosted.

*   Requirements:

    * Install: ``sphinxcontrib-drawio-html`` extension via Python :program:`pip` (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment)
    * Add ``sphinxdrawio.drawio_html`` to Sphinx extensions in conf.py (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment via defaults.py)

This is your *.rst* file code example to import **DrawIO Diagram(s)**  `<http://https://www.diagrams.net/>`_ into your generated documentation. It is also my personal preference to add a direct download link to original file using ``:download:`filename.drawio``` 

``.. drawio-html:: path/filename.drawio``

.. tabularcolumns:: |p{\dimexpr 0.2\linewidth-2\tabcolsep}|
                      p{\dimexpr 0.6\linewidth-2\tabcolsep}|

.. list-table:: *DrawIO HTML* Options
    :header-rows: 1
    :class: longtable

    * - **Option**
      - **Values**
    * - `:page:`
      - *Name of Sheet* or *do not include option for entire drawing*
    * - `:expanded:`
      - 
    * - `:hide-nav:`
      - *Hides the navigation pane*
    * - `:force-name:`
      - *Forces name of sheet to show* if only displaying a single sheet but is default if no ``:page:`` included.

``:download:`drawio_example.drawio (Download) <./drawio_example.drawio>```

.. only:: html

*   Rendered:

.. code-block:: none

    .. drawio-html:: drawio_example.drawio
        :expanded:
        :hide-nav:
        :force-name:

        style-overrides

    :download:`drawio_example.drawio (Download) <./drawio_example.drawio>`
