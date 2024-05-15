students <- c("Alice", "Bob", "Eve")
subjects <- c("Physics", "Chemistry", "Mathematics")
marks <- c(2, 5, 1, 4, 1, 2, 8, 7, 2)

results <- matrix(marks, ncol = 3, nrow = 3)
rownames(results) <- subjects
colnames(results) <- students

pdf(width = 6, height = 3)
barplot(results, beside = TRUE)
