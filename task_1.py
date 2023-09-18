import math
x1 = 62
x1_approx = 7.87
x2 = 7/12
x2_approx = 0.318
def precision(x1, x1_approx, x2, x2_approx):
    rel_error_x1 = abs((math.sqrt(x1) - x1_approx)/math.sqrt(x1))
    rel_error_x2 = abs((x2 - x2_approx)/x2)
    if(rel_error_x1 > rel_error_x2):
        print("Рівність номер 2 ночніша")
    elif(rel_error_x1 < rel_error_x2):
        print("Рівність номер 1 ночніша")
    else:
        print("Рівнoсті мають однакову точність")
precision(x1, x1_approx, x2, x2_approx)