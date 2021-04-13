install:
	python3 -m venv .env
	. .env/bin/activate && pip3 install -r requirements.txt

docs: clean
	rm -rf docs
	. .env/bin/activate && pdoc --html --output-dir html --force oceanex_py3
	mv html/oceanex_py3 docs/ 
	rm -rf html

test:
	. .env/bin/activate && python3 -m pytest -vv -s

clean:
	rm -rf ./docs

publish:
	rm -rf dist/*
	. .env/bin/activate && python3 setup.py sdist bdist_wheel
	. .env/bin/activate && python3 -m twine upload dist/*