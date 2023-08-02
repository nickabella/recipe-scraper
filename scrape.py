import sys, requests
from os import listdir
from os.path import isfile, join
from recipe_scrapers import scrape_me, scrape_html

def print_recipe(title, target, image, time, ingredients, instructions):
    print(f"{title}::")
    print(f"[Original Recipe]({target})")
    print("\n\n\n")
    print(f"[Image]({image})")
    print("\n\n\n")
    print(f"Total time:\n{time} minutes")
    print("\n\n\n")
    print("## Ingredients\n")
    for ingredient in ingredients: 
        print(f"* {ingredient}")
    print("\n\n\n")
    print("## Steps\n")
    print(instructions.replace("\n", "\n\n\n\n\n"))

def main():
    path = "./env/lib/python3.11/site-packages/recipe_scrapers"
    supported_sites = [f.replace(".py", "") for f in listdir(path) if isfile(join(path, f))]

    target = sys.argv[1]

    wild = True
    for site in supported_sites:
        if site in target:
            wild = False

    try:
        scraper = scrape_me(target, wild_mode=wild)
        print_recipe(scraper.title(), target, scraper.image(), scraper.total_time(), \
                scraper.ingredients(), scraper.instructions())
    except:
        try:
            html = requests.get(target).content
            scraper = scrape_html(html=html, org_url=target)
            print_recipe(scraper.title(), target, scraper.image(), scraper.total_time(), \
                scraper.ingredients(), scraper.instructions())
        except:        
            print("Error::")
            print("This site is not supported.\n\n\n\n")
            print(f"[Original Link]({target})\n\n\n\n")
            print(f"[JustTheRecipe Link](https://www.justtherecipe.com/?url={target})")

if __name__ == "__main__":
    main()
