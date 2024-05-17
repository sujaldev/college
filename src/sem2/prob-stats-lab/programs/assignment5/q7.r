n <- 8
p <- 0.65
x <- 0:n
bp <- dbinom(x, n, p)
d <- data.frame(x, "probabilities" = bp)
d
plot(x, bp, "h")

cp <- pbinom(x, n, p)
cp1 <- round(cp, 4)
d1 <- data.frame(x, cp1)
plot(x, cp1)

plot(x, cp1, "s")