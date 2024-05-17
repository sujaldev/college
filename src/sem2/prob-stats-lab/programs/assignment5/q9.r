li <- seq(144, 180, 6); ul <- seq(150, 186, 6)
f <- c(3, 12, 23, 52, 61, 39, 10)
x <- (li + ul) / 2; n <- sum(f); k <- length(f)
m <- sum(f * x) / n; v <- sum(f * (x - m)^2) / n; sd <- sqrt(v)
l1 <- c(-9999, li, 186)
cp <- pnorm(l1, m, sd)
p <- diff(cp)
p <- c(p, 1 - cp[k + 2])
ul <- c(144, ul, 9999); f <- c(0, f, 0)
ef <- round(n * p, 0)
d <- data.frame(
  "Lower Limit" = l1, "Upper Limit" = ul, "Obs. freq" = f,
  "prob" = p, "cumprob" = cp, "expfreq" = ef
)
d
plot(f, ef, xlab = "obs.freq", ylab = "exp.freq", "p"); abline(0, 1)
