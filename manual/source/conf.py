#!/usr/bin/env python3

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from datetime import datetime
import os
import sys
import yaml
import re
import string
from yamlreader import yaml_load

sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('./source/common'))
sys.path.append(os.path.abspath('./source/common_docs'))
sys.path.append(os.path.abspath('./source/configs'))
sys.path.append(os.path.abspath('./source/images'))
sys.path.append(os.path.abspath('./source/scripts'))

# -- Project information -----------------------------------------------------

project = 'Sphinx Manual'
copyright = u'{}, Binarylandscapes LLC'.format(datetime.now().year)
author = 'Josh Johnson <josh.johnson@binarylandscapes.com>'
address = 'Binarylandscapes Consulting\\\ 5923 Kingston Pike NUM 352\\\ Knoxville, TN 37919'

systemName = u'<SYSTEM NAME>'
csci = u'<CSCI NAME>'
responsibleEngineer = author

documentnumber = 'docnum-tbd'
docReleaseDate = u'01JAN2021'
changeNotice = u'TBD'
document_rev = 'A'
docReleaseDesc = u'Added DrawIO Extension'

classification = ""
contractNum = 'TBD'
cdrlNum = 'TBD'
doc_sw_pn_current = documentnumber
doc_sw_pn_dash_current = '0000'
doc_sw_pn_previous = documentnumber
doc_sw_pn_dash_previous = '0000'

# jinja_contexts can be multiple folders but they will appear to be merged in jinja_contexts.txt output, if you have documentConfig as part of load as it provides a common context
# the folder must be first option for yaml_load. Only one folder is permitted. It does not load sub-folders
# Update the context name and folder on a per document basis if needed
defaultConfig = {
        'defaultConfig' : {
            'systemName' : systemName,
            'revisionDate' : docReleaseDate,
        }
}

jinja_contexts = {
    'yaml_load' : yaml_load('configs/templates',defaultConfig),
}
with open('jinja_contexts.txt', 'wt') as out:
    print(yaml.safe_dump(jinja_contexts, default_flow_style=False), file=out)

# Confluence
confluence_publish = True
confluence_space_name = 'TG'
confluence_parent_page = 'Documentation'
confluence_server_url = 'https://binarylandscapes.atlassian.net/wiki/'
confluence_server_user = 'josh.johnson@binarylandscapes.com'
confluence_prev_next_buttons_location = 'top'
#confluence_publish_postfix = '-postfix'
#confluence_publish_prefix = 'prefix-'

# Load the rest of the default configuration
exec(open(r'./common/sphinx_scripts/sphinx_defaults.py').read())

