
import gzip
import glob, os


path = "C:/Users/Shengrui/Downloads/Trial1/Wearable_Data/files/raw/"




for counter, file in enumerate(glob.glob(path+"*/*.gz")):
   if os.path.isdir(file) == False:
        outputfile = file[:-3]
        

        # uncompress the file
        inF = gzip.open(file, 'rb')
        outF = open( outputfile , 'wb')
        outF.write( inF.read() )
        inF.close()
        outF.close()

