-----------------------
Tables Directives
-----------------------

.. note::

    Tables will not be given a number if no caption is provided.
    
* This role builds a table from Comma Seperated Value (CSV) data or file

    *   Syntax:

        *   ``:header: "Header 1", "Header 2", "Header 3"`` - Set Columns header names
        *   ``:widths: 15, 10, 20`` - Set widths of columns
        *   ``:stub-columns: integer`` - Number of table columns to use as stubs (row title, on the left)
        *   ``:file: filename`` - Path to CSV file to use
        *   ``:url: path`` - Path to CSV file to use
        *   ``:delim: char`` - One-character identifier for delimiter

    .. code-block:: none

        .. csv-table:: Frozen Delights!
            :header: "Treat", "Quanity", "Description"
            :widths: 15, 10, 20

            "Albatross", 2.99, "On a stick!"
            "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be crunchy, now would it?"
            "Gannet Ripple", 1.99, "On a stick!"

    *   Rendered:

        .. csv-table:: Frozen Delights!
            :header: "Treat", "Quanity", "Description"
            :widths: 15, 10, 20

            "Albatross", 2.99, "On a stick!"
            "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be crunchy, now would it?"
            "Gannet Ripple", 1.99, "On a stick!"


.. raw:: latex

    \newpage


*   This role builds a more robust table that built from a list of lists and is compatible with Jinja scription and yaml. It does not follow the tab for the list rules though.

    .. note::

        Ensure you include the ``.. tabularcolums::`` block for setting the  alignment of columns in latexpdf build. The 0.xx number should match the corresponding ``:widths:`` values in ``.. list-table::`` You will get a build message saying both are not needed and widths will be ignored.

        *   ``:header-rows: integer`` - Set the number of heading rows
        *   ``:stub-columns: integer`` - Number of table columns to use as stubs (row title, on the left)
        *   ``class: longtable`` - Makes the table continue across pages in latexpdf builds. This is automatic is table is more than 30 rows.
        *   ``:name: string`` - Names the table
        *   ``:align: left|center|right`` - Alignment of table outside edges.

    *   Syntax:

    .. code-block:: none

        .. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.4\linewidth-2\tabcolsep}
                            |>{\RaggedRight}p{\dimexpr 0.4\linewidth-2\tabcolsep}

        .. list-table:: List of Lists Table
            :header-rows: 1
            :class: longtable
            :name: list_table
            :align: left

            * - **Header 1**
              - **Header 2**
            * - Row 1 content
              - Row 1 content
            * - Row 2 content
              - Row 2 content

    *   Rendered:

        .. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.4\linewidth-2\tabcolsep}
                            |>{\RaggedRight}p{\dimexpr 0.4\linewidth-2\tabcolsep}

        .. list-table:: List of Lists Table
            :header-rows: 1
            :class: longtable
            :name: list_table
            :align: left

            * - **Header 1**
              - **Header 2**
            * - Row 1 content
              - Row 1 content
            * - Row 2 content
              - Row 2 content


.. raw:: latex

    \newpage
