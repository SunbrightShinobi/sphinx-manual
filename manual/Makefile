# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
COMMONDIR     = ./source/common
COMMONDOCSDIR = ./source/common_docs
CONFIGSDIR    = ./source/configs
IMAGESDIR     = ./source/images
SCRIPTSDIR    = ./source/scripts
GITHUBDIR     = ../docs

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@ln -snf ../../common/				$(COMMONDIR)
	@ln -snf ../../shared/configs		$(CONFIGSDIR)
	@ln -snf ../../shared/docs			$(COMMONDOCSDIR)
	@ln -snf ../../shared/images		$(IMAGESDIR)
	@ln -snf ../../shared/scripts		$(SCRIPTSDIR)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: clean
clean:
	rm -rf $(BUILDDIR)
	find . -type l -exec rm -f {} \;
	find . -type f -name '*.pyc' -exec rm -f {} \;
	find . -type f -name '*.lnk' -exec rm -f {} \;
	find . -type f -name '*.stackdump' -exec rm -f {} \;

.PHONY: livehtml
livehtml:
	@ln -snf ../../common/				$(COMMONDIR)
	@ln -snf ../../shared/configs		$(CONFIGSDIR)
	@ln -snf ../../shared/docs			$(COMMONDOCSDIR)
	@ln -snf ../../shared/images		$(IMAGESDIR)
	@ln -snf ../../shared/scripts		$(SCRIPTSDIR)
	sphinx-autobuild -aE -b html --re-ignore $(SOURCEDIR)/jinja_contexts.txt "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)

.PHONY: github
github:
	@ln -snf ../../common/				$(COMMONDIR)
	@ln -snf ../../shared/configs		$(CONFIGSDIR)
	@ln -snf ../../shared/docs			$(COMMONDOCSDIR)
	@ln -snf ../../shared/images		$(IMAGESDIR)
	@ln -snf ../../shared/scripts		$(SCRIPTSDIR)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)
	@rm -rf $(GITHUBDIR)/*
	@cp -a build/html/. $(GITHUBDIR)

.PHONY: confluence
confluence:
	@ln -snf ../../common/				$(COMMONDIR)
	@ln -snf ../../shared/configs		$(CONFIGSDIR)
	@ln -snf ../../shared/docs			$(COMMONDOCSDIR)
	@ln -snf ../../shared/images		$(IMAGESDIR)
	@ln -snf ../../shared/scripts		$(SCRIPTSDIR)
	@$(SPHINXBUILD) -b confluence "$(SOURCEDIR)" "$(BUILDDIR)/confluence" $(SPHINXOPTS) $(O)
