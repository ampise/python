from datetime import datetime
start_time = datetime.now()
import os, math
os.system("clear")

sum = 0
for n in range(25, 51):
    # Adding all numbers
    sum = sum + n
# Print total
print(sum)

print("\n--- Program ran for: {} ---".format(datetime.now() - start_time))