def m(s1, s2):
    if s1 == s2:
        return 0
    else:
        return 1


def calculate_lev_dist(string1, string2):
    d = []
    rows_number =  len(string1) + 1
    columns_numb = len(string2) + 1
    row = []
    for i in range(rows_number):
        for j in range(columns_numb):
            if i == 0 and j == 0:
                row.append(0)
            elif i > 0 and j == 0:
                row.append(i)
            elif i == 0 and j > 0:
                row.append(j)
            elif i > 0 and j > 0:
                row.append(min(row[j-1] + 1, d[i-1][j] + 1, d[i-1][j-1] + m(string1[i-1], string2[j-1])))
#        print(row)
        d.append(row[0: columns_numb])
        row.clear()

    return(d[rows_number-1][columns_numb-1])



string1 = "exponential"
string2 = "polynomial"
print("The Levenstein distance between the following words:", string1, "and", string2, "is", calculate_lev_dist("exponential","polynomial"))