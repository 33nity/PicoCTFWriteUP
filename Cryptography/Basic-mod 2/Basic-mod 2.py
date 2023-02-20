msg = [268, 413, 110, 190, 426, 419, 108, 229, 310, 379, 323, 373, 385, 236, 92, 96, 169, 321, 284, 185, 154, 137, 186]
library = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
for x in msg:
    result = pow(x, -1, 41)
    print(library[result-1])

        