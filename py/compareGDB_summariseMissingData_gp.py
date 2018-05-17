#-------------------------------------------------------------------------------
# Name:        GIS Viewer Attribution Evaluation
# Version:     V_2.0
# Purpose:     Produce report for installation geodatabase detailing data attribution
#
# Author:      Steven Connor Gonzalez
#
# Created:     2018/01/26
# Last Update: 2018/03/22
# Description: Evaluate installation geodatabases for minimum attribution required
#              by AFCEC GIS viewer for best display of data.
#-------------------------------------------------------------------------------

# Import modules
import arcpy, os,  numpy, pandas
from pandas import DataFrame
from datetime import datetime

# Start time
timenow = datetime.now()
print(timenow)



# WHICH FEATURE DATASETS ARE MISSING FROM THE INSTALLATION DATABASE COMPARED TO COMPARISON DATABASE
missFDSTable = arcpy.GetParameterAsText(0)
# WITHIN THE FEATURE DATASETS THAT THE INSTALLATION HAS, 
# WHICH FEATURE CLASSES ARE MISSING?
missFCTable = arcpy.GetParameterAsText(1)

# WITHIN EACH REQUIRED FEATURE DATASET AND FEATURE CLASS THAT THE INSTALLATION HAS, 
# WHICH FIELDS ARE MISSING?
missFLDTable = arcpy.GetParameterAsText(2)
# WITHIN EACH REQUIRED FEATURE DATASET AND FEATURE CLASS THAT THE INSTALLATION HAS, 
# WHICH FIELDS ARE MISSING?

nullTable = arcpy.GetParameterAsText(3)

outputFile = arcpy.GetParameterAsText(4)

# =============================================================================
# missFDSTable = os.path.join(installGDB,"CIP_MissingFDS")
# missFCTable = os.path.join(installGDB,"CIP_MissingFCs")
# missFLDTable = os.path.join(installGDB,"CIP_MissingFields")
# nullTable = os.path.join(installGDB,"CIP_MissingData")
# =============================================================================

# to get dataframe of feature datasets, feature classes, and fields of geodatabase
def getFeaturesdf(GDB):
    '''
    # to get unique FDS, FC, and FIELDS across a geodatabase
    Parameters
    ----------
    GDB = path to GDB
    
    Returns
    -------
    pandas dataframe of with two columns: Feature Dataset, Feature Class for each fc in gdb.
    '''

    d = pandas.DataFrame([])
    arcpy.env.workspace = GDB
    for theFDS in arcpy.ListDatasets():
        for theFC in arcpy.ListFeatureClasses(feature_dataset=theFDS):
            minFields = (fld.name.upper() for fld in arcpy.ListFields(os.path.join(GDB,theFDS,theFC)) if str(fld.name) not in ['Shape', 'OBJECTID', 'Shape_Length', 'Shape_Area'])
            minFields = list(minFields)
            for FLD in minFields:
                d = d.append(pandas.DataFrame({'FDS': str(theFDS), 'FC': str(theFC), 'FLD': str(FLD.name)}, index=[0]), ignore_index=True)
    return(d)
	
# to get field name of a ArcGIS table
def get_field_names(table):
    """
    Get a list of field names not inclusive of the geometry and object id fields.
    
    Parameters
    ----------
    table: Table readable by ArcGIS
    Returns
    -------
    List of field names.
    """
    # list to store values
    field_list = []

    # iterate the fields
    for field in arcpy.ListFields(table):

        # if the field is not geometry nor object id, add it as is
        if field.type != 'Geometry' and field.type != 'OID':
            field_list.append(field.name)

        # if geomtery is present, add both shape x and y for the centroid
        elif field.type == 'Geometry':
            field_list.append('SHAPE@XY')

    # return the field list
    return field_list

