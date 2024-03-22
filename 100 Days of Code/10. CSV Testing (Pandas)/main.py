# with open("./10. CSV Testing/weather_data.csv") as csvfile:
#     data = csvfile.readlines()

# print(data)

# instead of this ^
# try this v

# import csv
# with open("./10. CSV Testing (Pandas)/weather_data.csv") as csvfile:
#     data = csv.reader(csvfile)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
    
# print(temperatures)

# instead of this ^
# try this v

import pandas

data = pandas.read_csv("10. CSV Testing (Pandas)\weather_data.csv")
print(data)
# print(data.iloc[3][1])
# print(type(data))
# print(data["temp"]) # pandas menganggap row pertama adalah index penandanya
# print(data.temp)
# print(type(data["temp"])) # pandas menganggap row pertama adalah index penandanya

# data_dict = data.to_dict() # mengconvert sebagai dictionary
# print(len(data_dict["day"]))

# temp_list = data["temp"].tolist()
# print(sum(temp_list) / len(temp_list))
# print("Mean = ",data["temp"].mean())
# print("Median = ",data["temp"].median())
# print("Modus = ",data["temp"].mode())
# print("Max = ",data["temp"].max())

# Get Data in Colomns
# print("pake kurung = ",data["condition"])
# print("ga pake:",data.condition) # pandas will read the file and we can take it/ consider it as Attributes

# Get Data in Row
# ini akan mengeluarkan baris yang memiliki 'day' bernilai Monday
# Monday = data[data.day == "Monday"] 
# mondaytempf = Monday.temp[0]  * 9 / 5 + 32
# # print(mondaytempf) 
# print(Monday,type(Monday)) #disini monday dari read csv ya pasti tipenya dataframe
# print(f"Monday.temp tipe = ",type(Monday.temp)) #disini monday karena udah masuk ke attributenya .tipe ini sama aja kea 
# print(f"Monday.temp[0] tipe = ",type(Monday.temp[0])) #disini monday.temp

# ini akan mengeluarkan baris yang memilki temp max
# print("\n")
# Tempmax = data[data.temp == data.temp.max()]
# print(Tempmax)
# print(type(Tempmax))

# Create a dataframe from scratch
# student_scores_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76,65,56]
# }

# data = pandas.DataFrame(student_scores_dict) # jadiin dataframe dulu baru bisa jadi file baru
# data.to_csv("./10. CSV Testing (Pandas)/new_data.csv") # ini akan membuat file baru dengan data yang sudah kita buat dari python
# print(data)