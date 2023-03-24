import pandas

raw_data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray = raw_data[raw_data["Primary Fur Color"] == "Gray"].count()
black = raw_data[raw_data["Primary Fur Color"] == "Black"].count()
cinnamon = raw_data[raw_data["Primary Fur Color"] == "Cinnamon"].count()


final_data = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray["Primary Fur Color"], black["Primary Fur Color"], cinnamon["Primary Fur Color"]]
}
new_csv = pandas.DataFrame(final_data)
new_csv.to_csv("squirrel_count.csv")