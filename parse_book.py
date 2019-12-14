
import os
import sys
import re


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

filename = sys.argv[1]


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
            m = re.findall("[0-9]+", line)
            tmp = tmp + m 

    return(tmp)


with open(filename, "r") as f:
    
    article_number = 1
    go_to_first_page(f)

    next_article_number, article = next_article(f) 
    next_article_number, article = next_article(f) 

    print(possible_routes(article))
