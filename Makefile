doc:
	rm -rf ./html && pdoc --html --force  oceanex_py3

test:
	pytest -s

clean:
	rm -rf ./html
