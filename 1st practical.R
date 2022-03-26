set.seed(1)
#Generate random numbers and store it in a variable called data
data = runif(20,1,10)
data

#calculate mean
mean = mean(data)
print(mean)

#calculate median
median=median(data)
print(median)

#create a function for calculating mode
mode <- function(x) {
  ux  <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}
result <- mode(data)
print(data)
cat("mode= {}", result)

# Calculate Variance and std Deviation
variance = var(data)
standardDeviation = sqrt(var(data))
print(standardDeviation)
print(variance)

#plot Histogram
hist(data, bins=10, range= c(0,10), edgecolor='black')



