library(mailR)
library(xtable)
library(sendmailR)
s<- read.csv("G:\\extra things\\Knowledge\\Practice\\RP\\datasets\\MovieD.csv",header=T,sep=',');


msg <- mime_part(paste('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0
Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>
</html>'))

msg[["headers"]][["Content-Type"]] <- "text/html"

sender <- "prashantbhat94@gmail.com"
recipients <- c("prashantbhat94@gmail.com")
send.mail(from = sender,
          to = recipients,
          subject="Subject of the email",
          body = paste(print(xtable(s),type = 'html',style='grid'),collapse = "<br>"),
          smtp = list(host.name = "smtp.gmail.com", port = 465, 
                      user.name="prashantbhat94@gmail.com", passwd="spidermanshalinipbhats52@", ssl=TRUE),
          authenticate = TRUE,
          send = TRUE)