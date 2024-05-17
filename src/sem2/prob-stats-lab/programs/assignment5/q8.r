N <- 50; M <- 10; n <- 7; x <- 0:n
hp <- dhyper(x, M, N - M, n)
d <- data.frame(x, hp)
d
plot(x, hp, "h")

cp <- phyper(x, M, N - M, n)
cp1 <- round(cp, 4)
di <- data.frame(x, cp1)
di
plot(x, cp1, "s")
