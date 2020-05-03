------------------------
Specialized Directives
------------------------

*   This is a directive that identifies the author of the current section. The argument should include the author’s name such that it can be used for presentation and email address. The domain name portion of the address should be lower case.

    By default, this markup isn’t reflected in the output in any way (it helps keep track of contributions), but you can set the configuration value ``show_authors`` to True to make them produce a paragraph in the output.

    *   Syntax: ``.. sectionauthor:: Last, First <username@domain.com>``
    *   Rendered: N/A

    .. sectionauthor:: Last, First <username@domain.com>

*   This directive is the codeauthor directive, which can appear multiple times, names the authors of the described code, just like ``sectionauthor`` names the author(s) of a piece of documentation. It too only produces output if the ``show_authors`` configuration value is True.

    *   Syntax: ``.. codeauthor:: Last, First <username@domain.com>``
    *   Rendered: N/A

    .. codeauthor:: Last, First <username@domain.com>

*   The glossary directive is for defining terms and is used in :file:`/source/common_docs/acronym_list.rst` (Example taken from there)

    *   Syntax:

        .. code-block:: none

            .. glossary::

                ACI
                    Application Centric Infrastructure (Cisco product)

        .. code-block:: none

            :term:`ACI` (To just display the term and link it)

            :term:`Application Centric Infrastructure<ACI>` (To just display the term with Alternate text and link it)

    *   Rendered:

        :term:`ACI`

        or

        :term:`Application Centric Infrastructure<ACI>`

.. raw:: latex

    \newpage


*   The math directive for displayed math (math takes whole line). This also supports multiple equations, labeling the equation and then referencing with auto-numbering it inline with text.

    *   Syntax:

        .. code-block:: none

            .. math::
                :label: equation01

                (a + b)^2 = a^2 + 2ab + b^2

                (a - b)^2 = a^2 - 2ab + b^2

            Look at the cool equation :eq:`equation01`

    *   Rendered:

        .. math::
            :label: equation01

            (a + b)^2 = a^2 + 2ab + b^2

            (a - b)^2 = a^2 - 2ab + b^2

        Look at the cool equation :eq:`equation01`


*   This directive is for documenting footnotes.

    .. note::

        You can also explicitly number the footnotes (``[1]_``) or use auto-numbered footnotes without names (``[#]_``).

    *   Syntax:

        *   At text that requires a footnote:

            ``Text that requires a footnote [#]_.``

        *   At bottom of page or desired location of footnotes:

            .. code-block:: none

                .. rubric:: Footnotes:

                .. [#] Text of first footnote.

    *   Rendered:

        *   At text that requires a footnote: Text that requires a footnote [#]_.
        *   See left bottom of page:

            .. rubric:: Footnotes

            .. [#] Text of first footnote.


.. raw:: latex

    \newpage

*   This directive is for documenting Citation references.

    *   Syntax:

        *   Citation references, usually at bottom of page

            .. code-block:: none

                .. [CIT2002] A citation
                    (as often used in journals).

        *   and is called by: ``[CIT2002]_``

    *   Rendered:

        *   Citation references, usually at bottom of page

            .. [CIT2002] A citation
                (as often used in journals).

        *   an called by: [CIT2002]_

*   This directive is for documenting todo references.

    *   Syntax:

        *   Directive to create a todo list in document that appears as a row of Orange note blocks labeled as Todo with a link and location of all todo's

            .. code-block:: none

                **Todo List**

                .. todolist::

        *   Directive to mark a todo in document that will appear in list and create a Orange note block labeled as Todo

            .. code-block:: none

                .. todo::

                    (TODO: | FIXME: | BUG:) Currently when building latexpdf, todo directive causes issues. and disabled for adding to document during build but does show warnings during builds.
    *   Rendered:

        *   Directive to create a todo list in document that appears as a row of Orange note blocks labeled as Todo with a link and location of all todo's

            **Todo List**

            .. todolist::

        *   Directive to mark a todo in document that will appear in list and create a Orange note block labeled as Todo

            .. todo:: 

                TODO: Demonstration todo 1

            .. todo:: 

                FIXME: Demonstration todo 2

            .. todo:: 

                BUG: Demonstration todo 3

*   This directive is used for a concise titled paragraph, within its own box.

    .. note::

        The ``.. topic::`` role cannot be used within topics or body elements like lists or tables.

    *   Syntax:

        .. code-block:: none

            .. topic:: Your Topic Title

                Subsequent indented lines comprise
                the body of the topic, and are
                interpreted as body elements.

    *   Rendered (Untabbed due to limitation):

.. topic:: Your Example Topic Title

    Subsequent indented lines comprise the body of the topic, and are    interpreted as body elements.


.. raw:: latex

    \newpage
