#Fec Data Loader
Here is a bit of code I wrote to download data from FEC, de-normalize and de-code it and index it into elastic search for viewing in kibana. 
You can also use the output csv files in pandas without having to do any joins on the data. Note that this is pretty quick and dirty. 

Check out the first analysis here: http://tinyurl.com/nkuwu55

##How to use this:
     1. Download the code
     2. Run build2.py
        This will generate files in the data subdirectory. Generated files will start with an underscore (_). Files are
        _indiv16.csv, _exp16.csv, _pas216.csv. (16 is the dataset year)
     3. Run index_to_es.py (optional)

##Requirements: 
    1. Python 3
    2. elasticsearch-py (pip install elasticsearch) for index_to_es.py
    

##build2.py
Downloads the data from FEC (http://www.fec.gov/finance/disclosure/ftpdet.shtml), de-normalizes the data and writes out data as a csv to the filesystem. These CSVs are perfrect for importing into pandas or another tool. 
By default the script will process the data from the 2016 election cycle. You can adjust this by passing the script the year as an argument. 

For example, this will try to pull data from 2008 election cycle:
./build2.py 2008 

If you pull in legacy data you will also need to pass the year to index_to_es.py


##index_to_es.py
Pulls the csv files from the previous script and loads them into elastic search. It will also create an index called fec as well as all the fields that you will need, with proper type.
Make sure you have succesfully ran the buil2 script before running this.  

 By default this will point to local instance of elastic search. If you want to send this data somewhere else just edit ES_HOST parameter in the script.

##Notes:
There are some inconsistencies with a few values in FEC data translation. The script will print these out to the screen, but due to a relatively low number of them I generally disregard them.
 
 #Legal
 I am not sure how to write legal stuff; but I am not responsible for how you use this. In fact it's probably wrong, I may or may not have been drinking beer when I wrote this. 
 Definitely wrote it on my own time though... as far as I can remember. 