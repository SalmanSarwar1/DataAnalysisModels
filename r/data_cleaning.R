handle_missing_values <- function(data, strategy = "mean", columns = NULL) {
  if (is.null(columns)) {
    columns <- colnames(data)
  }
  for (column in columns) {
    if (strategy == "mean") {
      data[[column]][is.na(data[[column]])] <- mean(data[[column]], na.rm = TRUE)
    } else if (strategy == "median") {
      data[[column]][is.na(data[[column]])] <- median(data[[column]], na.rm = TRUE)
    } else if (strategy == "drop") {
      data <- data[!is.na(data[[column]]), ]
    }
  }
  return(data)
}