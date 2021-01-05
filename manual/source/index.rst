.. jinja:: yaml_load

    ================================================================================
    |project| - (|git_repo|, |release|)
    ================================================================================

    .. only:: html

        ------------------
        Revision History
        ------------------

        .. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.2\linewidth-2\tabcolsep}
                            |>{\RaggedRight}p{\dimexpr 0.2\linewidth-2\tabcolsep}
                            |>{\RaggedRight}p{\dimexpr 0.6\linewidth-2\tabcolsep}|

        .. list-table:: Revision History
            :header-rows: 1
            :class: longtable
            :name: revision_history
            :align: center

            * - **Date**
              - **Rev**
              - **Description**

            {% for revision in _document['revisionHistory'] %}

            * - {{ revision['date'] }}
              - {{ revision['rev'] }}
              - {% for change in revision['changes'] %}
                {{ change }}
                {% endfor %}

            {% endfor %}


        --------------
        To Do List
        --------------

        .. todolist::


        .. image:: /images/sphinxlogo.png
            :scale: 80
            :alt: Sphinx Logo
            :align: center

    -----------------------------
    Sphinx Documentation Manual
    -----------------------------

    .. toctree::
        :maxdepth: 5
        :numbered:
        :name: mastertoc
        :glob:

        document/main_content/contents

    .. raw:: latex

        \beginappendices

    ---------------------
    APPENDICIES
    ---------------------

    .. toctree::
        :maxdepth: 2
        :numbered:
        :name: appendices
        :glob:

        common_docs/appendices/acronym_list

    .. raw:: latex

        \renewcommand{\bibname}{REFERENCES}
        \renewcommand{\thepage}{REF-\arabic{page}}

    .. only:: html

        ---------------------
        REFERENCES
        ---------------------

    .. only:: html or latex

        .. bibliography::
            :style: alpha

    .. only:: html

        ---------
        Indexes
        ---------

        * :ref:`genindex`
        * :ref:`modindex`
        * :ref:`search`
