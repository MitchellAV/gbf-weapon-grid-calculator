import json
from pprint import pprint
import sys
from bs4 import BeautifulSoup, NavigableString, ResultSet, Tag
import requests
import pandas as pd

skill_title_set = set()
weapon_name_set = set()


def scrape_weapon_list_html(filename: str, folder: str = "gbf_wiki") -> pd.DataFrame:
    path = f"{folder}/{filename}"

    with open(path, "r", encoding="utf-8") as fp:
        html = fp.read()

    soup = BeautifulSoup(html, "html.parser")

    # Create a BeautifulSoup object from the HTML
    # soup = BeautifulSoup(html, "html.parser")

    # Get the rows
    weapon_table: Tag = soup.find_all("table", attrs={"class": "wikitable"})[0]

    weapon_rows: ResultSet = weapon_table.find("tbody").find_all(
        "tr"
    )  # 'tr' is the tag for table rows

    # Now, 'table_rows' is a list of all the rows in the table.
    # You can iterate over it to get each row's data:

    # columns = [
    #     "Icon",
    #     "Name",
    #     "Rarity",
    #     "Element",
    #     "Type",
    #     "ATK",
    #     "HP",
    #     "Skills",
    #     "Skills Description",
    # ]

    df = pd.DataFrame()

    def parse_weapon_skill_src(src: str):
        src = src.split(".")[0]
        return src

    for weapon_row in weapon_rows:
        weapon_rarity = weapon_row.attrs["data-filter-rarity"]

        if weapon_rarity != "ssr":
            continue

        weapon_type = weapon_row.attrs["data-filter-type"]
        weapon_element = weapon_row.attrs["data-filter-element"]
        evo_max = weapon_row.attrs["data-filter-evo-max"]

        weapon_cells: ResultSet = weapon_row.find_all(
            "td"
        )  # 'td' is the tag for table data

        weapon_id = weapon_cells[0].find("a")["href"].split("/")[-1]
        icon_url = weapon_cells[0].find("img")["src"]
        name = weapon_cells[1].find("a").text
        element = weapon_cells[3].find("a")["href"].split("/")[-1]
        atk = int(weapon_cells[5].text)
        hp = int(weapon_cells[6].text)
        skills = weapon_cells[7].find_all("img")
        skills = [parse_weapon_skill_src(skill["alt"]) for skill in skills]
        skills = ", ".join(skills)
        skill_td: Tag = weapon_cells[8]

        # Assuming 'skill_td' is the BeautifulSoup object containing the HTML element
        def has_bold_style(tag):
            style = tag.get("style", "")
            return "bold" in style

        skills_descriptions_objects = skill_td.find_all(has_bold_style)

        def parse_skill_title(title: str):
            title = title.split(":")[0]
            return title

        skills_descriptions = [
            parse_skill_title(skill.text) for skill in skills_descriptions_objects
        ]

        skills_titles = skills_descriptions[:-1]

        skill_title_set.update(skills_titles)
        weapon_name_set.add(name)

        pprint(skills_titles)
        # sys.exit()

        row = {
            "ID": weapon_id,
            "URL": f"https://gbf.wiki/{weapon_id}",
            "Element": weapon_element,
            "Rarity": weapon_rarity,
            "Max Evo Level": evo_max,
            "Name": name,
            "Type": weapon_type,
            "ATK": atk,
            "HP": hp,
            "Icon": icon_url,
            "Skills": ", ".join(skills_titles),
            # "Skills Description": skills_description,
        }

        df = pd.concat([df, pd.DataFrame(row, index=[0])], ignore_index=True)

    # pprint(df.to_dict("records")[0])
    return df


# # Get the html from the webpage
# url = "https://www.basketball-reference.com/leagues/NBA_2018_per_game.html"
# response = requests.get(url)
# html = response.content

# Load html from file
folder = "gbf_wiki"
filenames = [
    "Weapon Lists_Fire - Granblue Fantasy Wiki.html",
    "Weapon Lists_Water - Granblue Fantasy Wiki.html",
    "Weapon Lists_Earth - Granblue Fantasy Wiki.html",
    "Weapon Lists_Wind - Granblue Fantasy Wiki.html",
    "Weapon Lists_Light - Granblue Fantasy Wiki.html",
    "Weapon Lists_Dark - Granblue Fantasy Wiki.html",
]


for filename in filenames:
    df = scrape_weapon_list_html(filename, folder=folder)
    element = filename.split("_")[1].split(" ")[0]
    resultPath = f"results/{element}.csv"

    df.to_csv(resultPath, index=False)

# pprint(skill_title_set)

# save skill titles to file
with open("results/skill_titles.json", "w", encoding="utf-8") as fp:
    json_object = {}
    for title in sorted(skill_title_set):
        json_object[title] = ""
    json.dump(json_object, fp, ensure_ascii=False, indent=4)

# save weapon names to file
with open("results/weapon_names.json", "w", encoding="utf-8") as fp:
    json_object = {}
    for title in sorted(weapon_name_set):
        json_object[title] = ""
    json.dump(json_object, fp, ensure_ascii=False, indent=4)
