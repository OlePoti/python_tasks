#очистка списка от повторений

def clean_list(list_to_claen):
    output_list = []
    for i in list_to_clean:
        for j in output_list:
            if j is i:
                break
        else:
            output_list.append(i)
    return output_list

list_to_clean=['1', 2, 1, '1', 'Qwe', 'qWq', 'Qwe', 2.0, 'QWE', 'Qwe', 1, '1']
print(clean_list(list_to_clean))
