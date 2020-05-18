.. jinja::

    -----------------------------------------------
    **Diagrams.Net** or **drawio** Extension
    -----------------------------------------------

    Sphinx Extension to add the drawio directive to include draw.io diagrams into the generated documentation. `<https://www.diagrams.net/>`_ Its also my personal preference to add a direct download link to origiinal file using ``:download:`` 

    *   Requirements:

        * Install: ``sphinxcontrib-drawio`` via Python :program:`pip` (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment)
        * Add ``sphinxdrawio.drawio`` to Sphinx extentions in conf.py (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment via defaults.py)

    *   Syntax:

        *   ``.. drawio:: <drawio filename>``

        .. code-block:: none

            .. drawio:: example.drawio
                :align: center
                :alt: Example DrawIO File
                :page-index: 0

            :download:`example.drawio (Download) <./example.drawio>`

    *   Rendered:

        .. drawio:: example.drawio


        :download:`example.drawio (Download) <./example.drawio>`

    .. raw:: latex

        \newpage
