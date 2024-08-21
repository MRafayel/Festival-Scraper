import lxml
import requests
from bs4 import BeautifulSoup
import json
from config import URL, headers


fest_list_result = []
count = 0
for i in range(0, 36, 8):
    url = URL.replace("changeable_offset", f'{i}')

    response = requests.get(url=url, headers=headers)
    json_data = json.loads(response.text)
    result = json_data.get("results")
    with open(f"data/index_{i}.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    with open(f"data/index_{i}.json", encoding="utf-8") as file:
        page_data = json.load(file)

    for index, item in enumerate(page_data):
        #extracting location url
        try:
            fest_url = page_data[index].get("link")
            response = requests.get(url=fest_url, headers=headers)
            src = response.text

            with open(f"data/fest_index_{i}.html", "w", encoding="utf-8") as file:
                file.write(src)

            with open(f"data/fest_index_{i}.html", encoding="utf-8") as file:
                src = file.read()

            soup = BeautifulSoup(src, "lxml")

            block_hrefs = soup.find("div", class_="MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2 css-1ik2gjq").select \
                ("a[href]", class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-16jpb7r")
            #location link
            location_url = block_hrefs[0].get("href")
        except Exception as err:
            location_url = None
            print(f"#No contact information ☹")

        #info we need from exact site
        fest_name = item.get("eventname", None)
        fest_date = item.get("date", None)
        fest_location = location_url

        if fest_location is not None:
            try:
                response = requests.get(url=fest_location, headers=headers)
                src = response.text

                soup = BeautifulSoup(src, "lxml")

                contact_details_info = soup.find("h2", string="Venue contact details and info").find_next()

                items = [item.text for item in contact_details_info.find_all('p')]

                all_info_dict = {}
                for info in items:
                    info_list = info.split(":")

                    if len(info_list) == 3:
                        all_info_dict[info_list[0].strip()] = info_list[1].strip() + ":"\
                                                              + info_list[2].strip()
                    elif info_list[1] in {'', ' ', '.', '...'}:
                        all_info_dict[info_list[0].strip()] = "None"
                    else:
                        all_info_dict[info_list[0].strip()] = info_list[1].strip()
                count += 1
                print(f"{count} Info was recorded")
                print(f"location: {fest_location}")

                fest_list_result.append(
                    {
                        "Fest Name": fest_name,
                        "Fest Date": fest_date,
                        "Info Data": all_info_dict
                    }
                )

            except Exception as err:
                print(f"{err}")
        else:
            continue

print(f"{len(fest_list_result)} was recorded successfully")
with open("fest_list_result.json", "w", encoding="utf-8") as file:
    json.dump(fest_list_result, file, indent=4, ensure_ascii=False)