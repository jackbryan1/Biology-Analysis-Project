CSC1034: Practical 2
====================

This package allows analysis and display of proteins from Uniprot. To use this program, type 'pipenv run python' and then the name of the file and which function you would like to use. The available functions are: dump, list, average and plot. Dump lists all data, list will list all of the names, average will find the average length of the proteins, plot will produce a graph showing the average length of each taxa, and finally plot_pie will display a pie chart for the total number of proteins in each taxa.

You must also specify the name of the uniprot file in the command line by writing '--filename FILENAMEHERE'. You can also optionally specify the depth when using the plot function by writing '-depth DEPTHHERE'. If depth is not specified it will default to 1.

An example of a command is: 'pipenv run python uniplot.py --filename uniprot_receptor.xml.gz -depth 2, plot'. This would produce a bar chart at depth 2 from the normal data file.
