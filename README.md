# README

## About
Utilize [recipe-scraper](https://github.com/hhursev/recipe-scrapers) for use in an iOS shortcut.

## Execution
Code checks if the supplied recipe website is supported or not.

If no, Wild card is True.

If it returns an error, a link to [JustTheRecipe](https://www.justtherecipe.com/) is returned.

Once shortcut is complete, a new Apple Note is created and the text is copied to the clipboard for pasting which maintains the markdown-to-rich-text.

## Installation

1. Download/fork/clone project

2. Create "env" local environment:

```sh
python3 -m venv env
```

3. Then install dependency:

```sh
pip install recipe_scrapers
```

4. Run + supply URL

```sh
python scrape.py https://recipe.com/recipe
```
