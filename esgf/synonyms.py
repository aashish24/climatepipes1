
# Keep only Nouns, Adverbs, Preposition, and Number
#------------------------------------------------------------------------------
def should_keep( str ):
  lstr = str.upper()
  if( lstr == "N" or lstr == "ADV" or lstr == "NUM" or lstr == "NP"
      or lstr == "NN" ):
    return True
  else:
    return False

#------------------------------------------------------------------------------
def simple_path( path ):
  return [s.lemmas[0].name for s in path]

# Remove duplicate words ( requires python > 2.5.4 )
#------------------------------------------------------------------------------
def remove_duplicates( synlist ):
  return list( set( synlist ) )

# Using wordnet to get synonyms
#------------------------------------------------------------------------------
def get_all_synonyms( word ):
  import nltk
  from nltk.tokenize import word_tokenize as wst
  from nltk.corpus import wordnet

  sets = wordnet.synsets( word )

  syns = []
  for i in sets:
    names = wordnet.synset( i.name )
    tags = nltk.pos_tag( names.lemma_names )

    for j in tags:
      if should_keep( j[1] ) == True:
        syns.append( j[0] )
  return syns

# Given a string get synonyms for nouns, adv, prep, and number
# Usage: get_synonyms_strict( 'sea temperature at height 1000' )
#------------------------------------------------------------------------------
def get_synonyms_strict( str ):
  import nltk
  from nltk.tokenize import word_tokenize as wst

  # Initialize to empty list
  synonyms = []

  tokens = wst( str )
  synonyms += tokens

  tags = nltk.pos_tag( tokens )

  for i in tags:
    if should_keep( i[1] ) == True:
      syns = get_all_synonyms( i[0] )
      synonyms = synonyms + syns

  return remove_duplicates( synonyms )
