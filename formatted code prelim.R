#Variable formatting
amerinames <- progectdata[progectdata$`American name?` == 1,]
imminames <- progectdata[progectdata$`American name?` == 0,]
noout <- progectdata[progectdata$`View count` < 10000001,]
options(scipen = 100) #Used to disable scientific notation on graphs for readability

#Graphs in order of their appearance:
hist(noout$`View count`, main = "View count of TED talks", xlab = "View count")
hist(progectdata$`Number of words in title`, main = "Number of Words in Title", xlab = "Words")
scatterplot(noout$`Number of words in title`,noout$`View count`, xlab = "Words in Title", ylab = "View Count", main = "View count vs Word count for <10M views")
scatterplot(noout$`Number of words in title`[noout$`View count` < 2000001],noout$`View count`[noout$`View count` < 2000001],
            xlab = "Words in Title", ylab = "View Count", main = "View count vs Word count for <2M views")
table(progectdata$`American name?`)
boxplot(amerinames$`View count`[amerinames$`View count` < 4000001], imminames$`View count`[imminames$`View count` < 4000001], 
        names = c("American name", "non-American name"), main = "View count vs Name for Views <4M", ylab = "View Count", xlab = "Name")

#Number of "viral" videos:
length(progectdata$`View count`[progectdata$`View count`>10000000])

#Descriptive statistics for misc.
mean(progectdata$`View count`)
min(progectdata$`View count`)
median(progectdata$`View count`)

mean(amerinames$`View count`)
mean(imminames$`View count`)
mean(amerinames$`View count`) - mean(imminames$`View count`) #Difference in means

mean(progectdata$`Number of words in title`)
median(progectdata$`Number of words in title`)
max(progectdata$`Number of words in title`)