
-- Create all stats Table
CREATE TABLE all_stats (
  id SERIAL PRIMARY KEY,	
  team TEXT,
  season TEXT,
  Rel_Pace  DECIMAL,
  Rel_ORtg DECIMAL,
  Rel_DRtg DECIMAL,
  Chip TEXT
);


--Drop  all stats table
DROP TABLE all_stats



-- Create Champs Table
CREATE TABLE champs (
  id SERIAL PRIMARY KEY,	
  Team object,
  Rel_Pace float64,
  Rel_ORtg float64,
  Rel_DRtg float64,
  Playoffs float64,
  Age object,
  Ht. float64,
  Wt. object,
  FGA object,
  FG% object,
  3PA  object,
  3P% object,
  2PA object,
  2P% object,
  FTA object,
  FT% object,
  ORB object,
  DRB object,
  AST object,
  STL object,
  BL object,
  TOV object,
  PF object,
  PTS object,
  Predicted float64,
  Error float64 
);



--Drop champs table
DROP TABLE champs