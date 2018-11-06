import urllib3
from bs4 import BeautifulSoup
"""WHy is the list not changing?  How to get the candidates name out of Funds Raised."""
class Field:
    def __init__(self, name):
        self.name = name

client_list = [
    Field('District'),
    Field('Total_Candidates'),
    Field('Candidates'),
    Field('Total_Funds_In_Race'),
    Field('Dem_Candidates'),
    Field('Funds_Raised'),
    Field('Rep_Candidates'),
    Field('Funds_Raised'),
    Field('Dem_Ind_Expenditures_Supporting'),
    Field('Dem_Ind_Expenditures_Opposing'),
    Field('Rep_Ind_Expenditures_Supporting'),
    Field('Rep_Ind_Expenditures_Supporting'),
    Field('Rep_Ind_Expenditures_Opposing'),
]
# (i) indicates an incumbent candidate.
#print(soup.get_text()) Gets all text from a page
http = urllib3.PoolManager()
path = "https://illinoissunshine.org/contested-races/"
response = http.request('GET', path)
soup = BeautifulSoup(response.data, "html.parser")
table = soup.find("table", attrs={"class": "table table-striped table-hover table-border"})
data = table.find_all("td")
candidate_dict = dict()
candidate_list = []
key = ""
data_array = []
do_not_add_list = ['Democratic Candidates', 'Funds Raised', 'Ind. Expenditures Supporting', 'Ind. Expenditures Opposing',
                   'Republican Candidates', 'Total Funds from Primary Challengers']
count = 0
name = ""
for d in data:
    try:
        if "House District" in d.text:
            fld = client_list[0]
            client_list[0] = {fld.name: d.text.strip()}
            count = 1
        else:
            for string in d.stripped_strings:
                if string in do_not_add_list:
                    continue
                fld = client_list[count]
                if "$0.00" in string:
                    value = ""
                else:
                    value = string.replace(" ", "").replace("\n", "").replace("\xa0", "")
                client_list[count] = {fld.name: value}
                count += 1
        candidate_list.append(client_list)
    except:
        pass
for can in candidate_list:
    print(str(can))
# for d in data:
#     if "House District" in d.text:
#         key = d.text.strip()
#         data_array = []
#         candidate_dict.update({key: data_array})
#     else:
#         if "&nbsp;" not in d.text:
#             if d.stripped_strings:
#                 for string in d.stripped_strings:
#                     if string in do_not_add_list:
#                         continue
#                     data_array.append(string.replace(" ", "").replace("\n", "").replace("\xa0", "").replace("&nbsp;", ""))
#                     candidate_dict[key] = data_array
#
#             else:
#                 data_array.append(d.text.replace(" ", "").replace("\n", "").replace("\xa0", "").replace("&nbsp;", ""))
#                 candidate_dict[key] = data_array
# for cand in candidate_list:
#     print(cand)
# for key, value in candidate_dict.items():
#     print(key + " " + str(value))

# for child in table.descendants:
#
#     try:
#         print(child.text.strip())
#     except:
#         pass
# while name_box.find_next_sibling("td") is not None:
#     print(name_box.text)
#     next_sib = name_box.find_next_sibling("td")
#     print(next_sib.text)
#
#     name_box = name_box.find_next_sibling("td")


# print(name_box.text)
# print(next_name_box.text)

# for names in all_names:
#     print(names.text.strip())
#     print(aggregate_donations_all[i].text.strip())
#     i += 2
#print(soup)
#nt(all_names)