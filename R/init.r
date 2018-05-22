#library(packrat)
#packrat::init(options = list(ignored.packages = c()))
# packrat::snapshot()
# packify()
# packrat::bundle(project = NULL, file = NULL, include.src = TRUE,
#                  include.lib = FALSE, include.bundles = TRUE,
#                  include.vcs.history = TRUE, overwrite = TRUE, omit.cran.src = TRUE)


Install_And_Load <- function(Required_Packages)
{
  Remaining_Packages <- Required_Packages[!(Required_Packages %in% installed.packages()[,"Package"])];
  
  if(length(Remaining_Packages)) 
  {
    install.packages(Remaining_Packages,dependencies=TRUE);
  }
  for(package_name in Required_Packages)
  {
    library(package_name,character.only=TRUE,quietly=TRUE);
  }
}

requiredPackages = c('packrat'
                     ,'rprojroot'
                     ,'ggplot2'
                     ,'dplyr'
                     ,'leaflet'
                     ,'DT'
                     ,'stringr'
                     ,'knitr'
                     ,'markdown'
                     ,'rmarkdown'
                     ,'sf'
                     ,'ggmap'
                     ,'Rcpp'
                     ,'bookdown'
                     ,'purrr'
                     ,'bibtex'
                     ,'anchors'
                     ,'digest'
                     ,'backports'
                     ,'devtools'
                     ,'yaml'
                     ,'RgoogleMaps'
)

Install_And_Load(requiredPackages)

devtools::install_github('rstudio/rmarkdown')
#
if (!require('rmarkdown', character.only=TRUE)) {
  install_version("rmarkdown", version = 1.9)
  library(rmarkdown)
} else {
  library(rmarkdown)
}

if (!require('knitr', character.only=TRUE)) {
  devtools::install_github("haozhu233/kableExtra")
  library(knitr)
} else {
  library(knitr)
}

if (!require('kableExtra', character.only=TRUE)) {
  install_version("kableExtra", version = 1.9)
  library(kableExtra)
} else {
  library(kableExtra)
}

if (!require('rmarkdown', character.only=TRUE)) {
  install_version("rmarkdown", version = 1.9)
  library(rmarkdown)
} else {
  library(rmarkdown)
}

if (!require('tinytex', character.only=TRUE)) {
  devtools::install_github('yihui/tinytex')
  library(tinytex)
  
} else {
  library(tinytex)

}

# if this fails, try installing (Active) Perl on your computer and re-try. - https://www.perl.org/get.html
# https://github.com/yihui/tinytex/issues/45
if (tinytex:::is_tinytex()){
  print("TinyTeX already installed! -- No forced installation committed.")
} else{
  print("Installing TinyTeX within the TinyTeX R package (tinytex::install_tinytex())")
  tinytex::install_tinytex()
}

