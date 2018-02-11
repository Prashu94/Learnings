library(sendmailR)
library(xtable)

msg <- mime_part(paste('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0
Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
                       <html xmlns="http://www.w3.org/1999/xhtml">
                       <head>
                       <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                       <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                       </head>
                       <body>', print(xtable(s), type = 'html'), ',</body>
                       </html>'))
msg[["headers"]][["Content-Type"]] <- "text/html"

from    <- 'prashantbhat94@gmail.com'
to      <- 'prashantbhat94@gmail.com'
subject <- 'HTML table in the body'
body    <- list(msg)
sendmail(from, to, subject, body,control = list(smtpServer= "smtp.gmail.com"))