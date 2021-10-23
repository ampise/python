from datetime import datetime
start_time = datetime.now()
import os, math
os.system("clear")

attempts = 100000000
for n in range(2, attempts):
    if math.pow(n, 1/2) == math.pow(n, 1/3) == math.pow(n, 1/4):
        print("Found. It is " + str(n))
        break
print("Done. Nothing found after " + str(attempts) + " attempts.")

print("\n--- Program ran for: {} ---".format(datetime.now() - start_time))