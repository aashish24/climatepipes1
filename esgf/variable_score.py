
import synonyms 

def match_using_synonyms( in_token, query_token ):
  syns = synonyms.get_synonyms_strict( query_token )
  print 'query_token is ', query_token
  print 'synonyms are ', syns
  for i in syns:    
    if( i.lower() == in_token.lower() ):
      return 0.5
    
  return 0.0
  
  
def get_rank( in_str, query_str ):
  
  # This is how this algorithm works
  # First compare tokens ( case insensitive ), if it matches
  # then we increment the rank by 1. If all the token from input matches
  # all the tokens from query then return with a score of 1.0
  # If not then match in_str tokens with query_str tokens synonyms, give 
  # a score of 0.5 if it matches.
  # Scale score in the range of ( 0 - 1 ) when done.
  
  if( ( len( query_str ) <= 0 ) or ( len( in_str ) <= 0 ) ):
    return 0
  
  import nltk
  from nltk.tokenize import word_tokenize as wst
  
  input_tokens = wst( in_str )  
  query_tokens = wst( query_str )
  
  # Default score
  score = 0;
  
  # First match tokens as it is, if failed
  # then use its synonyms for matching
  for i in query_tokens:
    for j in input_tokens:
      if( j.lower() == i.lower() ):
        score += 1.0
      else:
        score += match_using_synonyms( j, i )
  
  #If it is one to one match then return full score
  if( score == len( query_tokens ) ):
    return 1.0
  
  # Filter out not so useful tokens from the query
  query_core_tokens = []
  tags = nltk.pos_tag( query_tokens )
  for i in tags:
    if( synonyms.should_keep( i[1] ) == True ):
      query_core_tokens.append( i[0] )
  
  # First use core tokens and the original tokens
  # in case of no core tokens
  numberOfTokens = len( query_core_tokens )
  if( numberOfTokens <= 0 ):
    numberOfTokens = len( query_tokens )
  
  # Scale ( 0 - 1 ) range   
  if( numberOfTokens > 0 ):  
    score = score / ( numberOfTokens )
    return score
  else:
    return 0
  
  
