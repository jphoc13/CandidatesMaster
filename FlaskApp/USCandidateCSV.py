import csv
import json
import logging

candidates_list_aggregate = list()


class Field:
    def __init__(self, name):
        self.name = name

fields = [
    Field("Link"),
    Field("Candidate ID"),
    Field("Candidate Name"),
    Field("can_off"),
    Field("State"),
    Field("District"),
    Field("Party"),
    Field("can_inc_cha_ope_sea"),
    Field("can_str1"),
    Field("can_str2"),
    Field("can_cit"),
    Field("can_sta"),
    Field("can_zip"),
    Field("ind_ite_con"),
    Field("ind_uni_con"),
    Field("ind_con"),
    Field("par_com_con"),
    Field("oth_com_con"),
    Field("can_con"),
    Field("tot_con"),
    Field("tra_fro_oth_aut_com"),
    Field("can_loa"),
    Field("oth_loa"),
    Field("tot_loa"),
    Field("off_to_ope_exp"),
    Field("off_to_fun"),
    Field("off_to_leg_acc"),
    Field("oth_rec"),
    Field("Total Received"),
    Field("ope_exp"),
    Field("exe_leg_acc_dis"),
    Field("fun_dis"),
    Field("tra_to_oth_aut_com"),
    Field("can_loa_rep"),
    Field("oth_loa_rep"),
    Field("tot_loa_rep"),
    Field("ind_ref"),
    Field("par_com_ref"),
    Field("oth_com_ref"),
    Field("tot_con_ref"),
    Field("oth_dis"),
    Field("tot_dis"),
    Field("cas_on_han_beg_of_per"),
    Field("cas_on_han_clo_of_per"),
    Field("net_con"),
    Field("net_ope_exp"),
    Field("deb_owe_by_com"),
    Field("deb_owe_to_com"),
    Field("cov_sta_dat"),
    Field("cov_end_dat")
]
def open_CSV():
    with open('CandidateSummaryAction .csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, quotechar='"', delimiter=',')
        firstline = True
        row_count = 0
        columns_to_add = [2,4,5,6,28]
        candidates_list_aggregate.clear()
        for row in spamreader:
            if firstline:
                firstline = False
                continue
            try:
                col_count = 0
                candidate_list = []
                for column in row:
                    if col_count < len(row):
                        if col_count in columns_to_add:
                            if column == "":
                                column = "$0"
                            candidate_list.append(column)
                        col_count += 1
                candidates_list_aggregate.append(candidate_list)
                row_count += 1
            except:
                print("Error")
    return str(json.dumps(candidates_list_aggregate))

def sort_CSV(header):
    print("HEADER: " + str(header))
    candidates_list = json.loads(open_CSV())
    headers = {"Candidate Name": 0, "State": 1, "District": 2, "Party": 3, "Total Received": 4}
    header = header.decode('UTF-8').replace('"', '')
    key = headers[str(header)]
    if key == 4:
        candidates_list = sorted(candidates_list, key=lambda x: float(x[key][1:].replace(',', '')), reverse=True)
    else:
        candidates_list = sorted(candidates_list, key=lambda x: x[key])
    return str(json.dumps(candidates_list))

open_CSV()
#sort_CSV()
