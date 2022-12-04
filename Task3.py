def delete(list_, index=None):
    if index == None:
        list_fin = list_[:-1]
    else:
        list_fin = list_[:index] + list_[index + 1:]
    return list_fin

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
