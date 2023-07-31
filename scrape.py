from recipe_scrapers import scrape_me
import sys
from os import listdir
from os.path import isfile, join

path = "./env/lib/python3.11/site-packages/recipe_scrapers"
supported_sites = [f.replace(".py", "") for f in listdir(path) if isfile(join(path, f))]

target = sys.argv[1]

wild = True
for site in supported_sites:
    if site in target:
        wild = False

try:
    scraper = scrape_me(target, wild_mode=wild)
    print(f"{scraper.title()}::")
    print(f"[Original Recipe]({target})")
    print("\n\n\n")
    print(f"[Image]({scraper.image()})")
    print("\n\n\n")
    print(f"Total time:\n{scraper.total_time()} minutes")
    print("\n\n\n")
    print("## Ingredients\n")
    for ingredient in scraper.ingredients():
        print(f"* {ingredient}")
    print("\n\n\n")
    print("## Steps\n")
    print(scraper.instructions().replace("\n", "\n\n\n\n\n"))
except:
    print("Error::")
    print("This site is not supported.\n\n\n\n")
    print(f"[JustTheRecipe Link](https://www.justtherecipe.com/?url={target})")

