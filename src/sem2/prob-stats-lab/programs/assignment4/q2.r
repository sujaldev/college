x <- floor(runif(20, min = 0, max = 100))
x
QD <- (quantile(x, 3 / 4) - quantile(x, 1 / 4)) / 2
coeffQD <- (quantile(x, 3 / 4) - quantile(x, 1 / 4)) / (quantile(x, 3 / 4) + quantile(x, 1 / 4))
QD
coeffQD
