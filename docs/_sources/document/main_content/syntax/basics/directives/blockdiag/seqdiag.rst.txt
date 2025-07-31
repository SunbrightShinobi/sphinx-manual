""""""""""""""""""""""""""""""""""""""""""""""
*blockdiag* Directive - **Sequence Diagram**
""""""""""""""""""""""""""""""""""""""""""""""

*   Requirements:

    *   Install: ``sphinxcontrib-seqdiag`` via Python :program:`pip` (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment)
    *   Add ``sphinxcontrib.seqdiag`` to Sphinx extentions in conf.py (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment via defaults.py)

This is your *.rst* file code example to create a **Sequence Diagram** `<http://blockdiag.com/en/seqdiag/index.html>`_:

.. tabularcolumns:: |p{\dimexpr 0.2\linewidth-2\tabcolsep}|
                     p{\dimexpr 0.6\linewidth-2\tabcolsep}|

.. list-table:: *seqdiag* Options
    :header-rows: 1
    :class: longtable

    * - **Option**
      - **Values**
    * - `:align:`
      - *left*, *center* or *right*
    * - `:scale:`
      - *0-100* percentage value
    * - `:caption:`
      - *text* to label Figure
    * - `:name:`
      - *text* to create hyperlink for sphinx (no spaces)
    * - `:desctable:`
      - Adds description table as shown in example. (no spaces in labels)

.. code-block:: none

    .. seqdiag::
        :align: center
        :caption: Example - Sequence Diagram
        :name: triton_coe_test_seqdiag
        :scale: 100
        :desctable:

        seqdiag {
            Level-1 ->  Level-2 ->  Level-3;
                        Level-2 ->              Report;
                                    Level-3 ->  Report;
            Level-1 [description = "Integration in Lab 9"];
            Level-2 [description = "Qualification in Lab 10 West"];
            Level-3 [description = "Certification in Triton System Center (TSC)"];
            Report [description = "Generate Report of testing"];
        }


.. raw:: latex

    \newpage


The previous code-block will generate this **Sequence Diagram**:

.. seqdiag::
    :align: center
    :caption: Example - Sequence Diagram
    :name: triton_coe_test_seqdiag
    :scale: 100
    :desctable:

    seqdiag {
        Level-1 ->  Level-2 ->  Level-3;
                    Level-2 ->              Report;
                                Level-3 ->  Report;
        Level-1 [description = "Integration in Lab 9"];
        Level-2 [description = "Qualification in Lab 10 West"];
        Level-3 [description = "Certification in Triton System Center (TSC)"];
        Report [description = "Generate Report of testing"];
    }


.. raw:: latex

    \newpage
