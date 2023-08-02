# README

## About
Utilize [recipe-scraper](https://github.com/hhursev/recipe-scrapers) for use in an iOS shortcut.

## Execution
Code checks if the supplied recipe website is supported or not.

If no, Wild card is True.

If it returns an error, a link to [JustTheRecipe](https://www.justtherecipe.com/) is returned.

Once shortcut is complete, a new Apple Note is created and the text is copied to the clipboard for pasting which maintains the markdown-to-rich-text.

## Installation

### Server

1. Download/fork/clone project

2. Create and activate "env" local environment:

```sh
python3 -m venv env
. ./env/vin/activate
```

3. Then install dependency:

```sh
pip install recipe_scrapers
```

4. Run + supply URL

```sh
python scrape.py https://recipe.com/recipe
```

### iOS Shortcut

1. [Download](https://www.icloud.com/shortcuts/79ba5f80d70841d6b2880edd6fdb2dfc)

2. Edit "Run script over SSH" action
	a. CD to directory where code will be executed on server and invoke script
	b. configure host, port, user, and password
	c. example:
		i. `cd ~/GitHub/recipe-scraper; source ./env/bin/activate; python3 scrape.py Shortcut Input`

3. Run shortcut with link in clipboard or via Share sheet
