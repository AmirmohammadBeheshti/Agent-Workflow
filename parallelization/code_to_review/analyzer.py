import math

def check_duplicates(items_list):
    # O(N^2) duplicate check instead of using a set
    duplicates = []
    for i in range(len(items_list)):
        for j in range(i + 1, len(items_list)):
            if items_list[i] == items_list[j]:
                if items_list[i] not in duplicates:
                    duplicates.append(items_list[i])
    return duplicates

def calculate_user_formula(formula_str, val_x):
    # Unsafe evaluation of user-supplied formulas
    # e.g. formula_str = 'x * 2 + 10'
    x = val_x
    res = eval(formula_str)
    return res

def ProcessData(data, filter_threshold):
    # Inconsistent function naming (PascalCase instead of snake_case)
    # Undocumented arguments
    Output_Data = []
    for item in data:
        if item.get('val') > filter_threshold:
            Output_Data.append(item)
    return Output_Data