# to convert arcgis table to pandas dataframe
def table_to_pandas_dataframe(table, field_names=None):
    """
    Load data into a Pandas Data Frame from esri geodatabase table for subsequent analysis.
    
    Parameters
    ----------
    table = Table readable by ArcGIS.
    field_names: List of fields.
    Returns
    -------
    Pandas DataFrame object.
    
    """
    # if field names are not specified
    if not field_names:

        # get a list of field names
        field_names = get_field_names(table)

    # create a pandas data frame
    dataframe = DataFrame(columns=field_names)

    # use a search cursor to iterate rows
    with arcpy.da.SearchCursor(table, field_names) as search_cursor:

        # iterate the rows
        for row in search_cursor:

            # combine the field names and row items together, and append them
            dataframe = dataframe.append(
                dict(zip(field_names, row)), 
                ignore_index=True
            )

    # return the pandas data frame
    return dataframe

def get_geodatabase_path(input_table):
  '''Return the Geodatabase path from the input table or feature class.
  :param input_table: path to the input table or feature class 
  '''
  workspace = os.path.dirname(input_table)
  if [any(ext) for ext in ('.gdb', '.mdb', '.sde') if ext in os.path.splitext(workspace)]:
    return workspace
  else:
    return os.path.dirname(workspace)

# to get a pandas dataframe into a arcgis table
def pandas_to_table(pddf,tablename):
    '''
    Parameters
    ----------
    pddf = pandas dataframe
    tablename = output table name to 'installGDB'
    
    Returns
    -------
    a geodatabase table from pandas dataframe inside 'installGDB' geodatabase object (string to .gdb path)
    '''
    x = numpy.array(numpy.rec.fromrecords(pddf))
    names = pddf.dtypes.index.tolist()
    x.dtype.names = tuple(names)
    gdbTbl = os.path.join(installGDB,tablename)
    if arcpy.Exists(gdbTbl):
        arcpy.Delete_management(gdbTbl)
    arcpy.da.NumPyArrayToTable(x, gdbTbl)


          
def summariseMissingData(installGDB):
    start_time = datetime.now()
    

    arcpy.env.workspace = installGDB
	    
    installationName = os.path.splitext(os.path.basename(installGDB))[0]
	
    tb =  os.path.splitext(os.path.basename(nullTable))[0]
    compName = tb.split("_")[0]
    
    # output table names, with comparison geodatabase name prepended
