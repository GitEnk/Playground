import pandas
import requests


data = requests.get("https://data.cityofnewyork.us/resource/vfnx-vebw.json")

pdata = pandas.read_json(data.text)

gray_squirrel_count = len(pdata[pdata.primary_fur_color == "Gray"])
cinnamon_squirrel_count = len(pdata[pdata.primary_fur_color == "Cinnamon"])
black_squirrel_count = len(pdata[pdata.primary_fur_color == "Black"])

data_dict = {
    "Fur_Color":["Gray","Cinnamon", "Black"],
    "count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrels.csv")