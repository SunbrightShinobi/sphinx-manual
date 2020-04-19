========================
Latex Directives
========================

*   For making a page break for pdf generation

    .. code-block:: none

      .. raw:: latex

          \newpage

*   To shrink text for PDF build that Landscape mode doesnt help with:

    *   To start text shrink:

        .. code-block:: none

            .. raw:: latex

                \begin{scriptsize}

    *   To stop text shrink:

        .. code-block:: none

            .. raw:: latex

                \end{scriptsize}

*   Custom latex roles

    *   In order to rotate pages for PDF output, you must tell it where to begin the rotation AND where to end it.

        *   To start the rotation, use the following

            .. code-block:: none

                .. raw:: latex

                    \begin{landscape}

        *   To end the rotation (yes you MUST do this otherwise the PDF build will FAIL):

            .. code-block:: none

                .. raw:: latex

                    \end{landscape}

.. raw:: latex

    \newpage