#    missingFDTblName=compName+"_MissingFDS"
#    missingFCTblName=compName+"_MissingFCs"
#    missingFLDTblName=compName+"_MissingFields"
#    nullTableName=compName+"_MissingData"
#    


    ## CONVERT TABLES TO PANDAS DATAFRAMES
    pdNullTbl= table_to_pandas_dataframe(nullTable, field_names=None)
    pdFLDTbl= table_to_pandas_dataframe(missFLDTable, field_names=None)
    pdFCTbl= table_to_pandas_dataframe(missFCTable, field_names=None)
    pdFDSTbl= table_to_pandas_dataframe(missFDSTable, field_names=None)
    
    
    # replace cells with '' as NaN
    pdNullTbl = pdNullTbl.replace('', numpy.nan)
    pdFLDTbl = pdFLDTbl.replace('', numpy.NaN)
    pdFCTbl = pdFCTbl.replace('', numpy.NaN)
    pdFDSTbl = pdFDSTbl.replace('', numpy.NaN)

    # FOR EACH FEATURE CLASS, GET COUNT OF CELLS THAT ARE INDETERMINANT
    arcpy.AddMessage ("Getting count of indeterminant cells per feature class")
    indtCntByFC = pdNullTbl.groupby(['FDS','FC','INSTALLATION'])['TOTAL_INDT_COUNT'].agg('sum').fillna(0).reset_index()
    indtCntByFC=pandas.DataFrame(indtCntByFC)
    # FOR EACH FEATURE CLASS, GET COUNT OF CELLS THAT ARE INDETERMINANT
    arcpy.AddMessage ("Getting count of indeterminant cells per feature class")
    detCntByFC = pdNullTbl.groupby(['FDS','FC','INSTALLATION'])['TOTAL_DET_COUNT'].agg('sum').fillna(0).reset_index()
    detCntByFC=pandas.DataFrame(detCntByFC)

    # FOR EACH FEATURE CLASS, GET COUNT OF CELLS THAT ARE NULL
    ## THEN EXPORT THEM TO THE GEODATABASE
    arcpy.AddMessage ("Getting count of 'null' cells per feature class")
    nullCntByFC = pdNullTbl.groupby(['FDS','FC','INSTALLATION'])['NULL_FC_COUNT'].agg('sum').fillna(0).reset_index()
    nullCntByFC=pandas.DataFrame(nullCntByFC)
    # FOR EACH FEATURE CLASS, GET COUNT OF CELLS THAT ARE TBD
    ## THEN EXPORT THEM TO THE GEODATABASE
    arcpy.AddMessage ("Getting count of 'tbd' cells per feature class")
    tbdCntByFC = pdNullTbl.groupby(['FDS','FC','INSTALLATION'])['TBD_FC_COUNT'].agg('sum').fillna(0).reset_index()
    tbdCntByFC=pandas.DataFrame(tbdCntByFC)

    # FOR EACH FEATURE CLASS, GET COUNT OF CELLS THAT ARE OTHER
    ## THEN EXPORT THEM TO THE GEODATABASE
    arcpy.AddMessage ("Getting count of 'other' cells per feature class")
    otherCntByFC = pdNullTbl.groupby(['FDS','FC','INSTALLATION'])['OTHER_FC_COUNT'].agg('sum').fillna(0).reset_index()
    otherCntByFC=pandas.DataFrame(otherCntByFC)

    
    # FOR EACH FEATURE CLASS, GET COUNT OF CELLS THAT ARE INDETERMINANT
    totalCntByFC = pdNullTbl.groupby(['FDS','FC','INSTALLATION'])['POP_VALS_COUNT'].agg('sum').fillna(0).reset_index()
    totalCntByFC=pandas.DataFrame(totalCntByFC)

    j1 = otherCntByFC.join ( tbdCntByFC.set_index( [ 'FDS','FC','INSTALLATION'], verify_integrity=True ),
               on=[ 'FDS','FC','INSTALLATION'], how='left' )
    
    j2 = j1.join ( nullCntByFC.set_index( [ 'FDS','FC','INSTALLATION'], verify_integrity=True ),
               on=[ 'FDS','FC','INSTALLATION'], how='left' )
    
    j3 = j2.join ( indtCntByFC.set_index( [ 'FDS','FC','INSTALLATION'], verify_integrity=True ),
               on=[ 'FDS','FC','INSTALLATION'], how='left' )
    
    j4 = j3.join ( detCntByFC.set_index( [ 'FDS','FC','INSTALLATION'], verify_integrity=True ),
               on=[ 'FDS','FC','INSTALLATION'], how='left' )
    
    j5 = j4.join ( totalCntByFC.set_index( [ 'FDS','FC','INSTALLATION'], verify_integrity=True ),
               on=[ 'FDS','FC','INSTALLATION'], how='left' )
    
    summary = pandas.DataFrame()
    summary["INSTALLATION"]=j5.INSTALLATION
    summary["FDS"]=j5.FDS  
    summary["FC"]=j5.FC  
    summary["OTHER_PCT"] = (j5.OTHER_FC_COUNT/(j5.POP_VALS_COUNT))*100
    summary["TBD_PCT"] = (j5.TBD_FC_COUNT/(j5.POP_VALS_COUNT))*100
    summary["NULL_PCT"] = (j5.NULL_FC_COUNT/(j5.POP_VALS_COUNT))*100
    summary["OTHER_CNT"] = j5.OTHER_FC_COUNT
    summary["TBD_CNT"] = j5.TBD_FC_COUNT
    summary["NULL_CNT"] = j5.NULL_FC_COUNT
    summary["DETERMINED_PCT"] = (j5.TOTAL_DET_COUNT/(j5.POP_VALS_COUNT))*100
    summary["UNDETERMINED_PCT"] = (j5.TOTAL_INDT_COUNT/(j5.POP_VALS_COUNT))*100
    summary["DETERMINED_CNT"] = j5.TOTAL_DET_COUNT
    summary["UNDETERMINED_CNT"] = j5.TOTAL_INDT_COUNT
    #pandas_to_table(summary,compName+"_Summary_Cell_Pct_by_FC")

    #summary.to_csv(os.path.join(outputFolder,compName+"_Summary_Cell_Pct_by_FC.csv"))
    
    writer = pandas.ExcelWriter(outputFile+".xlsx")
    summary.to_excel(writer,sheet_name=compName+"_Summary_by_FC")

    ''' do the above but grouping by field also '''
        # FOR EACH FIELD, GET COUNT OF CELLS THAT ARE NULL
    ## THEN EXPORT THEM TO THE GEODATABASE
    arcpy.AddMessage ("Getting count of 'null' cells per feature class field")
    nullCntByFLD = pdNullTbl.groupby(['FDS','FC','INSTALLATION','FIELD'])['NULL_FC_COUNT'].agg('sum').fillna(0).reset_index()

    nullCntByFLD=pandas.DataFrame(nullCntByFLD)
    #nullCntByFLD=nullCntByFLD.query('NULL_FC_COUNT > 0')

    # FOR EACH FEATURE CLASS, GET COUNT OF CELLS THAT ARE TBD
    ## THEN EXPORT THEM TO THE GEODATABASE
    arcpy.AddMessage ("Getting count of 'tbd' cells per feature class field")
    tbdCntByFLD = pdNullTbl.groupby(['FDS','FC','INSTALLATION','FIELD'])['TBD_FC_COUNT'].agg('sum').fillna(0).reset_index()
    tbdCntByFLD=pandas.DataFrame(tbdCntByFLD)
    #tbdCntByFLD=tbdCntByFLD.query('TBD_FC_COUNT > 0')

	
    # FOR EACH FEATURE CLASS, GET COUNT OF CELLS THAT ARE OTHER
    ## THEN EXPORT THEM TO THE GEODATABASE
    arcpy.AddMessage ("Getting count of 'other' cells per feature class field")

    otherCntByFLD = pdNullTbl.groupby(['FDS','FC','INSTALLATION','FIELD'])['OTHER_FC_COUNT'].agg('sum').fillna(0).reset_index()
    otherCntByFLD=pandas.DataFrame(otherCntByFLD)
    #otherCntByFLD=otherCntByFLD.query('OTHER_FC_COUNT > 0')

        # FOR EACH FEATURE CLASS, GET COUNT OF CELLS THAT ARE INDETERMINANT
    arcpy.AddMessage ("Getting count of indeterminant cells per feature class")
    indtCntByFLD = pdNullTbl.groupby(['FDS','FC','INSTALLATION','FIELD'])['TOTAL_INDT_COUNT'].agg('sum').fillna(0).reset_index()
    indtCntByFLD=pandas.DataFrame(indtCntByFLD)
    
    # FOR EACH FEATURE CLASS, GET COUNT OF CELLS THAT ARE INDETERMINANT
    arcpy.AddMessage ("Getting count of indeterminant cells per feature class")
    detCntByFLD = pdNullTbl.groupby(['FDS','FC','INSTALLATION','FIELD'])['TOTAL_DET_COUNT'].agg('sum').fillna(0).reset_index()
    detCntByFLD=pandas.DataFrame(detCntByFLD)
    
    # FOR EACH FEATURE CLASS, GET COUNT OF CELLS THAT ARE INDETERMINANT
    totalCntByFLD = pdNullTbl.groupby(['FDS','FC','INSTALLATION','FIELD'])['POP_VALS_COUNT'].agg('sum').fillna(0).reset_index()
    totalCntByFLD=pandas.DataFrame(totalCntByFLD)
    
    t1 = nullCntByFLD.join ( tbdCntByFLD.set_index( [ 'FDS','FC','INSTALLATION','FIELD'], verify_integrity=True),on=[ 'FDS','FC','INSTALLATION','FIELD'], how='left' )
    t2 = t1.join ( otherCntByFLD.set_index( [ 'FDS','FC','INSTALLATION','FIELD'], verify_integrity=True ),on=[ 'FDS','FC','INSTALLATION','FIELD'], how='left' )
    t3 = t2.join ( detCntByFLD.set_index( [ 'FDS','FC','INSTALLATION','FIELD'], verify_integrity=True ),on=[ 'FDS','FC','INSTALLATION','FIELD'], how='left' )
    t4 = t3.join ( indtCntByFLD.set_index( [ 'FDS','FC','INSTALLATION','FIELD'], verify_integrity=True ),on=[ 'FDS','FC','INSTALLATION','FIELD'], how='left' )
    t5 = t4.join ( totalCntByFLD.set_index( [ 'FDS','FC','INSTALLATION','FIELD'], verify_integrity=True ),on=[ 'FDS','FC','INSTALLATION','FIELD'], how='left' )
    

    countsByField = pandas.DataFrame()
    countsByField["INSTALLATION"]=t5.INSTALLATION
    countsByField["FDS"]=t5.FDS  
    countsByField["FC"]=t5.FC  
    countsByField["FIELD"]=t5.FIELD  
    countsByField["OTHER_PCT"] = (t5.OTHER_FC_COUNT/(t5.POP_VALS_COUNT))*100
    countsByField["TBD_PCT"] = (t5.TBD_FC_COUNT/(t5.POP_VALS_COUNT))*100
    countsByField["NULL_PCT"] = (t5.NULL_FC_COUNT/(t5.POP_VALS_COUNT))*100
    countsByField["OTHER_CNT"] = t5.OTHER_FC_COUNT
    countsByField["TBD_CNT"] = t5.TBD_FC_COUNT
    countsByField["NULL_CNT"] = t5.NULL_FC_COUNT
    countsByField["DETERMINED_PCT"] = (t5.TOTAL_DET_COUNT/(t5.POP_VALS_COUNT))*100
    countsByField["UNDETERMINED_PCT"] = (t5.TOTAL_INDT_COUNT/(t5.POP_VALS_COUNT))*100
    countsByField["DETERMINED_CNT"] = t5.TOTAL_DET_COUNT
    countsByField["UNDETERMINED_CNT"] = t5.TOTAL_INDT_COUNT
	
    countsByField=countsByField.query('UNDETERMINED_CNT > 0')
	
	
    #pandas_to_table(pddf=countsByField,tablename=compName+"_Indeterminate_Counts_by_Field")
    #countsByField.to_csv(os.path.join(outputFolder,compName+"_Indeterminate_Counts_by_Field.csv"))
    countsByField.to_excel(writer,sheet_name=compName+"_Summary_by_Field")

	
    ### FOR EACH FEATURE CLASS INCLUDED, HOW MANY ARE EMPTY? 
    emptyFCbyFDS=pdNullTbl.query("EMPTY_FC == 'T'").groupby(['FDS','FC','INSTALLATION']).size().reset_index()
    emptyFCbyFDS=pandas.DataFrame(emptyFCbyFDS)
    emptyFCbyFDS.columns = ['FDS','FC','INSTALLATION','TOTAL_EMPTY_FIELDS']


    ### FOR EACH FEATURE CLASS INCLUDED, HOW MANY ARE EMPTY?
    arcpy.AddMessage ("Getting total count empty feature classes")
    emptyFCcnt = len(pdNullTbl.query("EMPTY_FC == 'T'").groupby(['FDS','FC','EMPTY_FC']).size().reset_index() )
    arcpy.AddMessage ("Getting total count non-empty feature classes")
    nonemptyFCcnt = len(pdNullTbl.query("EMPTY_FC == 'F'").groupby(['FDS','FC','EMPTY_FC']).size().reset_index() )
    
    arcpy.AddMessage ("Getting count of empty feature classes by feature dataset")
    if emptyFCbyFDS.empty:
        emptyFLDsumFDS = "NA - no empty FCs"
    else:
        emptyFLDsumFDS = emptyFCbyFDS.groupby(['INSTALLATION']).agg('sum').fillna(0).reset_index()
        emptyFLDsumFDS = emptyFLDsumFDS.iloc[0]['TOTAL_EMPTY_FIELDS']
    arcpy.AddMessage ("Getting count of empty fields from non-empty feature classes ")
    emptyFLDsum = pdNullTbl.query("POP_VALS_COUNT ==0 & EMPTY_FC == 'F'").groupby(['FDS','FC','INSTALLATION']).ngroups

    #pandas_to_table(pddf=emptyFCbyFDS,tablename=compName+"_EmptyFeatureClasses")
    emptyFCbyFDS.to_excel(writer,sheet_name=compName+"__EmptyFeatureClasses")

    ### GET NUMBER OF MISSING FEATURE DATASETS
    arcpy.AddMessage ("Getting count of missing feature datasets ")

    missingFDScnt = pdFDSTbl.groupby(['FDS_MISSING','INSTALLATION']).ngroups
    
    ### GET NUMBER OF MISSING FEATURE CLASSES per FEATURE DATASET
    arcpy.AddMessage ("Getting count of missing feature classes per feature dataset ")
    missingFCcnt = pdFCTbl.groupby(['FDS','FC_MISSING','INSTALLATION']).ngroups
    arcpy.AddMessage ("Binding overview table")

    # BIND DATA INTO A PANDAS DATAFRAME
    d = {
         'Installation':[installationName],
         'MissingFDScount': [missingFDScnt],
         'MissingFCcount': [missingFCcnt],
         'InclFeatsEmpty':[emptyFCcnt],
         'InclFeatsNonEmpty':[nonemptyFCcnt],
         'TotalEmptyFields':[emptyFLDsum],
         'TotalEmptyFieldsfromEmptyFC':[emptyFLDsumFDS]
         }
    
    d= pandas.DataFrame(d)
    #pandas_to_table(pddf=d,tablename=compName+"_Overview")
    #d.to_csv(os.path.join(outputFolder,compName+"_Indeterminate_Overview.csv"))
    d.to_excel(writer,sheet_name=compName+"_Indeterminate_Overview")

    writer.save()
    time_elapsed = datetime.now() - start_time  
    time_elapsed
	
	
