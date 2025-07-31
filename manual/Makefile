# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
COMMONDIR     = ./source
COMMONDOCSDIR = ./source/common_docs
CONFIGSDIR    = ./source/configs
IMAGESDIR     = ./source/images
SCRIPTSDIR    = ./source/scripts
GITHUBDIR     = ../docs
SPHINX_TEMPLATES = us_dod
TEMPLATE_FOLDER = design_doc
CONFIGS_SRCDIR = sku

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: clean
clean:
	rm -rf $(BUILDDIR)
	find . -type l -exec rm -f {} \;
	find . -type f -name '*.pyc' -exec rm -f {} \;
	find . -type f -name '*.lnk' -exec rm -f {} \;
	find . -type f -name '*.stackdump' -exec rm -f {} \;
	rm -rf $(GITHUBDIR)

.PHONY: livehtml
livehtml:
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	sphinx-autobuild -aE -b html --re-ignore $(SOURCEDIR)/jinja_contexts.txt "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)

.PHONY: github
github:
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(GITHUBDIR)/html" $(SPHINXOPTS) $(O)

.PHONY: confluence
confluence:
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@$(SPHINXBUILD) -aE -b confluence "$(SOURCEDIR)" "$(BUILDDIR)/confluence" $(SPHINXOPTS) $(O)

.PHONY: latexpdf
latexpdf:
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: epub3
epub3: links
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	$(SPHINXBUILD) -b epub3 "$(SOURCEDIR)" "$(BUILDDIR)/epub3" $(SPHINXOPTS) $(O)

.PHONY: rinoh
rinoh:
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@$(SPHINXBUILD) -b rinoh "$(SOURCEDIR)" "$(BUILDDIR)/rinoh" $(SPHINXOPTS) $(O)
