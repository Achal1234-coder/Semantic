import json
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Pharma
import csv
import _json

def calculation(request, year, data):


     with open('static/csv/PharmaSales.csv', mode='r') as file:
        pharma_file = csv.DictReader(file)
        prev_year = str(int(year) - 1)
        if request.method == "GET":

            drug = data
            if drug == 'M':
                drug_classification = "Musculo-Skeletal System Drugs"
                atc_value = ['m01ab', 'm01ae']
                dict_atc_value = {'m01ab': 0, 'm01ae':0}
                prev_year = str(int(year) - 1)
                prev_dict_atc_value = {'m01ab': 0, 'm01ae':0}

            if drug == 'N':
                drug_classification = "Nervous System Drugs"
                atc_value = ['n02ba', 'n02be', 'n05b', 'n05c']
                dict_atc_value = {'n02ba':0,'n02be':0, 'n05b': 0, 'n05c':0}
                prev_year = str(int(year) - 1)
                prev_dict_atc_value = {'n02ba':0,'n02be':0, 'n05b': 0, 'n05c':0}

            if drug == 'R':
                drug_classification = "Respiratory System Drugs"
                atc_value = ['r03', 'r06']
                dict_atc_value = {'r03':0,'r06':0}
                prev_year = str(int(year) - 1)
                prev_dict_atc_value = {'r03':0,'r06':0}

            for dict in pharma_file:

                if dict['year'] == year:
                    for atc in atc_value:
                        dict_atc_value[atc] += float(dict[atc])

                elif dict['year'] == prev_year:
                     for atc in atc_value:
                        prev_dict_atc_value[atc] += float(dict[atc])

            for atc in atc_value:
                if dict_atc_value[atc] == 0:
                    dict_atc_value[atc] = 'NA'
                if prev_dict_atc_value[atc] == 0:
                    prev_dict_atc_value[atc] = 'NA'

            dictionary = {drug_classification: {value.upper(): {year: dict_atc_value[value], prev_year: prev_dict_atc_value[value]} for value in atc_value}}

            dump = json.dumps(dictionary)

            return HttpResponse(dump, content_type='application/json')

        return HttpResponse("File is not Open")