installGDB = get_geodatabase_path(nullTable)
summariseMissingData(installGDB)
        
## creates all reports for all gdbs, work on sending python object to R to markdown report.
# import subprocess 
# command = 'C:/Program Files/R/R-3.4.1/bin/Rscript'
# arg = '--vanilla'
# path2script = os.path.join(mainDir,'Installation_Reports.R')


# # =============================================================================
# subprocess.call([command, arg, path2script], shell=True)
# # =============================================================================




#arcpy.GetInstallInfo ()

# =============================================================================
# {'BuildNumber': u'8321',
#  'InstallDate': u'3/19/2018',
#  'InstallDir': u'c:\\program files (x86)\\arcgis\\desktop10.6\\',
#  'InstallTime': u'12:39:29',
#  'InstallType': u'N/A',
#  'Installer': u'stevenconnorg',
#  'ProductName': u'Desktop',
#  'SPBuild': u'N/A',
#  'SPNumber': u'N/A',
#  'SourceDir': u'C:\\Users\\stevenconnorg\\Documents\\ArcGIS 10.6\\Desktop\\SetupFiles\\',
#  'Version': u'10.6'}
# =============================================================================

#for name, module in sorted(sys.modules.items()): 
#  if hasattr(module, '__version__'): 
#    print name, module.__version__ 

