library(xlsx)
library(RJDBC)
library(RSQLite)
drv <- JDBC('oracle.jdbc.OracleDriver', "G:/extra things/Knowledge/Divers/ojdbc14.jar")
con <- dbConnect(drv,"jdbc:oracle:thin:@hp:1521:XE","PRASHANT","batman7")
data_xl <- read.xlsx("G:/extra things/Knowledge/practice/RP/datasets/IPlanFeb.xlsx",1,stringsAsFactors ='F')
idf<- as.data.frame(data_xl)
idf
#View(idf)
str(idf)
idf$PLANNER_MONTH_YEAR<- format(idf$PLANNER_MONTH_YEAR,"%d-%b-%Y")
idf$START_DATE<- format(idf$START_DATE,"%d-%b-%Y")
idf$END_DATE<- format(idf$END_DATE,"%d-%b-%Y")
dbWriteTable(con,"RIP_DB",idf)
#query1<-"UPDATE rip_db SET PID='%s',SCP_ID='%s',SUB_ACTIVITY_NAME='%s',COMPLETION_PERCENT= %s,ACTUAL_EFFORT= %s,END_DATE= '%s',REMARKS= '%s',CLIENT= '%s',ENV= '%s',RCA= '%s'"

for(row in 1:nrow(idf)) {
  dbSendUpdate(conn = con,"UPDATE rip_db SET PID = ",idf$PID[row],",  OWNER ='",idf$OWNER[row],",SCP_ID=",idf$SCP_ID[row],",SUB_ACTIVITY_NAME='",idf$SUB_ACTIVITY_NAME[row],"',COMPLETION_PERCENT=",idf$COMPLETION_PERCENT[row],",ACTUAL_EFFORT=",idf$ACTUAL_EFFORT[row],"END_DATE=",idf$END_DATE[row],",REMARKS=",idf$REMARKS[row],",CLIENT=",idf$CLIENT[row],",ENV=",idf$ENV[row],",RCA=",idf$RCA[row],"")
  dbCommit(conn = con)
  }
#dbSendUpdate(con,paste(sprintf(query1,idf$PID[row],idf$SCP_ID[row],idf$SUB_ACTIVITY_NAME[row],idf$COMPLETION_PERCENT[row],idf$ACTUAL_EFFORT[row],idf$END_DATE[row],idf$REMARKS[row],idf$CLIENT[row],idf$ENV[row],idf$RCA[row],query2),collapse=""))