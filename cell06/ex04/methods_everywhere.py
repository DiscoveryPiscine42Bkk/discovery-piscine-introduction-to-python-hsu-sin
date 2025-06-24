import sys
def shrink(s):
    print(s[:8])
    
def enlarge(s):
    print(s + 'Z' * (8-len(s)))

if len(sys.argv) < 2:
    print("none")

else:
    for i in sys.argv[1:]:
        if len(i) > 8:
            shrink(i)
        elif len(i) < 8:
            enlarge(i)
        else:
            print(i)