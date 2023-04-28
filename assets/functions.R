install.packages("paws", lib="/tmp/data/lib")# nolint: line_length_linter.
source("./s2_list.R")

species <- "picea_abies"
rep_in <- "/tmp/data"
tuile <- "T31TGN"
date_start <- "2023-03-15"
date_end <- as.character(Sys.Date())

download <- s2_list(
  tiles = c("T31TGN"),
  time_interval = c(date_start, date_end),
  level = "l2a",
  platform = "s2a",
  time_period = "full",
  maxcloud = 45,
  collection = "sentinel2",
  path_to_download = rep_in,
  project_name = species,
  download = TRUE,
  extract = FALSE)