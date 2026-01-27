# source/conf.py
# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime
from yamlreader import yaml_load
import subprocess
from pathlib import Path
from sphinx.util.osutil import ensuredir
from sphinx.builders.latex import LaTeXBuilder
# ---------------Convert to pdf for latexpff---------------------
def setup(app):
    app.connect('builder-inited', setup_latex_images)
    app.connect('build-finished', postprocess_latex_svg_to_pdf)

def setup_latex_images(app):
    """Setup image handling for LaTeX builds"""
    if app.builder.name == 'latex':
        # Ensure PDF versions of SVG diagrams exist
        diagrams_dir = Path(app.confdir) / '_static' / 'diagrams'
        if diagrams_dir.exists():
            for svg_file in diagrams_dir.glob('*.svg'):
                pdf_file = svg_file.with_suffix('.pdf')
                # If PDF already exists (created by _drawio_pdf), we're good
                if not pdf_file.exists():
                    # Try drawio command
                    try:
                        subprocess.run([
                            'drawio', str(svg_file.parent.parent.parent / 'shared' / 'diagrams' / svg_file.stem + '.drawio'),
                            '--export', '--disable-gpu',
                            '--disable-software-rasterizer', '--no-sandbox',
                            '--format', 'pdf', '-o', str(pdf_file)
                        ], check=True, capture_output=True, timeout=30)
                    except Exception:
                        pass

def postprocess_latex_svg_to_pdf(app, exc):
    """Replace SVG references with PDF in LaTeX output"""
    if app.builder.name != 'latex' or exc:
        return
    
    # Find and replace SVG references in the generated LaTeX file
    latex_file = Path(app.outdir) / f'{app.config.project}.tex'
    if latex_file.exists():
        content = latex_file.read_text()
        # Replace .svg references with .pdf
        # Look for patterns like {file}.svg or file.svg
        import re
        content = re.sub(r'([^}]*)\.svg([^}]*)', r'\1.pdf\2', content)
        content = re.sub(r'}{\.svg}', r'}.pdf}', content)
        latex_file.write_text(content)
# ------------------------------------------------------------------
# Base HTML context (MUST exist before use)
# ------------------------------------------------------------------

html_context = {}
documentnumber = os.getenv("DOCUMENT_NUMBER", "UNASSIGNED")

# ------------------------------------------------------------------
# HTML context
# ------------------------------------------------------------------

html_context.update({
    "documentnumber": documentnumber,
    "revisionHistory": [],
})

# ------------------------------------------------------------------
# Variable definement
# ------------------------------------------------------------------

docType = 'Sphinx Manual'
docType_short = 'EWI'
author = "Josh Johnson <joshua.johnson3@outlook.com>"
company = "Galaxy Forest Labs"
address = r"Galaxy Forest Labs\\ PO Box 239\\ Sunbright, TN 37872"
copyright = f"{datetime.now().year}, Galaxy Forest Labs"

companyProject = 'project'
segment = 'segment'
segment_short = 'XX'
csci = '<csciName>'
csci_short = '<csci>'
systemName = '<systemName>'
systemNameShort = '<systemName>'
icsVersion = 'X1.0'

responsibleEngineer = author
responsibleEngineerTitle = '<reTitle>'

signature01Name = '<name01>'
signature01Title = '<title01>'
signature02Name = '<name02>'
signature02Title = '<title02>'
signature03Name = '<name03>'
signature03Title = '<title03>'

documentnumber = '<docnum-tbd>'
docReleaseDate = '25JAN2026'
changeNotice = '<Rev. - CN ID>'
document_rev = '-'

docReleaseDesc = (
    r'Section x.x, Change Made\\ '
    r'Section x.x, Change Made\\ '
    r'Section x.x, Change Made'
)

classification = 'COMPANY INTERNAL'
contractNum = '<TBD>'
cdrlNum = '<TBD>'

doc_sw_pn_current = documentnumber
doc_sw_pn_dash_current = '01'
doc_sw_pn_previous = documentnumber
doc_sw_pn_dash_previous = '0000'

version = '1.0'
revision = '0'

project = docType
project_short = docType_short

# -- Path setup --------------------------------------------------------------
# Add project root so Sphinx can find modules
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# -- Project information -----------------------------------------------------
project = 'My Project'
author = 'Josh Johnson'
release = '1.0.0'

