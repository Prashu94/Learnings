library(rmarkdown)
rmarkdown::render("mailing.rmd")
library(base64enc)
library(mailR)

send.mail(from = "prashantbhat94@gmail.com",
          to = "prashantbhat94@gmail.com",
          subject = "R Markdown Report - rmarkdown",
          html = T,
          #inline = T,
          body = "mailing.html",
          smtp = list(host.name = "smtp.gmail.com", port = 465, user.name = "prashantbhat94@gmail.com", passwd = "spidermanshalinipbhats52@", ssl = T),
          authenticate = T,
          send = T)
?markdown::markdownHTMLOptions

#compile using knitr
library(knitr)
setwd("G:\\extra things\\Knowledge\\practice\\RP\\SourceCode")
getwd()
knit2html("mailing.Rmd",options="")

send.mail(from = "prashantbhat94@gmail.com",
          to = "prashantbhat94@gmail.com.com",
          subject = "R Markdown Report - knitr",
          html = T,
          #inline = T,
          body = "mailing.html",
          smtp = list(host.name = "smtp.gmail.com", port = 465, user.name = "prashantbhat94@gmail.com", passwd = "spidermanshalinipbhats52@", ssl = T),
          authenticate = T,
          send = T)