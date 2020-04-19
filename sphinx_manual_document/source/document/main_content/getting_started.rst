=================================================
Getting Started with Sphinx from template
=================================================

First we need to setup a copy of the template document to use. If you are not working in a CM enviroment that already has one in the repository and just want to work from local desktop then just copy the entire default template folder from you baseline environment included with Cygwin installer, with the command below:

:samp:`cp /baseline_sphinx_env/template_document_default /baseline_sphinx_env/{new_document_name}`

Otherwise ask your team where you should copy the preconfigured template from in your CM repository.

    *   In SVN you would branch the folder keeping it inside the folder structure of the needed common style, configuration files and scripts to a new name of your assigned CM document number.

    *   In Git you would make a copy of folder keeping it inside the folder structure of the needed common style, configuration files and scripts and rename the folder to your assigned CM document number.

.. note::

    If you ever need to update your document to changes included in template, simply just use :program:`Beyond Compare` to compare the template folder against your document folder and see when files are different and if chnages are required. Usually most files are particular to each document except things like :file:`conf.py`.

Once you have your folder copied and renamed to a assigned document number or short description title.

#.  Edit :file:`/links` for any additional needed links or remove non-needed ones. Remeber its based on the soft link being put in :file:`/source`
#.  Edit the following parameters in :file:`/source/conf.py`:

    #.  **project** - :kbd:`Document Short Title` ex: Sphinx Manual
    #.  If you do not have the folder named as a assigned CM number then update **documentnumber** as well. Otherwise this autopopulates based on folder name of document.
    #.  Update **document_rev** if needed
    #.  Update Classification, Logo and Style of document. The following section of configuration copies the required files to build your document. Uncomment the lines of your desired section. Leave the rest commented out using ``#``

        .. code-block:: none

            ########## Sphinx NGGN (U) #####################################################
            classification = "UNCLASSIFIED"
            latex_additional_files = ['./latex_templates/sphinx/_procedure.sty',
                                      './latex_templates/sphinx/titlelogo.png',
                                      #'common/templates/iftex.sty',
                                     ]



    #.  Update **version* and **release** if not using higher folder structure to define those values.
    #.  If using yaml files from :file:`../configuration_files` then update **contexts** per the comment. There can be multiple contexts.

#.  That is all that is required to build until you get more familar. The rest of the items will show up in a TBD table to let you know to go edit them.

#.  Now ensure your :program:`Cygwin` is running and you are inside your document folder. Perform either of the following steps depending on desired result:

    *   :kbd:`make livehtml` - Makes a livehtml build with a running web server at `<http://127.0.0.1:8000/>`_ that auto rebuilds upon detecting a change to any files of document.
    *   :kbd:`make html` - Makes a html build folder structure that can be uploaded to a web server. Output is located in :file:`./build/html`
    *   :kbd:`make latexpdf` - Makes a text file build then runs it through latex to make a pdf. Output is located in :file:`./build/latex` of document folder.
    *   :kbd:`make clean livehtml`, :kbd:`make clean html` or :kbd:`make clean latexpdf` does same as above items but prior to build generation it deletes the :file:`\build` folder

.. note::

    HTML builds are usually pretty good about overcoming errors and still building for you see what has happend. Latex not so much... Usually you will just have your build stop with a ? prompt. :kbd:`CTRL+D` cancels out of build and take note of line number at error and open the text file with a text editor to find that line and determine next steps.

.. raw:: latex

    \newpage
