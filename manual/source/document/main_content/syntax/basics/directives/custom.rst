.. jinja::

    -----------------------------------------------
    Custom Directives (Not part of Sphinx baseline)
    -----------------------------------------------

    *   Custom roles via downloadable Sphinx Extensions

        *   Adding excerpts from git history to documentation `<https://github.com/OddBloke/sphinx-git>`_

            *   Requirements:

                * Install: ``sphinx-git`` via Python :program:`pip` (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment)
                * Add ``sphinx-git`` to Sphinx extentions in conf.py (Included in `SPHINX_ENV_INSTALL`, Sphinx Environment via defaults.py)

            *   Syntax:

                ``.. git_changelog::``

            *   Rendered (Git Changelog of this document):

            {% if 'inGit' in gitstatus %}

                **Not rendered due to document not being part of a Git repository.**

            {% else %}

                .. git_changelog::

            {% endif %}

            .. raw:: latex

                \newpage

    .. raw:: latex

        \newpage
