
import os
import sys
import re
import csv


def go_to_first_page(f):
    """Go to first page"""
    for line in f:
        m = re.search("^*([0-9]+)$", line)
        if m is not None:
            if int(m.groups()[0]) == 1:
                break

def next_article(f):
    """Get article"""
    next_article_number = -1
    article = ""
    for line in f:
        m = re.search("^*([0-9]+)$", line)
        if m is not None:
            article_number = int(m.groups()[0])
            return (article_number, article)
        article += line

def possible_routes(article):
    """Extract possible routes for article"""
    tmp = []

    def look_for_vous(line):
        m = re.search("-vous", line, re.IGNORECASE)
        return(m is not None)

    flag_vous = False
    for line in article.split("\n"):
        if look_for_vous(line):
            flag_vous = True
        
        if flag_vous:
            m = [int(x) for x in re.findall("([0-9]+)\.", line)]
            tmp = tmp + m 

            m = [int(x) for x in re.findall("([0-9]+)\)", line)]
            tmp = tmp + m 

    return(tmp)


filename = sys.argv[1]
nodes_filename = "horreur_vallee_nodes.csv"
edges_filename = "horreur_vallee_edges.csv"

with open(nodes_filename, "w", newline = "\n", encoding = "utf-8") as nodes_outfile:
    nodewriter = csv.writer(nodes_outfile, delimiter = ";", quotechar="|",
                            quoting=csv.QUOTE_MINIMAL)
    nodewriter.writerow(["Node_ID"])

    with open(edges_filename, "w", newline = "\n", encoding = "utf-8") as edges_outfile:
        edgewriter = csv.writer(edges_outfile, delimiter = ";", quotechar = "|", 
                                quoting=csv.QUOTE_MINIMAL)
        edgewriter.writerow(["Source_ID", "Destination_ID"])

        with open(filename, "r") as infile:
            
            i = 0
            go_to_first_page(infile)

            while True:
                nodewriter.writerow(["%d" % (i+1)])

                data = next_article(infile)

                if data is None:
                    break

                i += 1

                article_number, article = data

                for destination_id in possible_routes(article):
                    edgewriter.writerow(["%d" % i, "%d" % destination_id])


