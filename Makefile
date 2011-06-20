PYDOCTOR=pydoctor

docs:
	$(PYDOCTOR) --make-html --html-output apidoc --add-package twistar --project-name=twistar --project-url=http://findingscience.com/twistar --html-use-sorttable --html-use-splitlinks --html-shorten-lists 
	lore --config template=doc/template.tpl doc/*.xhtml

test:
	trial twistar

install:
	python setup.py install
