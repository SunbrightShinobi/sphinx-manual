.. jinja::

    -----------------------------------------------
    **Diagrams.Net** or **drawio** Extension
    -----------------------------------------------

    Sphinx Extension to add the drawio-html directive to include draw.io diagrams into the generated HTML documentation. `<https://www.diagrams.net/>`_ Its also my personal preference to add a direct download link to origiinal file using ``:download:`` 

    *   Requirements:

        * Install: ``sphinxcontrib-drawio-html`` via Python :program:`pip` (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment)
        * Add ``sphinxdrawio.drawio_html`` to Sphinx extentions in conf.py (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment via defaults.py)

    *   Syntax:

        *   ``.. drawio-html:: <drawio filename>``
        *   ``:page:`` Specify the pages to be rendered. This option is enforced in python part of the extension. Only the content for the diagrams of the specified pages is embedded into the HTML generation.
        *   ``:expanded:`` When this flag is selected, we start off in the expanded mode. Minimize is still available. When there is only page, expand/collapse along with page name is automatically hidden.
        *   ``:hide-nav:`` Hide the navigation completely. This will automatically enable expansion and displays all the pages.
        *   ``:force-name:`` When there is only one page, navigation is hidden the page name is not displayed with the assumption that the context around the diagram is generally enough. However the name display can be enabled by chosing the force-name.
        *   ``<content of the directive>`` Content of the directive is treated as CSS styles. Each diagram is given a unique id, and div#id is prefixed to each line automatically so that the styling is scoped to the given id. NOTE: No CSS parser is used and we assume each line to be a complete CSS directive. This option is working intermittently for some reason.

        .. code-block:: none

            .. drawio-html:: example.drawio
                :page: it,uml
                :expanded:
                :hide-nav:
                :force-name:

                <content>

            :download:`example.drawio (Download) <./example.drawio>`

    *   Rendered:

        .. important::

            Currently extension only works in html output not latexpdf

        .. only:: html

            .. drawio-html:: example.drawio

            :download:`example.drawio (Download) <./example.drawio>`

    .. raw:: latex

        \newpage
