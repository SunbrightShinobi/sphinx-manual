===============
Linking
===============

*   Link to a website (external of document)

    *   Syntax: ```<https://www.sphinx-doc.org/>`_``

    *   Rendered: `<https://www.sphinx-doc.org/>`_

*   You can also use the ``.. seealso: {link}``

    *   Syntax:

        ``.. seealso: https://www.sphinx-doc.org/``

    *   Rendered:

        .. seealso: https://www.sphinx-doc.org/

*   Link to a reST Anchor (internal of document from /source) that generates a hyperlink to anchor with a title (title can be different than section). Remeber to link to other documents outside of ``/source`` use links file to create a link to their ``/source`` in your document ``/source``.

.. _rst_ref_linking:

    .. note::

        Using ``:ref:`` is advised over standard reStructuredText links to sections (like ```Section title`_``) because it works across files, when section headings are changed, and for all builders that support cross-references.

    .. note::

        When linking to a section title, put the link above the title with a blank line for separation.

    *   Syntax

        *   Creating Link Anchor (Above title on doc_structure.rst):

            ``.. _building_toctable:``

        *   Linking to Anchor and creating title for link:

            ``:ref:`Building a TOCtable<building_toctable>```

    *   Rendered: :

        *   Creating Link Anchor (Below title on doc_structure.rst):
        *   Linking to Anchor:

            :ref:`Building a TOCtable<building_toctable>`

    .. note::

        You can also use ``:numref:`<Figure anchor>``` to provide just a Figure or Table #.# link

.. raw:: latex

    \newpage


*   Linking to files for download in HTML builds

    When you use this role, the referenced file is automatically marked for inclusion in the output when building (obviously, for HTML output only using ``.. only:: builder_html``). All downloadable files are put into the :file:`_downloads` subdirectory of the output directory; duplicate filenames are handled.

    The given filename is usually relative to the directory the current source file is contained in, but if it absolute (starting with /), it is taken as relative to the top source directory.

    The example.py file will be copied to the output directory, and a suitable link generated to it.

    Not to show unavailable download links, you should wrap whole paragraphs that have this role for html only builds:

    *   Syntax:

        .. code-block:: none

            .. only:: html

                See ``:download:`Example Script Download Link </scripts/examples/colors.json>```

    *   Rendered: **No output in latexpdf build**

        .. only:: html

            See :download:`Example Script Download Link </scripts/examples/colors.json>`

.. raw:: latex

    \newpage
