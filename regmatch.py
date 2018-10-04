import re

pattern1 = re.compile(r"My name is (\b.*\b).")
literal1 = "My name is -Dorian-."

pattern2 = re.compile(r"(\b.*\b) (.*) (.*)")
literal2 = "add^map^define =dddddd_table $data99.ddddtabl.dddddd"

matcher1 = re.search(pattern1, literal1)
matcher2 = re.search(pattern2, literal2)

if matcher1:
    print (matcher1.group(1))
else:
    print ("matcher1 failed!")

if matcher2:
    print (matcher2.group(3))
else:
    print ("matcher2 failed!")
