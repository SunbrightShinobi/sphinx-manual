---------------------
List Roles
---------------------

*   This role is used to create a bulleted list. Ensure you have blank lines between different tabbed lines.

    .. note::

        If you get any "Nesting too large" errors in latexpdf build but livehtml or html build works, check your spacing of new lines to be even with above start of line text.


    .. note::

        Your whitespace placement is key in RestructuredText. Take note of the examples of ensuring after a ``*`` or ``#.`` the next character starts on the next tab line. So 3 or 2 spaces respectivly.


    *   Syntax:

        .. code-block:: none

            *   Bullet Line 1
            *   Bullet Line 2
            *   Bullet Line 3

                *   Sub-Bullet Line 1


    *   Rendered:

        *   Bullet Line 1
        *   Bullet Line 2
        *   Bullet Line 3

            *   Sub-Bullet Line 1

*   This role is used to create an auto-numbered list. Ensure you have blank lines between different tabbed lines.

    *   Syntax:

        .. code-block:: none

            #.  Numbered Line 1
            #.  Numbered Line 2
            #.  Numbered Line 3

                #.  Sub-Numbered Line 1

    *   Rendered:

        #.  Numbered Line 1
        #.  Numbered Line 2
        #.  Numbered Line 3

            #.  Sub-Numbered Line 1


.. raw:: latex

    \newpage


*   This role creates a horizontal list can be used to set a list on several columns (HTML build only, in latexpdf build it makes a vertical bullet list with less space between them)

    *   Syntax:

        .. code-block:: none

            ..  hlist::
                :columns: 3

                *   first item
                *   second item
                *   third item
                *   fourth item
                *   fifth item


    *   Rendered:

        ..  hlist::
            :columns: 3

            *   first item
            *   second item
            *   third item
            *   fourth item
            *   fifth item

.. raw:: latex

    \newpage
