"""
remember and understand the procedure to write the whole programe
"""
import sys
import re

def extract_names(filename):
    """ Given a filename for baby.html, returns a list starting with year string
followed by the name_rank strings in a alphabetical order
['2006', 'Aaliyah 91', 'Aaron 57']

"""
    name = []
    #open the file
    f = open(filename, "rU")
    text = f.read()
    #Could process the file line-by line, but regex on the whole text at once is easier
    # read line by line is too slow
    #get the year

    year_match = re.search(r"Popularity\sin\s(\d{4})",text)
    if not year_match:
        # if not find the match, exit with an error message
        sys.stderr.write("could not find the year \n")
        sys.exit(1)

    year = year_match.group(1)
    #here comes the list
    names.append(year)

    
    #print tuples, findall returns tuples, awesome!
    tuples = re.findall(r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>", text)
    #Store data into a dict using each name as key and that the rank number as value
    #(if the name is already in there, do not add it, since the new rank will bigger than
    #the previos one)

    name_to_rank = {}
    for rank_tuple in tuples:
        #here comes the new stuff, remember it
        (rank, boyname, girlname) = rank_tuple
        if boyname not in names_to_rank:
            names_to_rank[boyname] = rank
        if girlname not in names_to_rank:
            name_to_rank[girlname] = rank

    #Get the names, sorted in the aplphabetical order
    # Just sort the keys and do the next operation base on index
    sorted_names = sorted(names_to_rank.keys())

    #Build up result list, one element per line
    for name in sorted_names:
        name.append(name + "  "+ names_to_rank[name])

    return names

def main():

    args = sys.argv[1:]
    # argv[0] is [--summuryfile]

    if not args:
        print "usage: [--summaryfile] file [file...]"
        sys.exit(1)
    #Notice the summary flag and remove it from args if it present
    summary = False
    if args[0] =="--summaryfile":
        summary =True
        del args[0]
    #for each filename, get the name, then either print the text output
    #or write it to a summary file

    # that is why need to del args[0], what we need next are  the filename
    for filename in args:
        names = extract_names(filename)

        #Make text out of the whole list
        text = '\n'.join(names)

        if summary:
            outf = open(filename+ ".summary", "w")
            outf.write(text+ '\n')
            outf.close()
        else:
            print text

if __name__="__main__":
    main()


















            
        
