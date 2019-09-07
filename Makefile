docs:
	rm -rf doc && pdoc --html --output-dir html --force oceanex_py3 && mv html/oceanex_py3 doc/ && rm -rf html

test:
	pytest -s

clean:
	rm -rf ./html
