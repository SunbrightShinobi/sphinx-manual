import re
import sphinx
import tablib
import ciscoconfparse
import os

# -- General configuration ------------------------------------------------
# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinxcontrib.jinja',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.rackdiag',
    'sphinxcontrib.packetdiag',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.actdiag',
    'sphinx_git',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.jupyter',
    'sphinxcontrib.ansibleautodoc',
    'sphinxcontrib.confluencebuilder',
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',
]

# Configuration settings for imgmath
imgmath_image_format = "png"
# Configuration settings for seqdiag
seqdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
seqdiag_html_image_format = "SVG"
seqdiag_latex_image_format = "PDF"

# Configuration settings for nwdiag, rackdiag(nwdiag), packetdiag(nwdiag)
nwdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
nwdiag_html_image_format = "SVG"
nwdiag_latex_image_format = "PDF"
rackdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
rackdiag_html_image_format = "SVG"
rackdiag_latex_image_format = "PDF"
packetdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
packetdiag_html_image_format = "SVG"
packetdiag_latex_image_format = "PDF"

# Configuration settings for blockdiag
blockdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
blockdiag_html_image_format = "SVG"
blockdiag_latex_image_format = "PDF"

# Configuration settings for actdiag
actdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
actdiag_html_image_format = "SVG"
actdiag_latex_image_format = "PDF"

# Configuration settings for plantuml
plantuml_output_format = "svg"
plantuml_latex_output_format = "eps"
plantuml = "java -jar " + os.environ[r'PLANTUML']

numfig = True
numfig_format = {'figure': 'Figure %s',
                 'table': 'Table %s',
                 'code-block': 'Code %s',
                 'section': 'Section %s',
                }

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True # TODO: Figure out latex issues when i turn on todo list. This needs to be false in latexpdf
todo_emit_warnings = True
todo_link_only = True

highlight_languange = 'shell-session'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Load the git configuration
exec(open(r'./common/sphinx_git.py').read())

# set filename
file_name = '_'.join([project.replace(' ', '_'),
                      'Release',
                      gittag.replace('.', '_').replace(' ', '_'),])

rst_prolog = """
.. |project| replace:: {project}

.. |git_repo| replace:: {git_repo}

""".format(project=project,
           git_repo=git_repo,
           )

# Load the html configuration
exec(open(r'./common/sphinx_html_defaults.py').read())
# Load the latexpdf configuration
# exec(open(r'./common/sphinx_latex_defaults.py').read())

# The master toctree document.
master_doc = 'index'