rst_epilog = """
.. |project| replace:: Galaxy Forest Labs
.. |git_repo| replace:: https://github.com/SunbrightShinobi/sphinx-manual
"""
html_context.setdefault("revisionHistory", [])

# -- Jinja and YAML configuration ---------------------------------------------------

jinja_contexts = {
    "yaml_load": {
        "_document": {
            'revisionHistory': {
                'html': [
                    {
                    'documentnumber': documentnumber,
                    'revision': document_rev,
                    'revisionDate': docReleaseDate,
                    'revisionCN': changeNotice,
                    'revisionDescriptionLine01': '',
                    'revisionDescriptionLine02': 'Initial Release',
                    'revisionDescriptionLine03': '',
                    'docPartNumber': doc_sw_pn_current + doc_sw_pn_dash_current,
                    'classification': classification,
                    'contractNum': contractNum,
                    'cdrlNum': cdrlNum,
                    'responsibleEngineer': responsibleEngineer,
                    'responsibleEngineerTitle': responsibleEngineerTitle,
                    'author': author,
                    },
                ],
            },
        "gitstatus": {},
        }
    }
}

# -- General configuration ---------------------------------------------------
extensions = [
    # Core Sphinx extensions
    "sphinx_jinja",
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.imgmath',
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',
    'sphinx_git',

    # Markdown
    'myst_parser',

    # Diagrams
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.rackdiag',
    'sphinxcontrib.packetdiag',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.mermaid',

    # Other useful extensions
    'sphinxcontrib.bibtex',
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output -------------------------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']

# -- LaTeX / PDF output ------------------------------------------------------
latex_engine = 'pdflatex'
latex_elements = {
    'preamble': r'''
\newcommand{\beginappendices}{\appendix}
''',
    'extrapackages': r'''
\usepackage{varwidth}
\usepackage[toc,page]{appendix}
\usepackage{graphicx}
\usepackage{svg}
''',
    'latex_engine': 'pdflatex',
    'maketitle': '\\sphinxmaketitle',
}

latex_documents = [
    ('index', 'myproject.tex', 'My Project', 'Author', 'manual'),
]

latex_show_urls = 'footnote'
latex_use_xindy = False

# -- Numfig for numbering figures/tables/code/sections -----------------------
numfig = True
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Code %s',
    'section': 'Section %s',
}

# -- TODO extension ----------------------------------------------------------
todo_include_todos = True
todo_emit_warnings = True
todo_link_only = True

# -- Diagrams Configuration --------------------------------------------------
FONT_PATH = '/usr/share/fonts/dejavu/DejaVuSans.ttf'

# seqdiag
seqdiag_fontpath = FONT_PATH
seqdiag_html_image_format = "PNG"
seqdiag_latex_image_format = "PDF"

# nwdiag / rackdiag / packetdiag
nwdiag_fontpath = FONT_PATH
nwdiag_html_image_format = "PNG"
nwdiag_latex_image_format = "PDF"

rackdiag_fontpath = FONT_PATH
rackdiag_html_image_format = "PNG"
rackdiag_latex_image_format = "PDF"

packetdiag_fontpath = FONT_PATH
packetdiag_html_image_format = "PNG"
packetdiag_latex_image_format = "PDF"

# blockdiag
blockdiag_fontpath = FONT_PATH
blockdiag_html_image_format = "PNG"
blockdiag_latex_image_format = "PDF"

# actdiag
actdiag_fontpath = FONT_PATH
actdiag_html_image_format = "PNG"
actdiag_latex_image_format = "PDF"

# plantuml
plantuml = "java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar"
plantuml_output_format = "svg"
plantuml_latex_output_format = "pdf"

# mermaid
os.environ["MERMAIDCLI_COMMAND"] = "npx --package=@mermaid-js/mermaid-cli --call mmdc"
mermaid_enable = True
mermaid_output_format = "png"
mermaid_latex_output_format = "pdf"
mermaid_default_export_scale = 75
mermaid_include_elk = False
mermaid_cmd = "npx mmdc"
mermaid_d3_zoom = True

# bibtex
bibtex_bibfiles = ['common_docs/references/refs.bib']
bibtex_default_style = 'alpha'
bibtex_encoding = 'utf-8-sig'
