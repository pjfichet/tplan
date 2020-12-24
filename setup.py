from setuptools import setup

setup(
	name = "tplan",
	description = "Calculates business plans",
	version = "0.2",
	url = None,
	author = "Pierre-Jean Fichet",
	author_email = None,
	license = 'MIT',
	packages = ["tplan",],
	zip_safe = False,
	entry_points={
		'console_scripts': ['tplan=tplan.script:main',],
	},
	python_requires=">=3.7"
)
	
	
