m <- 2.6
x <- 0:10
p <- dpois(x, m)
d <- data.frame(x, p)
d
plot(x, p, "h")

cp <- ppois(x, m)
cp1 <- round(cp, 4)
d1 <- data.frame(x, cp1)
plot(x, cp1, "s")
