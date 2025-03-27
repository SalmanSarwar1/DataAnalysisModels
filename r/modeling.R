train_linear_model <- function(data, x_column, y_column) {
  formula <- as.formula(paste(y_column, "~", x_column))
  model <- lm(formula, data = data)
  return(model)
}