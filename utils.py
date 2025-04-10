import fitz # type: ignore
import os

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ''
    for page in doc:
        text += page.get_text()
    return text

def process_text(pdf_text, names):
    info_list = pdf_text.split('\n')

    result = {}
    current_name = None
    total_index = info_list.index('Total') + 1
    result['total'] = float(info_list[total_index].replace('$', '').strip())

    for i in range(len(info_list)):
        line = info_list[i]
        if any(name==line for name in names):
            current_name = line.strip()
            if current_name not in result:
                result[current_name] = 0
        elif line.isdigit() and i + 2 < len(info_list) and '$' in info_list[i + 2]:
            price = float(info_list[i + 2].replace('$', '').strip())
            if current_name:
                result[current_name] += price
    return result

def scale_charges(charge_dict):
    total = charge_dict['total']
    subtotal = 0
    for name, amount in charge_dict.items():
        if name != 'total':
            subtotal += amount
    for name, amount in charge_dict.items():
        if name != 'total':
            charge_dict[name] = amount / subtotal * total
    return charge_dict

def calculate_charges(charge_dicts):
    charges = {}
    for cd in charge_dicts:
        scale_charges(cd)
        for name, amount in cd.items():
            if name not in charges:
                charges[name] = 0
            charges[name] += amount
    return charges

def create_charges(paths, names):
    charge_dicts = []
    for path in paths:
        pdf_text = extract_text(path)
        charge_dict = process_text(pdf_text, names)
        charge_dicts.append(charge_dict)
    return calculate_charges(charge_dicts)
    
