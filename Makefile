
build: 
	rm -rf dist/
	python setup.py sdist

push_test:
	twine upload -r testpypi dist/*.tar.gz

push_prod:
	twine upload dist/*.tar.gz