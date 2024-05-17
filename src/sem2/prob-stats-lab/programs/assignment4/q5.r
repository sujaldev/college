x <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mad(x)
mad(x) / median(x)
var(x)
psd <- (sd(x) / mean(x)) * 100
psd
(psd / mean(x)) * 100
