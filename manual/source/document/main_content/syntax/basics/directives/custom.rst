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

                .. git_changelog::

            {% else %}

                **Not rendered due to document not being part of a Git repository.**

            {% endif %}

            .. raw:: latex

                \newpage

        *   Generate documentation from a task in an Ansible Playbook. `<https://github.com/shirou/sphinxcontrib-ansibleautodoc>`_

            .. code-block:: none

                .. ansibleautotask:: second task
                    :playbook: ../ansible/web.yml

            Rendered:

                .. todo::
                
                    Add rendered section when I have an example playbook

    .. raw:: latex

        \newpage
