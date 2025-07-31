.. jinja:: yaml_load

    ================================================================================
    |project| - (|git_repo|, |release|)
    ================================================================================

    .. only:: html

        ------------------
        Revision History
        ------------------

        .. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.36\linewidth-2\tabcolsep}
                            |>{\RaggedRight}p{\dimexpr 0.14\linewidth-2\tabcolsep}
                            |>{\RaggedRight}p{\dimexpr 0.07\linewidth-2\tabcolsep}
                            |>{\RaggedRight}p{\dimexpr 0.43\linewidth-2\tabcolsep}|

        .. list-table:: Revision History
            :header-rows: 1
            :class: longtable
            :name: revision_history
            :align: center

            * - **Date**
              - **CN#**
              - **Rev.**
              - **Description**

            {% for revision in _document['revisionHistory']['html'] %}

            * - {{ revision['revisionDate'] }}
              - {{ revision['revisionCN'] }}
              - {{ revision['revision'] }}
              - {{ revision['revisionDescriptonLine01'] }}
                
                {{ revision['revisionDescriptonLine02'] }}
                
                {{ revision['revisionDescriptonLine03'] }}
                
            {% endfor %}

        --------------
        To Do List
        --------------



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
