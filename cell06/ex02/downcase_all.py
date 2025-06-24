import sys

def downcase_all(text):
    return text.lower()

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        print(downcase_all(i))
        
else:
    print("none")