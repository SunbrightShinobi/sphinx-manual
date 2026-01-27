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
latexpdf: _drawio_pdf
	python3 check_conf.py
	@ln -snf ../../common/_static										$(COMMONDIR)/_static
	@ln -snf ../../common/sphinx_scripts								$(COMMONDIR)/sphinx_scripts
	@ln -snf ../../common/_templates/$(SPHINX_TEMPLATES)				$(COMMONDIR)/_templates
	@ln -snf ../../shared/configs/$(CONFIGS_SRCDIR)						$(CONFIGSDIR)
	@ln -snf ../../shared/docs											$(COMMONDOCSDIR)
	@ln -snf ../../shared/images										$(IMAGESDIR)
	@ln -snf ../../shared/scripts										$(SCRIPTSDIR)
	@ln -snf ../../shared/diagrams										$(DIAGRAMSDIR)
	@LATEXOPTS="-interaction=nonstopmode" $(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) || true
	@mkdir -p "$(BUILDDIR)/latex"
	@for f in $(COMMONDIR)/_static/diagrams/*.pdf; do \
		[ -f "$$f" ] && cp "$$f" "$(BUILDDIR)/latex/" || true; \
	done
	@cd "$(BUILDDIR)/latex" && latexmk -f -pdf -dvi- -ps- -interaction=nonstopmode myproject.tex > /dev/null 2>&1 || true
	@if [ -f "$(BUILDDIR)/latex/myproject.pdf" ]; then echo "PDF generated: $(BUILDDIR)/latex/myproject.pdf"; else echo "ERROR: PDF generation failed"; exit 1; fi

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

# Export all DrawIO diagrams to SVG before builds that need it

_drawio_pdf:
	@echo "Converting DrawIO files to PDF..."
	@mkdir -p source/_static/diagrams/
	@for f in ../shared/diagrams/*.drawio; do \
		basename=$$(basename "$$f" .drawio); \
		echo "Processing $$f..."; \
		drawio "$$f" \
		--export \
		--disable-gpu \
		--disable-software-rasterizer \
		--no-sandbox \
		--format pdf \
		-o "source/_static/diagrams/$$basename.pdf"; \
	done

