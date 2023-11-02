import random
import sys
from disk_struct import Disk
from page_replacement_algorithm import  page_replacement_algorithm
from CacheLinkedList import  CacheLinkedList
import numpy as np

import ARC
import ARC_adaptive
import ARC_gviet
import ARC_gviet2
import ARC_gviet3
import ARC_LEARNING
import ARC_OPT

import PyIO
import PyPluMA

class ARCPlugin:
  def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)

  def run(self):
        pass

  def output(self, outputfile):
    n = int(self.parameters["n"])
    infile = open(PyPluMA.prefix()+"/"+self.parameters["infile"], 'r')
    kind = self.parameters["kind"]
    outfile = open(outputfile, 'w')
    outfile.write("cache size "+str(n))
    if (kind == "ARC"):
       arc = ARC.ARC(n)
    elif (kind == "ARC_adaptive"):
       arc = ARC_adaptive.ARC_adaptive(n)
    elif (kind == "ARC_gviet"):
       arc = ARC_gviet.ARC_gviet(n)
    elif (kind == "ARC_gviet2"):
       arc = ARC_gviet2.ARC_gviet2(n)
    elif (kind == "ARC_gviet3"):
       arc = ARC_gviet3.ARC_gviet3(n)
    elif (kind == "ARC_LEARNING"):
       arc = ARC_LEARNING.ARC_LEARNING(n)
    else:
        arc = ARC_OPT.ARC_OPT(n)
    page_fault_count = 0
    page_count = 0
    for line in infile:
        line = int(line.strip())
        outfile.write("request: "+str(line))
        if arc.request(line) :
            page_fault_count += 1
        page_count += 1

    
    outfile.write("page count = "+str(page_count))
    outfile.write("\n")
    outfile.write("page faults = "+str(page_fault_count))
    outfile.write("\n")
