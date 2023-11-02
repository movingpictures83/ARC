import sys
from ARC import ARC
from ARC_gviet import ARC_gviet

if __name__ == "__main__" :
    #if len(sys.argv) < 2 :
    #    print("Error: Must supply cache size.")
    #    print("usage: python3 [cache_size]")
    #    exit(1)

    n = int(sys.argv[1])
    print("cache size ", n)
    infile = open(sys.argv[2], 'r')
    #marking = ARC({'cache_size':n})
    marking = ARC_gviet(n)
    page_fault_count = 0
    page_count = 0
    for line in infile:
        print("request: ", line)
        if marking.request(line) :
            page_fault_count += 1
        page_count += 1


    print("page count = ", page_count)
    print("page faults = ", page_fault_count)
