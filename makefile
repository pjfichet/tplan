NAME=tplan
BINDIR=$(HOME)/.local/bin


test: $(NAME) $(NAME)/test/test.tr
	python -m unittest $(NAME).test.test_all

install: $(NAME)
	pip install --user .

uninstall:
	pip uninstall $(NAME)

test.tr: $(NAME)/test/test.tr
	$(NAME) $< > $@

test.pdf: test.tr
	$(BINDIR)/roff -mu-tbl $< | $(BINDIR)/pdf > test.pdf

clean:
	rm -f test.pdf test.tr

.PHONY: test install uninstall clean