# =============================================================================
# Cython 0.27.3
# Cython.Build.Dependencies 0.27.3
# Cython.Shadow 0.27.3
# IPython 5.4.1
# IPython.core.release 5.4.1
# IPython.utils._signatures 0.3
# PIL 5.0.0
# PIL.version 5.0.0
# _ast 82160
# _csv 1.0
# _ctypes 1.1.0
# _elementtree 1.0.6
# _struct 0.2
# argparse 1.1
# ast 82160
# backports.shutil_get_terminal_size 1.0.0
# bottleneck 1.2.1
# bottleneck.version 1.2.1
# bs4 4.6.0
# cPickle 1.71
# cffi 1.11.4
# cgi 2.6
# chardet 3.0.4
# chardet.version 3.0.4
# cloudpickle 0.5.2
# colorama 0.3.9
# csv 1.0
# ctypes 1.1.0
# cycler 0.10.0
# cython 0.27.3
# dateutil 2.6.1
# decimal 1.70
# decorator 4.2.1
# distutils 2.7.14
# email 4.0.3
# future 0.15.2
# html5lib 1.0.1
# ipykernel 4.8.0
# ipykernel._version 4.8.0
# ipython_genutils 0.2.0
# ipython_genutils._version 0.2.0
# ipywidgets 7.1.1
# ipywidgets._version 7.1.1
# json 2.0.9
# jupyter_client 5.2.2
# jupyter_client._version 5.2.2
# jupyter_core 4.4.0
# jupyter_core.version 4.4.0
# logging 0.5.1.2
# lxml.etree 4.1.1
# matplotlib 2.1.2
# matplotlib.backends.backend_agg 2.1.2
# multiprocessing 0.70a1
# numexpr 2.6.4
# numpy 1.14.0
# numpy.core 1.14.0
# numpy.core.multiarray 3.1
# numpy.core.umath 0.4.0
# numpy.lib 1.14.0
# numpy.linalg._umath_linalg 0.1.5
# pandas 0.22.0
# pandas._libs.json 1.33
# pickle $Revision: 72223 $
# pickleshare 0.7.4
# pkg_resources._vendor.appdirs 1.4.0
# pkg_resources._vendor.packaging 16.8
# pkg_resources._vendor.packaging.__about__ 16.8
# pkg_resources._vendor.pyparsing 2.1.10
# pkg_resources._vendor.six 1.10.0
# pkg_resources.extern.appdirs 1.4.0
# pkg_resources.extern.packaging 16.8
# pkg_resources.extern.pyparsing 2.1.10
# pkg_resources.extern.six 1.10.0
# platform 1.0.7
# prompt_toolkit 1.0.15
# pydoc $Revision: 88564 $
# pyexpat 2.7.14
# pygments 2.2.0
# pyparsing 2.2.0
# pytz 2017.3
# re 2.2.1
# scandir 1.6
# six 1.11.0
# spyder 3.2.6
# spyder.utils.external.binaryornot 0.4.0
# tarfile $Revision: 85213 $
# traitlets 4.3.2
# traitlets._version 4.3.2
# urllib 1.17
# urllib2 2.7
# zlib 1.0
# zmq 16.0.3
# zmq.sugar 16.0.3
# zmq.sugar.version 16.0.3
# =============================================================================


import platform
platform.machine()
# =============================================================================
# 'AMD64'
# =============================================================================
platform.version()
# =============================================================================
# '10.0.16299'
# =============================================================================
platform.platform()
# =============================================================================
# 'Windows-10-10.0.16299'
# =============================================================================
platform.uname()
# =============================================================================
# ('Windows',
#  'LAPTOP-TNLQN6EV',
#  '10',
#  '10.0.16299',
#  'AMD64',
#  'Intel64 Family 6 Model 94 Stepping 3, GenuineIntel')
# =============================================================================

platform.processor()
# =============================================================================
# 'Intel64 Family 6 Model 94 Stepping 3, GenuineIntel'
# =============================================================================

