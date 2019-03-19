#!/usr/bin/env python
# coding=utf-8
import json
import urllib
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, default="test",
                    help="input train data file")
parser.add_argument("--output", type=str, default="test",
                    help="output bert train data file")

arg = parser.parse_args()

input_file = open(arg.input)
output_file = open(arg.output, "w")

linenum = 0
query_set = set()
for line in input_file.readlines():
    linenum = linenum + 1
    if linenum % 10000 == 0:
        print("linenum = " + str(linenum))
    train_data_one = json.loads(line)
    query = train_data_one["query"]
    if query in query_set:
        continue
    query_set.add(query)
    output_file.write(train_data_one["query"] + "#" +
                      train_data_one["task"] + "#" +
                      train_data_one["response"]["states"]["semantic"]["intent"] + "#")
    if "slots" in train_data_one["response"]["states"]["semantic"]:
        output_file.write(json.dumps(
            train_data_one["response"]["states"]["semantic"]["slots"], ensure_ascii=False) + "#" +
            str(train_data_one["response"]["states"]["semantic"]["confidence"]) + "\n")

input_file.close()
output_file.close()

