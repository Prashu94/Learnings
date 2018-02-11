library(xlsx)
library(RJDBC)

drv <- JDBC('oracle.jdbc.OracleDriver', "G:/extra things/Knowledge/Drivers/ojdbc14.jar")
con <- dbConnect(drv, "jdbc:oracle:thin:@hp:1521:XE","PRASHANT","batman7")
data_xl <- read.xlsx("G:/extra things/Knowledge/practice/RP/datasets/IPlanFeb.xlsx",1,stringsAsFactors ='F')
idf<- as.data.frame(data_xl)
idf
View(idf)
str(idf)
idf$PLANNER_MONTH_YEAR<- format(idf$PLANNER_MONTH_YEAR,"%d-%b-%Y")
idf$START_DATE<- format(idf$START_DATE,"%d-%b-%Y")
idf$END_DATE<- format(idf$END_DATE,"%d-%b-%Y")

for(row in 1:nrow(idf)) {   
  query1<-"UPDATE rip_db SET COMPLETION_PERCENT= %s,ACTUAL_EFFORT= %s,END_DATE= '%s',REMARKS= '%s',CLIENT= '%s',ENV= '%s',RCA= '%s'"
  query2<-"commit"
  dbSendUpdate(con,paste(sprintf(query1,idf$COMPLETION_PERCENT[row],idf$ACTUAL_EFFORT[row],idf$END_DATE[row],idf$REMARKS[row],idf$CLIENT[row],idf$ENV[row],idf$RCA[row]),collapse=""))
}
  