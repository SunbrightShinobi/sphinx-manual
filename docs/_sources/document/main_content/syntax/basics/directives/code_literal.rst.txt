-------------------------------
Code or Literal Directives
-------------------------------

.. note::

    Your whitespace placement is key in RestructuredText. Take note of the examples of ensuring after a ``*`` or ``#.`` the next character starts on the next tab line. So 3 or 2 spaces respectively. This will make your code-block render inline with text of list.

.. important::

    You must have only (1) space between ``..`` and ``code-block::`` or another other role called in this manner. Do not tab between.

*   This is a role to document a python code object:

    *   Syntax:

        .. code-block:: none

            .. py:function:: enumerate(sequence[, start=0])

                Return an iterator that yields tuples of an index and an item of the  *sequence*. (And so on.)


    *   Rendered:

        .. py:function:: enumerate(sequence[, start=0])

            Return an iterator that yields tuples of an index and an item of the  *sequence*. (And so on.)


.. raw:: latex

    \newpage


*  This is a role used to display a boxed code-block section for code with an optional caption and optional line numbers.

    .. note::

        Since Cisco IOS/ASA/IOS-XE does not support a line continuation character, the latex generator will insert space and next line character into PDF. You will have to bring the code block to indent with main document level to have a copy/paste ready code block. Usually happens with ASA firewall rules.

        Or if in landscape and its still too long, you will need to have regular command lines for copy paste and use ``.. raw:: latex`` then ``/begin{scriptsize}`` and ``/end{scriptsize}``

    .. note::

        You can include variables from your yaml or contexts by using {{ variable }} in the code block and the value will be rendered. You must have at beginning of rst file ``.. jinja::`` and contents tabbed under.

    *   Syntax:

        *   ``.. code-block:: {lexer}`` Use :ref:`Lexers for RST <lexers_rst>`
        *   ``:linenos:`` Add Line numbers
        *   ``:lineno-start: {integer}`` Integer of where to start
        *   ``:caption: {string}`` Display name
        *   ``:name: {string}`` Name for ``ref``
        *   ``:emphasize-lines: {integer}``

        .. code-block:: none

            .. code-block:: python
                :linenos:
                :caption: Code Block
                :name: code_block
                :emphasize-lines: 1

                code line 1 *variable*
                code line 2 **cannot bold**
                You can also include variables like {{ release }}

    *   Rendered:

        .. jinja::

            .. code-block:: python
                :linenos:
                :caption: Code Block
                :name: code_block
                :emphasize-lines: 1

                code line 1 *variable*
                code line 2 **cannot bold**
                You can also include variables like {{ release }}


.. raw:: latex

    \newpage


*   This is used to where a large code blocks or literal are needed **with** markup inside.

    .. note::

        When rendered in PDF, it does not have a box around it.

    .. note::

        If you need to do inline markup with italics right after a bold. For example a unknown file name in a command. You will need to use escape character ``\`` then a space between them.

    .. note::

        You can include variables from your yaml or contexts by using {{ variable }} in the parsed-literal block and the value will be rendered. You must have at beginnging of rst file ``.. jinja::`` and the contents tabbed under.

    *   Syntax:

        *   ``:name: {string}`` Name for ``ref``

        .. code-block:: none

            .. parsed-literal::
                :name: parsed_literal

                code line 1 *variable*
                code line 2 **can bold**
                You can also include variables like {{ release }}

    *   Rendered:

        .. parsed-literal::
            :name: parsed_literal

            code line 1 *variable*
            code line 2 **can bold**
            You can also include variables like {{ release }}


.. raw:: latex

    \newpage


*   This is how you include a plain-text based file to render.

    .. note::

        There is a ``.. include:: filename`` role but with the features of the *literalinclude* role there isn't much benefit for it.

    *   Syntax:

        *   ``:caption: text`` - Text caption
        *   ``:name: text`` - Text name to use for ``:ref:``
        *   ``:dedent: 4`` - Removes leading indentation characters from file
        *   ``:language: {lexer}`` - Use :ref:`Lexers for RST <lexers_rst>`
        *   ``:emphasize-lines: 1,3-6`` Emphasis's called out lines
        *   ``:linenos:`` - Turns on Line Numbers
        *   ``:encoding: utf-8-sig`` - Encoding of file. default: `utf-8-sig`
        *   ``:pyobject: class.function`` - Only include the object/class from file if a py file.
        *   ``:lines: 1-10`` - Limits rendered output to listed line numbers
        *   ``:diff: filename2`` - diffs with listed filename compared to included filename

        .. code-block:: none

            .. literalinclude:: /scripts/examples/install.ps1
                :caption: install.ps1
                :name: install.ps1
                :language: none
                :emphasize-lines: 1-2
                :linenos:

    *   Rendered:

        .. literalinclude:: /scripts/examples/install.ps1
            :caption: install.ps1
            :name: install.ps1
            :language: none
            :emphasize-lines: 1-2
            :linenos:


.. raw:: latex

    \newpage
