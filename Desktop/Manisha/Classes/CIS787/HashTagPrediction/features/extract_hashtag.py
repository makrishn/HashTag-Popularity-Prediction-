extract_hashtags <- function(text){
  hashtags = regmatches(text,gregexpr("#(\\d|\\w)+",text))
  hashtags = unlist(hashtags)
  hashtags = table(hashtags)
  sorted = order(hashtags, decreasing=TRUE)
  hashtags = ashtags[sorted]
  class(hashtags) = "hashtags"
  return(hashtags)
}
