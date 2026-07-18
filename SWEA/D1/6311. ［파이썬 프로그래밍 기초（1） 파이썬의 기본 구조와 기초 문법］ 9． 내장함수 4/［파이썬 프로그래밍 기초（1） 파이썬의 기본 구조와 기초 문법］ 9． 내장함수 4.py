s = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
trans = lambda s: {"A": 4, "B": 3, "C": 2, "D": 1}[s]
print(sum(list(map(trans, s))))