--------------------------
Inline Text Markup Roles
--------------------------

.. note::

    Though some roles looks the same currently, follow the guidance listed of which role to use so if later the formatting for a role changes, you will not require to update your rst files to match.

*   For inline .rst file comments.

    *   Syntax:

        .. code-block:: none

            .. This is a comment line for a rst file.

        .. code-block:: none

            ..
                This whole indented block
                is a comment for a rst file.

                Still in the comment

    *   Rendered: N/A

*   This role is used to make any text bold (strong) and should be used to emphasize a point.

    *   Syntax: ``**Bolded**`` or ``:strong:`Bolded```
    *   Rendered: **Bolded** or :strong:`Bolded`

*   This role is used to bold the following text and represent a command entered by the user. *Looks the same as* ``**Bolded**`` *&* ``:strong:`Bolded```

    *   Syntax: ``:command:`del -rf /folder```
    *   Rendered: :command:`del -rf /folder`

*   This role is used when referring to the name of an application or suite. *Looks the same as* ``**Bolded**`` *&* ``:strong:`Bolded```

    *   Syntax: ``:program:`Mozilla Firefox```
    *   Rendered: :program:`Mozilla Firefox`

*   This role should be used to point out variable text with a lighter emphasis.

    *   Syntax: ``*Italicized*`` or ``:emphasis:`Italicized```
    *   Rendered: *Italicized* or :emphasis:`Italicized`


.. raw:: latex

    \newpage


*   This role is used to reference to a Unix/Linux manual page including the section. *Looks the same as* ``**Italicized**`` *&* ``:emphasis:`Italicized```

    *   Syntax: ``:manpage:`ls(1)```
    *   Rendered: :manpage:`ls(1)`

*   This role should be used for hostnames or screen output of a command.

    *   Syntax: ````text```` or ``:literal:`text```
    *   Rendered: ``text`` or :literal:`text`

*   This role is used when wanting to provide an example of a command and show the variable in { } for a single line. *Looks the same as* ````text```` *&* ``:literal:`text```

    *   Syntax: ``:samp:`ssh admin@{host}```
    *   Rendered: :samp:`ssh admin@{host}`

*   This role is used for any single (or combo) key press. *Looks the same as* ````text```` *&* ``:literal:`text```

    *   Syntax: ``:kbd:`CTRL+Z```
    *   Rendered: :kbd:`CTRL+Z`

*   This role is used when you are giving a path or a file name and show the variable in { }. *Looks the same as* ````text```` *&* ``:literal:`text```

    *   Syntax: ``:file:`source/document/{system}/```
    *   Rendered: :file:`source/document/{system}/`

*   This role is used for all GUI elements. This includes labels, text fields, buttons, etc. Place an ``&`` before any letter if you want to show the hotkey.

    *   Syntax: ``:guilabel:`&Next```
    *   Rendered: :guilabel:`&Next`

* This role is used to show a sequence through a menu. Place an ``&`` before any letter if you want to show the hotkeys.

    * Syntax: ``:menuselection:`Next --> Finish```
    * Rendered: :menuselection:`Next --> Finish`

*   This role is used to call out an abbreviation. If the role content contains a parenthesized explanation, it will be treated specially: it will be shown in a tool-tip in HTML, and output only once in LaTeX.

    *   Syntax: ``:abbr:`AD (Active Directory)```
    *   Rendered: :abbr:`AD (Active Directory)`

*   This role is used to call out an acronym that is in the acronym list (required). The acronym list is located at .. :file:`/source/common/appendices/acronym_list.rst`

    *   Syntax: ``:term:`AD```
    *   Rendered: :term:`AD`


.. raw:: latex

    \newpage


*   This role should be used for subscript text.

    *   Syntax: ``:subscript:`subscripted text```
    *   Rendered: :subscript:`subscripted text`

*   This role should be used for superscript text.

    *   Syntax: ``:superscript:`superscripted text```
    *   Rendered: :superscript:`superscripted text`

*   This role should be used for referencing books, periodicals and other materials.

    *   Syntax: ``:title-reference:`Reference Book```
    *   Rendered: :title-reference:`Reference Book`

.. raw:: latex

    \newpage
