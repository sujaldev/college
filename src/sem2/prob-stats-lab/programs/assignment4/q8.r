grp <- seq(0, 5)
f <- c(5, 35, 2, 24, 25, 35)
x <- rep(grp, f)
psd <- (sd(x) * length(x) - 1) / sqrt(length(x))
cv <- (psd / mean(x)) * 100
var(x)
sd(x)
cv