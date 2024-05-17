x <- 0:5
f <- c(142, 156, 69, 27, 5, 1)
m <- sum(x * f) / sum(f)
px <- dpois(x, m)
px <- round(px, 4)
ef <- sum(f) * px
ef1 <- round(ef, 0)
d <- data.frame(x, f, "expected frequency" = ef)
d
plot(f, ef1, pch = "x")
abline(0, 1)