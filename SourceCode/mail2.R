library(mailR)
library(pander)


s<- read.csv("G:\\extra things\\Knowledge\\Practice\\RP\\datasets\\MovieD.csv",header=T,sep=',');
dput(s)
structure(list(Description = c("ServerA", "ServerB", "ServerC", 
                               "ServerD", "ServerE", "ServerF"), Value = c("2", "2", "100", 
                                                                           "100", "80", "20")), .Names = c("Description", "Value"), row.names = c(NA, 
                                                                                                                                                  6L), class = "data.frame")
t<-pandoc.table.return(s, caption="Server CPU Utilization",style = "")

from <- "prashantbhat94@gmail.com"
to <- c("prashantbhat94@gmail.com")
#subject <- paste(Sys.time()," Servers CPU utilization")
body <- t                
#mailControl=list(smtpServer="mailhost.example.net")

send.mail(from = sender,
          to = recipients,
          subject="Subject of the email",
          body = t,
          smtp = list(host.name = "smtp.gmail.com", port = 465, 
                      user.name="prashantbhat94@gmail.com", passwd="spidermanshalinipbhats52@", ssl=TRUE),
          authenticate = TRUE,
          send = TRUE)