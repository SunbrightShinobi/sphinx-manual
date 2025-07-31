=================================================
Sphinx Documentation Structure
=================================================

From an official Sphinx-doc.org documentation standpoint, the applicable folder structure starts at :file:`/source` and is perfectly fine to use as the basis while learning. From a production standpoint, the folder structure is more robust to include aspects for configuration management using tools like :program:`Subversion` or :program:`Git`.

.. note::

    Ensure in all files and folders of your document there is no special characters or spaces in the names. You are using Cygwin as your environment and thus using a UNIX/Linux based file structure. That is why all folders are defined as using the back slash ``/`` instead of the forward slash ``\`` used in Windows.

.. note::

    Ensure none of your files you create start with :kbd:`_` and none are named **genindex, modindex, search** as those have reservation within Sphinx.


.. raw:: latex

    \newpage

.. _building_toctable:

=====================================
Building a Table of Contents
=====================================

This is the primary method used to link files together into a larger document. (Table of Contents)

.. note::

    While if using globs in your table of contents, you can start the files and folder with ## to order automatically but it is highly recommended to use a more detailed content.rst file with the toc to control ordering of creation

*   ``:maxdepth:`` - A numeric maxdepth option may be given to indicate the depth of the tree; by default, all levels are included.
*   ``:numbered:`` - Adds section numbers even in HTML output. Can also be limited by giving a numeric argument.
*   ``:name:`` - Implicit target name that ``:ref:`` can use.
*   ``:caption:`` - Provides a toctree caption
*   ``:titlesonly:`` - Shows only the titles of documents in the tree not other headings of same level
*   ``:glob:`` - All entries are matches against list of availble documents and then ordered into a alphabetical list. Required for ``folder/*`` entries.
*   ``:reversed:`` - Reverses ordering of list entries
*   ``:hidden:`` - Will notify Sphinx of document heirarchy but not build links. Useful if making custom links yourself
*   ``:includehidden:`` - If you want to have top level toctree linked but all other toctrees hidden.

.. note::

    Include ``:orphan:`` at top of rst file if it will not be part of toctree and to clear build warning.

.. code-block:: none

    .. toctree::
        :maxdepth: 4
        :numbered:
        :name: mastertoc
        :caption: Table of Contents
        :glob:

        rst_file01
        folder01/rst_file02
        folder02/*

.. raw:: latex

    \newpage
