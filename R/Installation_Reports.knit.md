---
output:
  bookdown::pdf_document2:
    latex_engine: xelatex
    toc: true
    toc_depth: 3
    number_sections: true
    fig_caption: true
    keep_md: true
    documentclass: report
    self_contained: true
  bookdown::gitbook:
    split_by: none
    self_contained: true
    search: yes
    edit : no
    config:
      toc:
        before: |
          <li><a href="./">Missing and Indeterminant Data Reports</a></li>
        after: |
          <li><a href="https://github.com/rstudio/bookdown" target="blank">Published with bookdown</a></li>
      download: ["pdf"]
author:  
- Steven C. Gonzalez
- Air Force Civil Engineering Center (AFCEC)
- Geospatial Integration Office (GIO)
params: 
    set_title: "My Title!"
subtitle: <h1> Missing and Indeterminant Data Report</h1>
date: "17 May, 2018"
link-citations: true
bibliography: [packages.bib]
biblio-style: apalike
linestretch: 1.25
header-includes:
  - \usepackage {hyperref}
  - \hypersetup{linktocpage}
  - \hypersetup {colorlinks = true,linkcolor = blue, urlcolor = blue}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \usepackage{array}
  - \usepackage{multirow}
  - \usepackage[table]{xcolor}
  - \usepackage{wrapfig}
  - \usepackage{float}
  - \usepackage{colortbl}
  - \usepackage{pdflscape}
  - \usepackage{tabu}
  - \usepackage{threeparttable}
  - \usepackage[normalem]{ulem}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyfoot[L]{Air Force Civil Engineering Center}
  - \fancyfoot[R]{Geospatial Integration Office}
  - \fancyhead[L]{}
  - \renewcommand{\footrulewidth}{0.5pt}\usepackage{fancyhdr}
---

---
title: Altus AFB
---







\pagebreak


# Report Overview
The purpose of this report is to give  an overview of data missing from Altus AFB's geodatabase when compared with the Air Force (AF) [Spatial Data Standards for Facilities, Infrastructure, and Environment (SDSFIE)](https://www.sdsfieonline.org/) 3.101 geodatabase schema. The Air Force Data Model (GeoBase 3.1.0.1) developed under the [AF GeoBase mission](https://www.sdsfieonline.org/Components/USAF) is based upon the SDSFIE-V 3.1 Gold model, which complies with  the Department of Defense Instruction (DoDI) 8130.01, *Installation Geospatial Information and Service* (IGI&S), but  allows some greater flexibility within the program to aid the AF mission. As part of the IGI&S program, this report complies with the Fiscal Year 2017 Common Installation Picture (CIP) data call required by DoDI 8130.01.

**The template geodatabase used for this report is the CIP AF SDSFIE 3.101 geodatabase.**

Upon receiving Altus AFB's geodatabase, standard Feature Classes were migrated to standard Feature Datasets to match the CIP AF SDSFIE 3.101 geodatabase, where required.  Then, this report identifies discrepancies between Altus AFB's geodatabase in comparison with the CIP geodatabase schema, following the following format:  

1. Section \@ref(summary) lists a summary of findings regarding indeterminant and missing data in Altus AFB's geodatabase in comparison with the CIP geodatabase schema.
2. Section \@ref(missFDS) lists which AF SDSFIE standard Feature Datasets are missing from Altus AFB's geodatabase in comparison with the CIP geodatabase schema.
3. Sections \@ref(missFCFDS) - \@ref(missFC) lists which AF SDSFIE standard Feature Classes are missing from those Feature Datasets for each of the AF SDSFIE standard Feature Datasets in the CIP geodatabase schema that are included in Altus AFB's geodatabase.
4. Section \@ref(missFLDincFC) continues to identify the counts of Missing Fields per standard Feature Classes included. Of the included Feature Classes, empty Feature Classes are listed in the 'Empty Feature Classes' section (Section \@ref(emptFC)).
5. Section \@ref(emptFLDneFC) identifies the counts of empty fields from non-empty, standard Feature Classes included in Altus AFB's geodatabase.
6. Section \@ref(detindtVal) then analyzes each AF SDSFIE standard Feature Class within Altus AFB's geodatabase for indeterminant data at the Attribute level for each of the AF SDSFIE standard Feature Dataset/Feature Class combinations from CIP schema that are included in Altus AFB's geodatabase. 
7. Section \@ref(pctindtFC) gives an overview of the percent of Attribute Table cells identified as 'Null', 'TBD', and 'Other' per Feature Class.
8. Sections \@ref(nullCnt), \@ref(tbdCnt), and \@ref(otherCnt) give the counts of 'Null', 'TBD', and 'Other' data (called: 'indeterminant' data), respectively, by each SDSFIE Feature Dataset/Feature Class in Altus AFB's Geodatabase
9. Finally, this report identifies noted discrepancies between the target CIP schema and Altus AFB's geodatabase (Section \@ref(diff)) for (1) Fields with Incorrectly Populated Domains (Section \@ref(diffIncDom)) and, (2) Fields Included in Altus AFB's Geodatabase Not in the CIP schema (Section \@ref(diffFLD)).  

