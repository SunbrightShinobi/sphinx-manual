# -- Options for LaTeX output ---------------------------------------------
#latex_engine = 'lualatex'

latex_elements = {
    
'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',

# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',

'classoptions': ',openany,oneside',

'preamble': r'''

    \usepackage{xcolor}
    \usepackage{titlesec}

    %\usepackage{unicode-math} % Requires lualatex builder
    \usepackage{eforms}
    \usepackage{longtable,tabularx,ltxtable}
    \usepackage{booktabs}
    \usepackage[para]{threeparttablex}
    \usepackage{array,ragged2e}
    \usepackage{rotating}
    \usepackage{makecell}
    \usepackage{xstring}
    \usepackage{pdflscape}
    \usepackage{pdfpages}
    \usepackage{multicol}
    \usepackage{bookmark}


    \setkeys{Hyp}{bookmarksnumbered=true}%
    \setkeys{Hyp}{pageanchor=true}%
    \newgeometry{top=1.3in,bottom=1.1in,right=.5in,left=.5in,headheight=90pt}

    % Some document have long list lengths that will cause the build to fail
    % This resolves that issue.
    \usepackage{enumitem}
    \setlistdepth{9}
    \setlist[itemize,1]{label=$$\bullet$$}
    \setlist[itemize,2]{label=$$\bullet$$}
    \setlist[itemize,3]{label=$$\bullet$$}
    \setlist[itemize,4]{label=$$\bullet$$}
    \setlist[itemize,5]{label=$$\bullet$$}
    \setlist[itemize,6]{label=$$\bullet$$}
    \setlist[itemize,7]{label=$$\bullet$$}
    \setlist[itemize,8]{label=$$\bullet$$}
    \setlist[itemize,9]{label=$$\bullet$$}
    \renewlist{itemize}{itemize}{9}

    % Set the depth of the TOC counter
    \setcounter{secnumdepth}{9}

    \usepackage{alphalph,etoolbox}
    \appto\appendix{% patch \appendix so \AlphAlph is used
    \renewcommand\thechapter{\AlphAlph{\value{chapter}}}%
    }

    % Setup the color and look of note type directives
    % Color Mapping - https://www.latextemplates.com/svgnames-colors

    \sphinxsetup{
        noteborder=2pt,
        noteBorderColor={named}{Blue},
        %todoborder=2pt,
        %todoBorderColor={named}{Olive},
        importantborder=2pt,
        importantBorderColor={named}{Violet},
        cautionborder=2pt,
        cautionBorderColor={named}{Yellow},
        warningborder=2pt,
        warningBorderColor={named}{Orange},
        dangerborder=2pt,
        dangerBorderColor={named}{Red},
        VerbatimHighlightColor={named}{Magenta},
        TitleColor={named}{Black},
    }

    \makeatletter
    % Change the default layout of notes, caution, warning and danger blocks.
    \renewenvironment{sphinxnote}[1]
    {\begin{sphinxheavybox}\begin{center}\sphinxstrong{\MakeUppercase{#1}}\\\end{center} }{\end{sphinxheavybox}}

    \renewenvironment{sphinximportant}[1]
    {\begin{sphinxheavybox}\begin{center}\sphinxstrong{\MakeUppercase{#1}}\\\end{center} }{\end{sphinxheavybox}}

    \renewenvironment{sphinxwarning}[1]
    {\begin{sphinxheavybox}\begin{center}\sphinxstrong{\MakeUppercase{#1}}\\\end{center} }{\end{sphinxheavybox}}

    \renewenvironment{sphinxcaution}[1]
    {\begin{sphinxheavybox}\begin{center}\sphinxstrong{\MakeUppercase{#1}}\\\end{center} }{\end{sphinxheavybox}}

    \renewenvironment{sphinxdanger}[1]
    {\begin{sphinxheavybox}\begin{center}\sphinxstrong{\MakeUppercase{#1}}\\\end{center} }{\end{sphinxheavybox}}

    % Insert the Last Signature Field. WILL LOCK ALL OTHER FIELDS (PREVENT SIGNING!)
    \newcommand{\lastSigField}[3]{
    \sigField[\Lock{/Action/All}]{#1}{#2}{#3}
    }

''',

#'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
'printindex': r'\footnotesize\raggedright\printindex',

}

latex_top_level_sectioning= 'part'

# latex_additional_files = ['./common/procedure.sty',
#                           './common/titlelogo.png',
#                          ]

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (master_doc, file_name+'.tex', project,
     author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = './common/logo.eps'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = 'footnote'

# Documents to append as an appendix to all manuals.
latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, file_name, project,
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, file_name, project,
     author, file_name, 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


