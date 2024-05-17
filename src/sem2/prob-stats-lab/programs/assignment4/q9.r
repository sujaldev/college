library(moments)

x <- c(25, 29, 30, 17, 19, 30, 18, 28, 31, 33, 26, 28)
psd <- (sd(x) * sqrt(length(x) - 1)) / sqrt(length(x))
skp <- (3 * (mean(x) - median(x))) / psd
a <- quantile(x, 3 / 4)
b <- quantile(x, 1 / 4)
c <- 2 * quantile(x, 1 / 2)
skb <- (a + b - c) / (a - b)

skewness(x)