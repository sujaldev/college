attended <- c(2, 4, 5, 6)
total <- rep(10, 4)

attendance <- data.frame(
  'Classes Attended' = attended, 'Total Classes' = total,
  row.names = c('BS106', 'A201', 'BS158', 'A104')
)

attendance
