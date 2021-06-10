
-- Create NBA Champs Table
CREATE TABLE all_stats (
  id SERIAL PRIMARY KEY,	
  team TEXT,
  season TEXT,
  Rel_Pace  DECIMAL,
  Rel_ORtg DECIMAL,
  Rel_DRtg DECIMAL,
  Chip TEXT
--   Predicted INT
);



-- Create NBA Champs Table

DROP TABLE all_stats