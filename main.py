import re
from pyexcel_ods import save_data
from collections import OrderedDict
import pyexcel
def get_data():
    pattern = "\d{1,3}\tiPhone (\d{1,2})?\w{1,2}?\+?\s?\t?(Pro Max)?(Pro)?(mini)?(Max)?\s?\t?LCD\s(Black|White)\sAFTERMARKET\s\d{1,2}"

    filtered_list = []
    with open("inv_test.txt") as file: # Use file to refer to the file object

       document = file.read().split("\n")

       for line in document:
           if re.search(pattern, line):
               # line = line.replace("\t", " ")

               model_pattern = "iPhone \w{1,2}\+?\s(mini)?(Pro)?\s?(Max)?"
               model = re.search(model_pattern, line).group()

               color_pattern = "Black|White"
               color = re.search(color_pattern, line).group()

               quanty_pattern = "(?<=\t)-?\d{1,3}"
               quanty = re.search(quanty_pattern, line).group()





               filtered_list.append([model, color, quanty])


    return filtered_list

print(get_data())

inventory = get_data()
# data = OrderedDict()
sheet = pyexcel.Sheet(inventory)
# # data.update({"Sheet 1": [["Model", "Color", "OnHand", "Front", "Back", "Difference"]]})
# # for entry in inventory:
# #     # print(entry)
# #     model = entry[1] + " " + entry[2]
# #     # print(model)
# #     data.update({"Sheet 1": [[model, entry[3], entry[2]]]})
sheet.save_as("Inventory.ods")
# save_data("Inventory.ods", data)

# def write_to_spreadsheet(data):
#
#     workbook = Workbook(FileFormatType.ODS)
#
#     # Access the first worksheet of the workbook.
#     worksheet = workbook.getWorksheets().get(0)
#
#     # // Get the desired cell(s) of the worksheet and input the value into the cell(s).
#     worksheet.getCells().get("A1").putValue("ColumnA")
#     worksheet.getCells().get("B1").putValue("ColumnB")
#     worksheet.getCells().get("A2").putValue("ValueA")
#     worksheet.getCells().get("B2").putValue("ValueB")
#
#     # // Save the workbook as ODS file.
#     workbook.save(self.dataDir + "book.default.out.output.ods")
#     print(workbook)
#     jpype.shutdownJVM()
#
# write_to_spreadsheet()