The data utilized to produce this report may be found within the Altus AFB_Indeterminant_Data-CIP Excel Workbook accompanying this  report. Specific references to the tables found in this Excel Workbook are found throughout the report where further details may be warranted.

\pagebreak

# Summary of Findings {#summary}
1. **0** : Total Number of Missing Feature Datasets   
2. **1** : Total Number of Missing Feature Classes within included Feature Datasets  
3. **10 **: Total Number of Empty Feature Classes within included Feature Datasets  
4. **387** : Total Number of Empty Fields from Empty Feature Classes  
5. **0** : Total Number of Empty Fields from non-Empty Feature Classes   
6. 44,330/252,936 **(17.53%)**: Total number of cells are populated with determinant data (i.e.: **not** 'Null', 'TBD', or 'Other')

7. 208,606/252,936 **(82.47%)**: Total number of cells are missing data (i.e.: 'Null', 'TBD', or 'Other')

    + 180,662/252,936 **(71.43%)**: Total number of cells are 'Null' data  
    
    + 27,444/252,936 **(10.85%)**: Total number of cells are 'TBD' data  
    
    + 500/252,936 **(0.2%)**: Total number of cells are 'Other' data    
8. **0** : Total Number of Fields with Incorrectly Populated Domains (within included standard Feature Classes)  
9. **0** : Total Number of Fields Included in Altus AFB's Geodatabase **Not** Included in the CIP Schema (within included standard Feature Classes)  


\pagebreak



# Missing Feature Datasets {#missFDS}
This section provides an overview of the AF SDSFIE standard Feature Datasets in the CIP schema that are not also included in Altus AFB's geodatabase. If Altus AFB's geodatabase was delivered to AFCEC without Feature Datasets, 'loose' standard Feature Classes were first migrated to the respective Feature Dataset according to AF SDSFIE 3.101 standards.

Overall, Altus AFB has 0 missing AF SDSFIE standard Feature Datasets.  

Please see Table \@ref(tab:cmissFDS) below for a complete listing of the AF SDSFIE standard Feature Datasets  missing from Altus AFB's geodatabase, where applicable.  This information is also found in Altus AFB's geodatabase under the 'CIP_MissingFDS' table.


\begin{table}[!h]

\caption{(\#tab:cmissFDS)Missing Feature Datasets}
\centering
\begin{tabular}{l}
\hline
FDS\\


\hline
\multicolumn{1}{l}{\textbf{Note: } }\\
\multicolumn{1}{l}{0 Total Missing Feature Datasets}\\
\end{tabular}
\end{table}



# Missing and Empty Feature Classes {#miss-empFC}
## Missing Feature Classes by Feature Dataset {#missFCFDS}
Of the required Feature Datasets within the CIP schema included in Altus AFB's geodatabase, 1 of the standard Feature Classes are not present. Table \@ref(tab:cmissFCFDS) below gives the count of missing Feature Classes per Feature Dataset, sorted in ascending order, where applicable.  


\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}cc}
\caption{(\#tab:cmissFCFDS)Missing Feature Classes by Feature Dataset}\\
\hiderowcolors
\toprule
FDS & Missing\_FC\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cmissFCFDS)Missing Feature Classes by Feature Dataset \textit{(continued)}}\\
\toprule
FDS & Missing\_FC\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{1 Total Missing Feature Classes}\\
\endlastfoot
\showrowcolors
Transportation & 1\\*
\end{longtable}
\rowcolors{2}{white}{white}



## Missing Feature Classes {#missFC}
Of the required Feature Datasets within the CIP schema included in Altus AFB's geodatabase, 1 of the required Feature Classes are not present. Table \@ref(tab:cmissFC) below gives a listing of all the Feature Classes missing, along with the associated Feature Dataset, where applicable. This information is also found in the'CIP_MissingFCs' table/sheet in the Altus AFB_Indeterminant_Data-CIP Excel Workbook provided with this report.


