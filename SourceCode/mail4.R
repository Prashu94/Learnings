library(mailR)
library(xtable)
setwd("G:\\extra things\\Knowledge\\practice\\RP\\SourceCode")
getwd()
s<-("MovieD.csv")

send.mail(from = "prashantbhat94@gmail.com",
          to = "prashantbhat94@gmail.com.com",
          subject = "R Markdown Report - knitr",
          html = T,
          #inline = T,
          body <- paste(mime_part(print(s), "GregsData")),
          smtp = list(host.name = "smtp.gmail.com", port = 465, user.name = "prashantbhat94@gmail.com", passwd = "spidermanshalinipbhats52@", ssl = T),
          authenticate = T,
          send = T)
