grp <- seq(0, 5)
f <- c(5, 35, 2, 24, 25, 35)
x <- rep(grp, f)
crange <- (max(x) - min(x)) / (max(x) + min(x))
QD <- (quantile(x, 3 / 4) - quantile(x, 1 / 4)) / 2
CQD <- (quantile(x, 3 / 4) - quantile(x, 1 / 4)) / (quantile(x, 3 / 4) + quantile(x, 1 / 4))
x
diff(range(x))
crange
QD
CQD