\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}cc}
\caption{(\#tab:cmissFC)Missing Feature Classes}\\
\hiderowcolors
\toprule
FDS & FC\_MISSING\\
\midrule
\endfirsthead
\caption[]{(\#tab:cmissFC)Missing Feature Classes \textit{(continued)}}\\
\toprule
FDS & FC\_MISSING\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{1 Total Missing Feature Classes}\\
\endlastfoot
\showrowcolors
Transportation & RoadSeg\_L\\*
\end{longtable}
\rowcolors{2}{white}{white}


## Missing Field Counts from Included Feature Classes {#missFLDincFC}
Of the standard Feature Classes included, 2 standard fields for said Feature Classes in CIP schema are missing in Altus AFB's geodatabase. Table \@ref(tab:cmissFLDincFC) gives a count of the *fields* missing from each standard Feature Class in Altus AFB's geodatabase. For the purposes of this report, the following fields are not included in this search: 'SHAPE,' 'DATEEDITED,' 'EDITOR,' 'CREATOR,' 'CREATEDATE'.

For a more detailed breakdown of the individual missing fields from standard Feature Classes, see the 'CIP_MissingFields' table/sheet in the Altus AFB_Indeterminant_Data-CIP Excel Workbook.
\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccc}
\caption{(\#tab:cmissFLDincFC)Missing Field Counts by Feature Class}\\
\hiderowcolors
\toprule
FDS & FC & Missing\_Field\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cmissFLDincFC)Missing Field Counts by Feature Class \textit{(continued)}}\\
\toprule
FDS & FC & Missing\_Field\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{2 Total Missing Fields}\\
\endlastfoot
\showrowcolors
RealProperty & Building\_A & 1\\
RealProperty & Tower\_P & 1\\*
\end{longtable}
\rowcolors{2}{white}{white}




## Empty Feature Classes {#emptFC}


Of the Feature Classes within the CIP schema included in Altus AFB's geodatabase, 10 standard Feature Classes are empty. Table \@ref(tab:cemptFC2) gives a listing of all the empty Feature Classes in Altus AFB's geodatabase. In total, 387 empty Fields are present due to empty Feature Classes. This information is also found in the Altus AFB_Indeterminant_Data-CIP Excel Workbook in the 'CIP_EmptyFeatureClasses' table/sheet. 

\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccc}
\caption{(\#tab:cemptFC2)Empty Feature Classes}\\
\hiderowcolors
\toprule
FDS & FC & Empty\_Field\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cemptFC2)Empty Feature Classes \textit{(continued)}}\\
\toprule
FDS & FC & Empty\_Field\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{387 Total Empty Fields}\\
\endlastfoot
\showrowcolors
Auditory & NoiseZone\_A & 44\\
Cadastre & Site\_P & 35\\
MilitaryRangeTraining & ImpactArea\_A & 35\\
MilitaryRangeTraining & MilQuantityDistCombinedArc\_A & 36\\
Recreation & RecArea\_A & 33\\
Transportation & Bridge\_L & 52\\
Transportation & RailTrack\_L & 40\\
Transportation & RoadPath\_L & 36\\
WaterWays & DocksAndWharfs\_A & 37\\
environmentalCulturalResources & HistoricDistrict\_A & 39\\*
\end{longtable}
\rowcolors{2}{white}{white}





## Empty Fields from Non-Empty Feature Classes {#emptFLDneFC}
Of the Feature Classes within the CIP schema included in Altus AFB's geodatabase, 0 empty fields are present due to non-empty Feature Classes. Table \@ref(tab:cemptFLDneFC) below gives the count of empty fields by non-empty feature classes.  


For a more detailed breakdown of the individual empty fields from non-empty feature classes, see the 'CIP_MissingData' table/sheet in the Altus AFB_Indeterminant_Data-CIP Excel Workbook accompanying this report, where rows are 'F' for the 'EMPTY_FC' column *and* rows are '0' for the 'POP_VALS_COUNT' column.  


\begin{table}[!h]

\caption{(\#tab:cemptFLDneFC)Empty Fields from Non-Empty Feature Classes}
\centering
\begin{tabular}{l|l|r}
\hline
FDS & FC & Empty\_Fields\_Counts\\


\hline
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{0 Total Empty Fields}\\
\end{tabular}
\end{table}



# Determinant and Indeterminant Values {#detindtVal}

Altus AFB's geodatabase was analyzed for potential gaps in data at the Attribute level. Gaps in data were determined for each standard Feature Class' Attribute Table where cell values are 'Null', 'TBD' or 'Other.'  


Within the standard Feature Dataset/Feature Class combinations included in Altus AFB's geodatabase, the percentage of data populated with determinant values (i.e.: data **not** classified as 'Null', 'TBD', or 'Other') are recorded in Table \@ref(tab:cdetindtVal2) below by Feature Class. The figure below gives a cursory look at the average percentage of data determined (i.e.: not 'Null', 'TBD', or 'Other') by SDSFIE Feature Dataset within Altus AFB's geodatabase. 

Within Altus AFB's geodatabase, the 'PavementSection_A' Feature class had the minimum data determined percentage of 8.3%, while the 'EnvRemediationSite_A' Feature class had the maximum data determined percentage of 66.2%. On average, not including empty, standard Feature Classes, 43.5% of values are populated with determinant data for Altus AFB's geodatabase *when averaged across standard Feature Classes included*. This information is also found in the Altus AFB_Indeterminant_Data-CIP Excel Workbook delivered with this report under the 'CIP_Determinant_Values_by_FC' table/sheet.  


![](C:/Users/stevenconnorg/Documents/knight-federal-solutions/Missing_Data_Reports/out/Reports/CIP/Altus_AFB_Missing_Data_Report_CIP_files/figure-latex/unnamed-chunk-1-1.pdf)<!-- --> 


\rowcolors{2}{white}{gray!6}

\begin{longtable}{l>{\bfseries}ccc}
\caption{(\#tab:cdetindtVal2)Determinant Value Percentage by Feature Class}\\
\hiderowcolors
\toprule
  & FDS & FC & Values\_Determined(\%)\\
\midrule
\endfirsthead
\caption[]{(\#tab:cdetindtVal2)Determinant Value Percentage by Feature Class \textit{(continued)}}\\
\toprule
  & FDS & FC & Values\_Determined(\%)\\
\midrule
\endhead
\
\endfoot
\bottomrule
\endlastfoot
\showrowcolors
2 & Cadastre & Site\_A & 47.2\\
3 & Cadastre & Outgrant\_A & 61.3\\
4 & Cadastre & LandParcel\_A & 63.2\\
5 & Cadastre & Installation\_A & 63.4\\
8 & environmentalNaturalResources & Wetland\_A & 59.4\\
9 & environmentalRestoration & EnvRemediationSite\_A & 66.2\\
10 & MilitaryRangeTraining & MilRange\_A & 47.2\\
11 & MilitaryRangeTraining & MilTrainingLoc\_A & 50.0\\
14 & Pavements & PavementSection\_A & 8.3\\
15 & Pavements & PavementBranch\_A & 22.4\\
16 & Planning & LandUse\_A & 45.0\\
17 & Planning & AirAccidentZone\_A & 51.5\\
18 & RealProperty & Tower\_P & 35.7\\
19 & RealProperty & Building\_A & 45.4\\
20 & Recreation & GolfCourse\_A & 52.9\\
22 & Security & Fence\_L & 26.2\\
23 & Security & AccessControl\_L & 31.5\\
24 & Security & AccessControl\_P & 37.5\\
25 & Transportation & RailSegment\_L & 26.5\\
26 & Transportation & Bridge\_A & 33.6\\
27 & Transportation & RoadCenterline\_L & 37.5\\
28 & Transportation & VehicleParking\_A & 45.6\\*
\end{longtable}
\rowcolors{2}{white}{white}



## Percent of Values 'Null', 'TBD' or 'Other' by Feature Class {#pctindtFC}


Within the standard Feature Dataset/Feature Class combinations included, the percentage of data populated with indeterminant values are recorded in Table \@ref(tab:cpctindtFC2) below.  

 

For Altus AFB's geodatabase, 0.6% of cells are populated with 'Other' values, 3% of cells are populated with values 'To be determined,' and 52.9 of cells are populated with 'Null' cells, *when averaged across standard Feature Classes* included in Altus AFB's geodatabase.  This information is also found in the Altus AFB_Indeterminant_Data-CIP Excel Workbook under the 'CIP_Summary_Cell_Pct_by_FC' table/sheet. 




\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccccc}
\caption{(\#tab:cpctindtFC2)Percent Other, TBD, and Null Cells by Feature Class}\\
\hiderowcolors
\toprule
FDS & FC & \%\_Other & \%\_TBD & \%\_Null\\
\midrule
\endfirsthead
\caption[]{(\#tab:cpctindtFC2)Percent Other, TBD, and Null Cells by Feature Class \textit{(continued)}}\\
\toprule
FDS & FC & \%\_Other & \%\_TBD & \%\_Null\\
\midrule
\endhead
\
\endfoot
\bottomrule
\endlastfoot
\showrowcolors
Cadastre & Installation\_A & 2.9 & 0.6 & 33.1\\
Cadastre & LandParcel\_A & 0.0 & 0.0 & 36.8\\
Cadastre & Outgrant\_A & 0.0 & 0.0 & 38.7\\
Cadastre & Site\_A & 0.0 & 0.0 & 52.8\\
environmentalNaturalResources & Wetland\_A & 0.0 & 21.0 & 19.6\\
environmentalRestoration & EnvRemediationSite\_A & 1.0 & 5.4 & 27.5\\
MilitaryRangeTraining & MilTrainingLoc\_A & 0.0 & 2.9 & 47.1\\
MilitaryRangeTraining & MilRange\_A & 2.8 & 2.8 & 47.2\\
Pavements & PavementBranch\_A & 0.0 & 8.2 & 69.4\\
Pavements & PavementSection\_A & 0.0 & 14.9 & 76.8\\
Planning & AirAccidentZone\_A & 1.3 & 0.0 & 47.2\\
Planning & LandUse\_A & 0.0 & 2.7 & 52.2\\
RealProperty & Building\_A & 0.0 & 0.0 & 54.6\\
RealProperty & Tower\_P & 0.0 & 7.1 & 57.1\\
Recreation & GolfCourse\_A & 0.0 & 0.0 & 47.1\\
Security & AccessControl\_P & 0.0 & 0.0 & 62.5\\
Security & AccessControl\_L & 0.0 & 0.0 & 68.5\\
Security & Fence\_L & 0.0 & 0.0 & 73.8\\
Transportation & VehicleParking\_A & 2.5 & 0.0 & 52.0\\
Transportation & RoadCenterline\_L & 2.1 & 0.0 & 60.4\\
Transportation & Bridge\_A & 0.4 & 0.0 & 66.0\\
Transportation & RailSegment\_L & 0.0 & 0.0 & 73.5\\*
\end{longtable}
\rowcolors{2}{white}{white}



## 'Null' Value Counts {#nullCnt}
Altus AFB's geodatabase was analyzed for data with attributes 'Null' data at the Feature Class Attribute level.  180,662/252,936 (71.43%) *null* cells exist within standard Feature Classes in Altus AFB's geodatabase. 
 
 For the purposes of this report, 'Null' data is classified as any cell within a Feature Class' Attribute Table  that contains any one of the following values:

1.  "NULL"
2.  "None"
3.  "none"
4.  "NONE"
6.  "-99999"
7.  "77777"
8.  "NA"
9.  "N/A"
10. "n/a"
11. "Null"

Please see Tables \@ref(tab:cnullCntFDS) & \@ref(tab:cnullCntFC) for a count of Null cells by Feature Dataset and Feature Class, respectively.

A more detailed breakdown of the individual values and counts of values for each *field* may be found in the Altus AFB's geodatabase in the 'CIP_MissingData' Table under the 'NULL_VALUE_COUNTS' column. Further, you may see the counts of 'Null' cells by standard Feature Class in the 'CIP_NullCellCountbyFC' Table, or by Field in the 'CIP_NullCellCountbyFLD' Table, in in the Altus AFB_Indeterminant_Data-CIP Excel Workbook provided with this report.


###  'Null' Count by Feature Dataset {#nullCntFDS}
\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}cc}
\caption{(\#tab:cnullCntFDS)Count of Null Cells by Feature Dataset}\\
\hiderowcolors
\toprule
FDS & Total\_Null\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cnullCntFDS)Count of Null Cells by Feature Dataset \textit{(continued)}}\\
\toprule
FDS & Total\_Null\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{180662 Total 'Null' Cells}\\
\endlastfoot
\showrowcolors
Cadastre & 1,892\\
environmentalNaturalResources & 27\\
environmentalRestoration & 308\\
MilitaryRangeTraining & 33\\
Pavements & 149,615\\
Planning & 1,861\\
RealProperty & 7,258\\
Recreation & 33\\
Security & 6,869\\
Transportation & 12,766\\*
\end{longtable}
\rowcolors{2}{white}{white}



###  'Null' Count by Feature Class {#nullCntFC}
\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccc}
\caption{(\#tab:cnullCntFC)Count of Null Cells by Feature Class}\\
\hiderowcolors
\toprule
FDS & FC & Total\_Null\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cnullCntFC)Count of Null Cells by Feature Class \textit{(continued)}}\\
\toprule
FDS & FC & Total\_Null\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{180662 Total 'Null' Cells}\\
\endlastfoot
\showrowcolors
Cadastre & Installation\_A & 57\\
Cadastre & LandParcel\_A & 1,231\\
Cadastre & Outgrant\_A & 376\\
Cadastre & Site\_A & 228\\
MilitaryRangeTraining & MilRange\_A & 17\\
MilitaryRangeTraining & MilTrainingLoc\_A & 16\\
Pavements & PavementBranch\_A & 23,535\\
Pavements & PavementSection\_A & 126,080\\
Planning & AirAccidentZone\_A & 374\\
Planning & LandUse\_A & 1,487\\
RealProperty & Building\_A & 7,234\\
RealProperty & Tower\_P & 24\\
Recreation & GolfCourse\_A & 33\\
Security & AccessControl\_L & 1,656\\
Security & AccessControl\_P & 372\\
Security & Fence\_L & 4,841\\
Transportation & Bridge\_A & 297\\
Transportation & RailSegment\_L & 144\\
Transportation & RoadCenterline\_L & 8,758\\
Transportation & VehicleParking\_A & 3,567\\
environmentalNaturalResources & Wetland\_A & 27\\
environmentalRestoration & EnvRemediationSite\_A & 308\\*
\end{longtable}
\rowcolors{2}{white}{white}


                           

## 'TBD' Value Counts {#tbdCnt}
Altus AFB's geodatabase was analyzed for data with attributes 'to be determined ' (TBD) at the Feature Class Attribute level. 27,444/252,936 (10.85%) *TBD* cells exist within standard Feature Classes in Altus AFB's geodatabase. 

For the purposes of this report, TBD data is classified as any Feature Class Attribute Table cell that contains one of the following values:

1. 'To be determined'
2. 'TBD'
3. 'Tbd'
4. 'tbd'
5. '99999'

Please see Tables \@ref(tab:ctbdCntFDS) & \@ref(tab:ctbdCntFC) for a count of 'TBD' cells by Feature Dataset and Feature Class, respectively.

A more detailed breakdown of the individual values and counts of values found for each *field* may be found in the Altus AFB_Indeterminant_Data-CIP Excel Workbook within the 'CIP_MissingData' Table under the 'TBD_VALUE_COUNTS' column. Further, you may see the counts of 'Null' cells by standard Feature Class in the 'CIP_TBDCellCountbyFC' Table, or by Field in the 'CIP_TBDCellCountbyFLD' Table, in the Altus AFB_Indeterminant_Data-CIP Excel Workbook accompanying this report.


###  'TBD' Count by Feature Dataset {#tbdCntFDS}
\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}cc}
\caption{(\#tab:ctbdCntFDS)Count of TBD Cells by Feature Dataset}\\
\hiderowcolors
\toprule
FDS & Total\_TBD\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:ctbdCntFDS)Count of TBD Cells by Feature Dataset \textit{(continued)}}\\
\toprule
FDS & Total\_TBD\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{27444 Total 'TBD' Cells}\\
\endlastfoot
\showrowcolors
Cadastre & 1\\
environmentalNaturalResources & 29\\
environmentalRestoration & 60\\
MilitaryRangeTraining & 2\\
Pavements & 27,265\\
Planning & 78\\
RealProperty & 9\\*
\end{longtable}
\rowcolors{2}{white}{white}


###  'TBD' Count by Feature Class {#tbdCntFC}
\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccc}
\caption{(\#tab:ctbdCntFC)Count of TBD Cells by Feature Class}\\
\hiderowcolors
\toprule
FDS & FC & Total\_TBD\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:ctbdCntFC)Count of TBD Cells by Feature Class \textit{(continued)}}\\
\toprule
FDS & FC & Total\_TBD\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{27444 Total 'TBD' Cells}\\
\endlastfoot
\showrowcolors
Cadastre & Installation\_A & 1\\
MilitaryRangeTraining & MilRange\_A & 1\\
MilitaryRangeTraining & MilTrainingLoc\_A & 1\\
Pavements & PavementBranch\_A & 2,798\\
Pavements & PavementSection\_A & 24,467\\
Planning & LandUse\_A & 78\\
RealProperty & Building\_A & 6\\
RealProperty & Tower\_P & 3\\
environmentalNaturalResources & Wetland\_A & 29\\
environmentalRestoration & EnvRemediationSite\_A & 60\\*
\end{longtable}
\rowcolors{2}{white}{white}



## 'Other' Value Counts {#otherCnt}
Altus AFB's geodatabase was analyzed for data with attributes classified as 'Other' at the Feature Class Attribute level. Overall, 500/252,936 (0.2%) *Other* cells exist within standard Feature Classes in Altus AFB's geodatabase.  


For the purposes of this report, 'Other' data is classified as any Feature Class Attribute Table cell that contains one of the following values:

1. 'Other'
2. 'other'
3. 'OTHER'
4. '88888'

Please see Tables \@ref(tab:cotherCntFDS) & \@ref(tab:cotherCntFC) for a count of 'Other' cells by Feature Dataset and Feature Class, respectively.


A more detailed breakdown of the individual values and counts of values for each *field* may be found in the Altus AFB_Indeterminant_Data-CIP Excel Workbook within the 'CIP_MissingData' table/sheet under the 'OTHER_VALUE_COUNTS' column.   Further, you may see the counts of 'Null' cells by standard Feature Class in the 'CIP_OtherCellCountbyFC' Table, or by Field in the 'CIP_OtherCellCountbyFLD' Table, in the Altus AFB_Indeterminant_Data-CIP Excel Workbook provided with this report.

###  'Other' Count by Feature Dataset {#otherCntFDS}
\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}cc}
\caption{(\#tab:cotherCntFDS)Count of Other Cells by Feature Dataset}\\
\hiderowcolors
\toprule
FDS & Total\_Other\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cotherCntFDS)Count of Other Cells by Feature Dataset \textit{(continued)}}\\
\toprule
FDS & Total\_Other\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{500 Total 'Other' Cells}\\
\endlastfoot
\showrowcolors
Cadastre & 5\\
environmentalRestoration & 11\\
MilitaryRangeTraining & 1\\
Planning & 10\\
Transportation & 473\\*
\end{longtable}
\rowcolors{2}{white}{white}

###  'Other' Count by Feature Class {#otherCntFC}

\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccc}
\caption{(\#tab:cotherCntFC)Count of Other Cells by Feature Class}\\
\hiderowcolors
\toprule
FDS & FC & Total\_Other\_Count\\
\midrule
\endfirsthead
\caption[]{(\#tab:cotherCntFC)Count of Other Cells by Feature Class \textit{(continued)}}\\
\toprule
FDS & FC & Total\_Other\_Count\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{500 Total 'Other' Cells}\\
\endlastfoot
\showrowcolors
Cadastre & Installation\_A & 5\\
MilitaryRangeTraining & MilRange\_A & 1\\
Planning & AirAccidentZone\_A & 10\\
Transportation & Bridge\_A & 2\\
Transportation & RoadCenterline\_L & 302\\
Transportation & VehicleParking\_A & 169\\
environmentalRestoration & EnvRemediationSite\_A & 11\\*
\end{longtable}
\rowcolors{2}{white}{white}


# Differences Between Altus AFB's Geodatabase and the CIP Standard Schema {#diff}

## Fields with Incorrectly Populated Domains {#diffIncDom}


Within the standard Feature Classes included in Altus AFB's geodatabase from the CIP schema, this section identifies the count of domain-constrained fields that have values outside of the domain values. In total, 0 fields have values that are not included in a field's domain.  

Please see Table \@ref(tab:cdiffIncDom2) below for the counts of incorrectly populated domains/fields by feature class.


A more detailed breakdown of the individual incorrectly-populated values and counts of these values may be found in the Altus AFB_Indeterminant_Data-CIP Excel Workbook accompanying this report within the 'CIP_MissingData' table/sheet under the 'INC_POP_VALS' column.   




\begin{table}[!h]

\caption{(\#tab:cdiffIncDom2)Count of Incorrectly Populated Domains by Feature Class}
\centering
\begin{tabular}{l|l|r}
\hline
FDS & FC & Incorrectly\_Populated\_Field\_Count\\


\hline
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{0 Total Count of Fields}\\
\end{tabular}
\end{table}



## Fields Included in Altus AFB's Geodatabase Not in CIP {#diffFLD}
In total, 208 fields are included in Altus AFB's geodatabase that are not included in the CIP schema for each standard Feature Class included. Tables \@ref(tab:cdiffFLDnotFDS) & \@ref(tab:cdiffFLDnotFC) below lists counts of these fields by Feature Dataset and by Feature Class, respectively.  

In general, across AF Installations, if the Feature Class was included, Non-standard fields derived largely from fields such as "LAST_EDITED_DATE", "LAST_EDITED_USER", or "CREATED_DATE", therefore it is recommended that you cross-reference this sections with Section \@ref(missFLDincFC), where applicable. Further, for a more detailed listing of the individual non-standard *fields* included in Altus AFB's geodatabase, see the 'CIP_MissingData' table/sheet in the Altus AFB_Indeterminant_Data-CIP Excel Workbook under the 'NON_SDS' column. Fields that are not included the CIP geodatabase will have the 'NON_SDS' column equal to 'T' (for 'True').  


### Fields Included in Altus AFB's Geodatabase Not in CIP Schema by Feature Dataset {#diffFLDnotFDS}

\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}cc}
\caption{(\#tab:cdiffFLDnotFDS)Count of Fields not in Target Geodatabase by Feature Dataset}\\
\hiderowcolors
\toprule
FDS & NON\_SDS\_FIELD\_COUNT\\
\midrule
\endfirsthead
\caption[]{(\#tab:cdiffFLDnotFDS)Count of Fields not in Target Geodatabase by Feature Dataset \textit{(continued)}}\\
\toprule
FDS & NON\_SDS\_FIELD\_COUNT\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{2}{l}{\textbf{Note: } }\\
\multicolumn{2}{l}{208 Total Count of Fields}\\
\endlastfoot
\showrowcolors
Auditory & 6\\
Cadastre & 33\\
environmentalCulturalResources & 6\\
environmentalNaturalResources & 6\\
environmentalRestoration & 6\\
MilitaryRangeTraining & 24\\
Pavements & 17\\
Planning & 12\\
RealProperty & 14\\
Recreation & 12\\
Security & 20\\
Transportation & 46\\
WaterWays & 6\\*
\end{longtable}
\rowcolors{2}{white}{white}


### Fields Included in Altus AFB's Geodatabase Not in CIP Schema by Feature Class {#diffFLDnot}

\rowcolors{2}{white}{gray!6}

\begin{longtable}{>{\bfseries}ccc}
\caption{(\#tab:cdiffFLDnotFC)Count of Fields not in Target Geodatabase by Feature Class}\\
\hiderowcolors
\toprule
FDS & FC & NON\_SDS\_FIELD\_COUNT\\
\midrule
\endfirsthead
\caption[]{(\#tab:cdiffFLDnotFC)Count of Fields not in Target Geodatabase by Feature Class \textit{(continued)}}\\
\toprule
FDS & FC & NON\_SDS\_FIELD\_COUNT\\
\midrule
\endhead
\
\endfoot
\bottomrule
\multicolumn{3}{l}{\textbf{Note: } }\\
\multicolumn{3}{l}{208 Total Count of Fields}\\
\endlastfoot
\showrowcolors
Auditory & NoiseZone\_A & 6\\
Cadastre & Installation\_A & 6\\
Cadastre & LandParcel\_A & 7\\
Cadastre & Outgrant\_A & 7\\
Cadastre & Site\_A & 6\\
Cadastre & Site\_P & 7\\
environmentalCulturalResources & HistoricDistrict\_A & 6\\
environmentalNaturalResources & Wetland\_A & 6\\
environmentalRestoration & EnvRemediationSite\_A & 6\\
MilitaryRangeTraining & ImpactArea\_A & 6\\
MilitaryRangeTraining & MilQuantityDistCombinedArc\_A & 6\\
MilitaryRangeTraining & MilRange\_A & 6\\
MilitaryRangeTraining & MilTrainingLoc\_A & 6\\
Pavements & PavementBranch\_A & 11\\
Pavements & PavementSection\_A & 6\\
Planning & AirAccidentZone\_A & 6\\
Planning & LandUse\_A & 6\\
RealProperty & Building\_A & 7\\
RealProperty & Tower\_P & 7\\
Recreation & GolfCourse\_A & 6\\
Recreation & RecArea\_A & 6\\
Security & AccessControl\_L & 8\\
Security & AccessControl\_P & 6\\
Security & Fence\_L & 6\\
Transportation & Bridge\_A & 6\\
Transportation & Bridge\_L & 6\\
Transportation & RailSegment\_L & 7\\
Transportation & RailTrack\_L & 7\\
Transportation & RoadCenterline\_L & 7\\
Transportation & RoadPath\_L & 7\\
Transportation & VehicleParking\_A & 6\\
WaterWays & DocksAndWharfs\_A & 6\\*
\end{longtable}
\rowcolors{2}{white}{white}




\pagebreak


# Production Information {#prodInfo}
This report was created using R [@R-base] and RStudio [@Rstudio] with the following packages: 

- bookdown [@R-bookdown]
- knitr [@R-knitr]
- rmarkdown [@R-rmarkdown]
- tinytex [@R-tinytex]


For posterity, package information is listed below:   

```
## R version 3.4.1 (2017-06-30)
## Platform: x86_64-w64-mingw32/x64 (64-bit)
## Running under: Windows >= 8 x64 (build 9200)
## 
## Matrix products: default
## 
## locale:
## [1] LC_COLLATE=English_United States.1252 
## [2] LC_CTYPE=English_United States.1252   
## [3] LC_MONETARY=English_United States.1252
## [4] LC_NUMERIC=C                          
## [5] LC_TIME=English_United States.1252    
## 
## attached base packages:
## [1] stats     graphics  grDevices utils     datasets  methods   base     
## 
## other attached packages:
##  [1] bindrcpp_0.2.2        anchors_3.0-8         MASS_7.3-49          
##  [4] rgenoud_5.8-1.0       purrr_0.2.4           kableExtra_0.7.0.9000
##  [7] Rcpp_0.12.16          devtools_1.13.4       sf_0.6-1             
## [10] rmarkdown_1.9.12      markdown_0.8          knitr_1.20           
## [13] stringr_1.3.0         DT_0.4                leaflet_1.1.0        
## [16] dplyr_0.7.4           ggplot2_2.2.1         yaml_2.1.19          
## [19] tinytex_0.5           bookdown_0.7         
## 
## loaded via a namespace (and not attached):
##  [1] xfun_0.1          colorspace_1.3-2  viridisLite_0.3.0
##  [4] htmltools_0.3.6   rlang_0.2.0       e1071_1.6-8      
##  [7] pillar_1.2.1      glue_1.2.0        withr_2.1.2      
## [10] DBI_0.8           bindr_0.1.1       plyr_1.8.4       
## [13] munsell_0.4.3     gtable_0.2.0      rvest_0.3.2      
## [16] htmlwidgets_1.0   evaluate_0.10.1   memoise_1.1.0    
## [19] labeling_0.3      httpuv_1.3.6.2    crosstalk_1.0.0  
## [22] class_7.3-14      xtable_1.8-2      udunits2_0.13    
## [25] readr_1.1.1       scales_0.5.0      backports_1.1.2  
## [28] classInt_0.1-24   mime_0.5          hms_0.4.2        
## [31] packrat_0.4.9-1   digest_0.6.15     stringi_1.1.7    
## [34] shiny_1.0.5       grid_3.4.1        rprojroot_1.3-2  
## [37] tools_3.4.1       magrittr_1.5      lazyeval_0.2.1   
## [40] tibble_1.4.2      pkgconfig_2.0.1   xml2_1.2.0       
## [43] httr_1.3.1        rstudioapi_0.7    assertthat_0.2.0 
## [46] R6_2.2.2          units_0.5-1       compiler_3.4.1
```

