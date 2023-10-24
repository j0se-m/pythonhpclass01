# name="Joseph"
#
# for i in name:
#     if i!=0:
#         print(i)

fruits=["Mangoes","Oranges","Apples"]

try:
    for i in range(6):
        print(f"the index and element from the fruit list is {i,fruits[i]}")

except:
    print("index out of  range")

nambari=[4,5,6,7]

if len(nambari)>3:
    raise Exception(f"Length of the given list must be less or equal to 3  but its {len(nambari)}")
