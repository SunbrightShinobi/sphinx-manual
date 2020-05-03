# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
GITHUBDIR     = ../ghpages

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	ln -s ../../common/sphinx_scripts		./source/common
	ln -s ../../common/_static				./source/_static
	ln -s ../../common/_templates			./source/_templates
	ln -s ../../shared/configs				./source/configs
	ln -s ../../shared/scripts				./source/scripts
	ln -s ../../shared/docs					./source/common_docs
	ln -s ../../shared/images				./source/images
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
	ln -s ../../common/sphinx_scripts		./source/common
	ln -s ../../common/_static				./source/_static
	ln -s ../../common/_templates			./source/_templates
	ln -s ../../shared/configs				./source/configs
	ln -s ../../shared/scripts				./source/scripts
	ln -s ../../shared/docs					./source/common_docs
	ln -s ../../shared/images				./source/images
	sphinx-autobuild -b html --poll "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)

.PHONY: github
github:
	ln -s ../../common/sphinx_scripts		./source/common
	ln -s ../../common/_static				./source/_static
	ln -s ../../common/_templates			./source/_templates
	ln -s ../../shared/configs				./source/configs
	ln -s ../../shared/scripts				./source/scripts
	ln -s ../../shared/docs					./source/common_docs
	ln -s ../../shared/images				./source/images
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)
	@rm -rf ../docs/*
	@cp -a build/html/. ../docs
