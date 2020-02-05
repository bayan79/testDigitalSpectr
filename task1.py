import re

l_test = ["А123АА11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12", 
          "В999ВВ45", # + ok 
          "FF54120F", # - wrong letters
          "А101AA55", # - wrong region code 
          "В000РС98", # - zero  number
          "В123РС00"] # - zero region code
l_result = []

s_num_format = r"^[АВЕКМНОРСТУХ](?!000)\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$"

# List of possible region codes
l_region_codes = list(range(1, 100)) + [102, 113, 116, 121, 123, 124, 125, 126, 
     134, 136, 138, 142, 150, 152, 154, 159, 161, 163, 164, 173, 174, 177, 178, 
     186, 190, 196, 197, 199, 277, 299, 716, 725, 750, 763, 777, 790, 799]

def check_num(num):
    if re.match(s_num_format, num): 
        return int(re.search("\d+$", num).group()) in l_region_codes
    return False

for num in l_test:
    if check_num(num):
        l_result.append(num)

print(l_result)
