#! /usr/bin/env python3
import sys
import os
import subprocess


def main():

    in_folder = sys.argv[1]
    out_folder = sys.argv[2]

    directory = os.fsencode(in_folder)

    for file in os.listdir(directory):
         filename = os.fsdecode(file)
         parse_file(in_folder + '/' + filename, out_folder)


def parse_file(file, dest):

    with open(file) as input:
        read_data = input.readline()
        while not '(":" denotes' in read_data:
            read_data = input.readline()
        if '(":" denotes' in read_data:
            first = input.readline()
            gaps = input.readline()
            second = input.readline()

    input.close()
    print(first)
    print(second)

    first_unali = first.replace("-", "")
    second_unali = second.replace("-", "")

    seq1 = []
    seq2 = []
    count1 = 0
    count2 = 0
    for i in range(0, len(first)):
        if first[i] != "-":
            count1 += 1
        if second[i] != "-":
            count2 += 1
        if first[i] != "-" and second[i] != "-":
            seq1.append(count1)
            seq2.append(count2)
    name = file.split(".")[0].split("/")[-1]
    output = open(dest + name + '.atab', "w")
    output.write(">A3M\n")
    output.write("missing dssp\n")
    output.write("\t i \t j\n")
    for j in range(0, len(seq1)):
        output.write("\t " + str(seq1[j]) + " \t " + str(seq2[j]) + "\n")
    output.close()

if __name__ == "__main__":
    main()
