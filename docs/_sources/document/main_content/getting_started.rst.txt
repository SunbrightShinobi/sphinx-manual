=================================================
Installing Ubuntu WSL and Cloning Repositories
=================================================
#.  First we need to install the Windows Subsystem for Linux (WSL) on your Windows 10/11 machine. This will allow us to run a Linux environment directly on Windows without the overhead of a traditional virtual machine or dualboot setup.
#.  Open PowerShell as Administrator and run the following command to enable the WSL feature:

    .. code-block:: none

        dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

#.  Next, enable the Virtual Machine Platform feature by running the following command in PowerShell:

    .. code-block:: none

        dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

#.  Restart your computer to apply the changes.
#.  After restarting, open the Microsoft Store and search for "Ubuntu". Choose the latest LTS version (e.g., Ubuntu 24.04 LTS) and click "Get" to start the installation.
#.  Once the installation is complete, launch Ubuntu from the Start menu. The first time you run it, you'll be prompted to create a new user account and password for the Linux environment.
#.  Then run :samp:`git clone <https://github.com/SunbrightShinobi/ubuntuWSL.git>_` This is the repository that contains all the installation scripts and configuration files needed to setup your WSL environment for Sphinx documentation building.
#.  Then run the setup script with the following commands:

    .. code-block:: none

        cd ubuntuWSL
        chmod +x setup_wsl_sphinx.sh
        ./setup_wsl_sphinx.sh

#.  When prompted, enter your sudo password to allow the script to install necessary packages and dependencies.
#.  Then close and reopen your Ubuntu WSL terminal to ensure all changes take effect.
#.  Then run :samp:`git clone <https://github.com/SunbrightShinobi/sphinx-manual.git>_` This will clone the repository inside you WSL Linux file structure. Which much faster and more efficient than working on the Windows side.
#.  If desired run :samp:`git clone <https://github.com/SunbrightShinobi/documentation-templates.git>_`` to get a repository of preconfigured Sphinx document templates to use as starting points for new documents.










=================================================
Getting Started with Sphinx from template
=================================================

First we need to setup a copy of the template document to use. If you are not working in a CM enviroment that already has one in the repository and just want to work from local desktop then just copy the entire default template folder from you baseline environment included with Cygwin installer, with the command below:

:samp:`cp /baseline_sphinx_env/template_document_default /baseline_sphinx_env/{new_document_name}`

Otherwise ask your team where you should copy the preconfigured template from in your CM repository.

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

#.  Now ensure your :program:`WSL` is running and you are inside your document folder. Perform either of the following steps depending on desired result:

    *   :kbd:`make livehtml` - Makes a livehtml build with a running web server at `<http://127.0.0.1:8000/>`_ that auto rebuilds upon detecting a change to any files of document.
    *   :kbd:`make html` - Makes a html build folder structure that can be uploaded to a web server. Output is located in :file:`./build/html`
    *   :kbd:`make latexpdf` - Makes a text file build then runs it through latex to make a pdf. Output is located in :file:`./build/latex` of document folder.
    *   :kbd:`make lgithunivehtml` - Makes a html build in the build/pages folder to be committed to GitHub Pages for hosting online. Once it pushed to Github folder it will be live at `<https://your_github_username>.github.io/<your_repository_name>/`_
    *   :kbd:`make clean latexpdf` does same as above items but prior to build generation it deletes the :file:`\build` folder

.. note::

    HTML builds are usually pretty good about overcoming errors and still building for you see what has happend. Latex not so much... Usually you will just have your build stop with a ? prompt. :kbd:`CTRL+D` cancels out of build and take note of line number at error and open the text file with a text editor to find that line and determine next steps.

.. raw:: latex

    \newpage
