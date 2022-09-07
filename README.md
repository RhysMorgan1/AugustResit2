CSC1034: Resit
==============

This package allows analysis and display of proteins from Uniprot.



Functions

1.) Data Dumping
If you want to see the entirety of the data file that you are using (in our example it is uniprot_receptor.xml.gz)
you can use the command:
    python uniplot.py dump

2.) Data listing
Dumping the data can look incredibly messy however, so in order to see just the proteins
themselves, we can use the command:
    python uniplot.py list

3.) Average Protein list
If you wish to see the average length of the proteins in your specified database, you can
use the command:
    python uniplot.py average

4.) Display average using a bar chart
You're able to see the average length of different taxas by using the command:
    python uniplot.py plot-taxa

5.) Displaying different depths using a bar chart
In order to see different levels of taxonomy with the bar graph, use the command:
    python uniplot.py plot-taxa --depth 2
With 2 being any integer you like

6.) Displaying this data as a pie graph
You can view this data as a pie chart as well as a bar chart. To do so,
use the command:
    python uniplot.py plot-taxa --depth 2 --pie 1

7.) Saving file location
In order to specify the file location in which you are keeping all of your data,
you can use the command:
    python uniplot.py location FileLocation
where FileLocation is replace by your file's location