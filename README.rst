Tplan
-----

Tplan calculates a business plan in a troff document.

From a set of datas (products, salaries, operating expenses, loans, grants...),
Tplan calculates an operating result, a working capital and a cash flow.

With a traditional office suite, people use a spreadsheet to calculate their
business plan, and copy-paste the result in their document. Tplan does the same
for troff: datas are fetched from the troff document, and resulting tables are
written in there.

Dependencies
------------

Tplan uses tbl.tmac from neatroff_make to format the tables.
https://github.com/aligrudi/neatroff_make

Installation
------------

The provided makefile will install tplan locally (usually in $HOME/.local/bin).
It understands the following targets:

	$ make test
	$ make install
	$ make uninstall
	$ make test.tr
	$ make test.pdf
	$ make clean
