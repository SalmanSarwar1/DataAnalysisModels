load_csv <- function(file_path) {
  if (!file.exists(file_path)) {
    stop("File not found: ", file_path)
  }
  data <- read.csv(file_path)
  return(data)
}