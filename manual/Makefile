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
DIAGRAMSDIR   = ./source/diagrams
SCRIPTSDIR    = ./source/scripts
GITHUBDIR     = ../docs
SPHINX_TEMPLATES = us_dod
TEMPLATE_FOLDER = design_doc
CONFIGS_SRCDIR = sku

# Export all DrawIO diagrams to SVG before builds that need it
_drawio_svg:
	@echo "Converting DrawIO files to SVG..."
	@mkdir -p source/_static/diagrams
	@for f in ../shared/diagrams/*.drawio; do \
		echo "Processing $$f..."; \
		drawio --export \
		--disable-gpu \
		--disable-software-rasterizer \
		--no-sandbox \
		--output source/_static/diagrams/ \
		--format svg "$$f"; \
	done

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
	@ln -snf ../../shared/diagrams										$(DIAGRAMSDIR)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: clean
clean:
	rm -rf $(BUILDDIR)
	find . -type l -exec rm -f {} \;
	find . -type f -name '*.pyc' -exec rm -f {} \;
	find . -type f -name '*.lnk' -exec rm -f {} \;
	find . -type f -name '*.stackdump' -exec rm -f {} \;

.PHONY: html
html: _drawio_svg
	python3 check_conf.py
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@ln -snf ../../shared/diagrams										$(DIAGRAMSDIR)
	@$(SPHINXBUILD) -aE -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) $(O)

.PHONY: livehtml
livehtml: _drawio_svg
	python3 check_conf.py
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@ln -snf ../../shared/diagrams										$(DIAGRAMSDIR)
	sphinx-autobuild -aE -b html \
	--ignore "source/_static/diagrams/*.svg" \
	--re-ignore "source/jinja_contexts.txt" \
	source \
	build/html

.PHONY: github
github: _drawio_svg
	python3 check_conf.py
	rm -rf $(GITHUBDIR)
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@ln -snf ../../shared/diagrams										$(DIAGRAMSDIR)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(GITHUBDIR)/" $(SPHINXOPTS) $(O)

.PHONY: confluence
confluence: _drawio_svg
	python3 check_conf.py
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@ln -snf ../../shared/diagrams										$(DIAGRAMSDIR)
	@$(SPHINXBUILD) -aE -b confluence "$(SOURCEDIR)" "$(BUILDDIR)/confluence" $(SPHINXOPTS) $(O)

.PHONY: latexpdf
latexpdf: _drawio_svg
	python3 check_conf.py
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@ln -snf ../../shared/diagrams										$(DIAGRAMSDIR)
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: epub3
epub3: links _drawio_svg
	python3 check_conf.py
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@ln -snf ../../shared/diagrams										$(DIAGRAMSDIR)
	$(SPHINXBUILD) -b epub3 "$(SOURCEDIR)" "$(BUILDDIR)/epub3" $(SPHINXOPTS) $(O)

.PHONY: rinoh
rinoh: _drawio_svg
	python3 check_conf.py
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@ln -snf ../../shared/diagrams										$(DIAGRAMSDIR)
	@$(SPHINXBUILD) -b rinoh "$(SOURCEDIR)" "$(BUILDDIR)/rinoh" $(SPHINXOPTS) $(O)
