#!/usr/bin/env python3

# Configuration file for the Sphinx documentation builder.

from datetime import datetime
import os
import sys
import yaml
import string
from yamlreader import yaml_load

# -- Path setup --------------------------------------------------------------

sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('./source/common_docs'))
sys.path.append(os.path.abspath('./source/configs'))
sys.path.append(os.path.abspath('./source/images'))
sys.path.append(os.path.abspath('./source/scripts'))

def exec_file(path):
    with open(path, 'r') as f:
        code = compile(f.read(), path, 'exec')
        exec(code, globals())

exec_file('./sphinx_scripts/sphinx_git.py')
docReleaseVersion = get_git_release()

# -- Helper functions --------------------------------------------------------
def latex(s: str) -> str:
    """
    Helper for LaTeX content.
    - Write LaTeX naturally with single backslashes
    - Python-safe escaping handled here
    """
    return s.replace('\\', r'\\')

# -- Project information -----------------------------------------------------

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
docReleaseDate = '29JULY2025'
changeNotice = '<Rev. C CN ID>'
document_rev = 'C'

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

# -- Jinja / Document Context ------------------------------------------------

documentConfig = {
    '_document': {
        'release': docReleaseVersion,
        'type': docType,
        'type_short': docType_short,
        'company': company,
        'companyProject': companyProject,
        'segment': segment,
        'segment_short': segment_short,
        'csci': csci,
        'csci_short': csci_short,
        'icsVersion': icsVersion,
        'title': project,

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

            'latex': [
                [
                    r'\\multicolumn{1}{|c|}{\\rule{0pt}{36pt}'
                    r'\\multirow{2}{2.5in}[2.6em]{'
                    '\\textbf{Document Number} \\ \\ '
                    '\\textbf{Revision} \\ \\ '
                    '\\textbf{Date} \\ \\ '
                    '\\textbf{Change Notice} \\ \\ '
                    '\\textbf{Document Part Number} \\ \\ '
                    '\\textbf{Classification} \\ \\ '
                    '\\textbf{Contract Number} \\ \\ '
                    '\\textbf{CDRL Number} \\ \\ '
                    '\\textbf{Responsible Engineer} \\ \\ '
                    '\\textbf{Author} \\ \\ '
                    '}',
                    r'\\multicolumn{1}{c|}{\\rule{0pt}{36pt}'
                    r'\\multirow{2}{2.5in}[2.6em]{'
                    f'{documentnumber} \\ \\ '
                    f'{document_rev} \\ \\ '
                    f'{docReleaseDate} \\ \\ '
                    f'{changeNotice} \\ \\ '
                    f'{doc_sw_pn_current}{doc_sw_pn_dash_current} \\ \\ '
                    f'{classification} \\ \\ '
                    f'{contractNum} \\ \\ '
                    f'{cdrlNum} \\ \\ '
                    f'{responsibleEngineer} \\ \\ '
                    f'{author} \\ \\ '
                    '}',
                    r'\\sigField{Sig1}{2.5in}{0.5in} \\ }}',
                    r'\\multicolumn{1}{l|}{\\rule{0pt}{36pt}\changeNotice}',
                    r'\\multicolumn{1}{c|}{\\rule{0pt}{36pt}\docrevision}',
                    r'\\multicolumn{1}{l|}{\\rule{0pt}{36pt}'
                    r'\\multirow{3}{3.0in}[2.5em]{\docReleaseDesc}} \\ \hline',
                ],
            ],
        },

        'signatures': {
            'html': [
                {'jobFunction': responsibleEngineerTitle, 'name': responsibleEngineer, 'date': '-'},
                {'jobFunction': signature01Title, 'name': signature01Name, 'date': '-'},
                {'jobFunction': signature02Title, 'name': signature02Name, 'date': '-'},
                {'jobFunction': signature03Title, 'name': signature03Name, 'date': '-'},
            ],

            'latex': [
                [
                    r'\\multicolumn{1}{|c|}{\\rule{0pt}{36pt}\\responsibleEngineerTitle}',
                    r'\\multicolumn{1}{c|}{\\rule{0pt}{36pt}\\responsibleEngineer}',
                    r'\\multicolumn{1}{c|}{\\rule{0pt}{36pt}\sigField{Sig0}{2.5in}{0.5in}} \\ \hline',
                    r'\\multicolumn{1}{l|}{\\rule{0pt}{36pt}'
                    r'\\multirow{3}{3.0in}[2.5em]{'
                    r'Section x.x, Change Made \\ '
                    r'Section x.x, Change Made \\ '
                    r'Section x.x, Change Made} \\ \hline',
                ],
                [
                    r'\\multicolumn{1}{|c|}{\\rule{0pt}{36pt}\\iptSignatureTitle}',
                    r'\\multicolumn{1}{c|}{\\rule{0pt}{36pt}\\iptSignatureName}',
                    r'\\multicolumn{1}{c|}{\\rule{0pt}{36pt}\sigField{Sig1}{2.5in}{0.5in}} \\ \hline',
                ],
                [
                    r'\\multicolumn{1}{|c|}{\\rule{0pt}{36pt}\\vpSignatureTitle}',
                    r'\\multicolumn{1}{c|}{\\rule{0pt}{36pt}\\vpSignatureName}',
                    r'\\multicolumn{1}{c|}{\\rule{0pt}{36pt}\sigField{Sig2}{2.5in}{0.5in}} \\ \hline',
                ],
                [
                    r'\\multicolumn{1}{|c|}{\\rule{0pt}{36pt}\\qaSignatureTitle}',
                    r'\\multicolumn{1}{c|}{\\rule{0pt}{36pt}\\qaSignatureName}',
                    r'\\multicolumn{1}{c|}{\\rule{0pt}{36pt}\sigField{Sig3}{2.5in}{0.5in}} \\ \hline',
                ],
            ],
        },
    },

    'system': {
        'name': systemName,
        'domain': '<domainName>',
        'id': systemNameShort,
    },

    'requiredMedia': [],
}

BASE_DIR = os.path.dirname(__file__)
jinja_contexts = {
    'yaml_load': yaml_load(os.path.join(BASE_DIR, 'configs', 'templates'), documentConfig),
}

if os.environ.get('SPHINX_DEBUG_JINJA'):
    with open('jinja_contexts.txt', 'wt') as out:
        yaml.safe_dump(jinja_contexts, out)

# -- Confluence --------------------------------------------------------------

confluence_publish = False
confluence_space_key = 'US'
confluence_parent_page = 'Sphinx Manual'
confluence_server_url = 'https://skydweller.atlassian.net/wiki/'
confluence_ask_user = False
confluence_server_user = ''
confluence_ask_password = True
confluence_disable_notifications = True
confluence_add_secnumbers = True
confluence_default_alignment = 'left'
confluence_page_generation_notice = True
confluence_page_hierarchy = True
confluence_prev_next_buttons_location = 'top'
confluence_purge = True
confluence_publish_dryrun = True

confluence_sourcelink = {
    'url': 'https://github.com/SunbrightShinobi/sphinx-manual',
}
exec_file('./sphinx_scripts/sphinx_defaults.py')

# -- Defaults ----------------------------------------------------------------
exclude_patterns = ['**/.nojekyll']
