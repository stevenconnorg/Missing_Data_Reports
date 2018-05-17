### setup packages with init.R
source("R/init.R")

### get gdb and target-gdb paths
installationGDBs <- list.files(paste0(getwd(),"/dat/gdbs-complete"),full.names = T,pattern=".gdb")
targetGDBs <- list.files(paste0(getwd(),"/dat/gdbs-target"),full.names = T)

### then knit pdf reports in a loop with bookdown::pdf_document2
library(bookdown)
library(tinytex)
library(yaml)
for (installationGDB in installationGDBs){
  for (targetGDB in targetGDBs){

      tbasename<-basename(targetGDB)
      compName<-tools::file_path_sans_ext(tbasename)
      
      basename<-basename(installationGDB)
      installationName<-tools::file_path_sans_ext(basename)
      
      reportDir<-paste0(getwd(),"/out/Reports/",compName)
      dir.create(reportDir,recursive=TRUE,showWarnings = F)

      # using bookdown::pdf_document2() to render, ensures cross-references linked and referenced
      
      rmarkdown::render(input = paste0(getwd(),"/R/Installation_Reports.Rmd"),
                        output_file = paste0(installationName,"_Missing_Data_Report_",compName),
                        output_dir = reportDir,
                        clean= FALSE,
                        pdf_document2(toc = TRUE, number_sections = TRUE, fig_caption = TRUE,  toc_unnumbered = FALSE, toc_appendix = TRUE, toc_bib = TRUE, quote_footer = NULL, highlight_bw = FALSE)
                        )
      
      # rmarkdown::render(input = paste0(getwd(),"/R/Installation_Reports-html.Rmd"),
      #                   output_file = paste0(installationName,"_Missing_Data_Report_",compName,".html"),
      #                   output_dir = reportDir,
      #                   clean= FALSE,
      #                   gitbook(self_contained=TRUE,
      #                           #code_download=TRUE,
      #                           #theme = "default",
      #                           smart=TRUE,
      #                           keep_md=FALSE,
      #                           df_print="kable",
      #                           number_sections = TRUE,
      #                           split_by = c("none"),
      #                           fig_caption = TRUE,
      #                           toc_unnumbered = FALSE,
      #                           toc_appendix = TRUE,
      #                           toc_bib = TRUE,
      #                           quote_footer = NULL,
      #                           highlight_bw = FALSE
      #                           )
      # )
      
      
      # without bookdown::pdf_document2 ... won't have cross-references correctly configured, but has less software dependencies
      # rmarkdown::render(input = paste0(getwd(),"/Installation_Reports.Rmd"),
      #         output_format = "pdf_document",
      #         output_file = paste0(installationName,"_Missing_Data_Report_",compName,"_",Sys.Date(),".pdf"),
      #         output_dir = reportDir)
      
      
       # remove params after loop or else you get error:"params object already exists in knit environment so can't be overwritten by render params" or a memory error
      rm(params)
      rm(list=setdiff(ls(), c("installationGDBs","installationGDB","targetGDBs","targetGDB")))
      
      }
}



