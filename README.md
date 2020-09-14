# FPLBayesianNetwork

Introduction:
To find an expected value for points to be scored by each an every player in the league. Random variable X(name) ~ Expected points of player by the given name in the next gameweek

Variables:
 1   assists            NOT USED, R = ?     int64  
 2   bonus              NOT USED, R = ?     int64  
 3   bps                NOT USED, R = ?     int64  
 4   clean_sheets       NOT USED, R = 0     int64  
 5   creativity         NOT USED, R = ?     float64
 6   element            NOT USED, R = ?     int64  
 7   fixture            NOT USED, R = ?     int64  
 8   goals_conceded     NOT USED, R = ?     int64  
 9   goals_scored       NOT USED, R = ?     int64  
 10  ict_index          USED, R = 75%       float64
 11  influence          USED, R = 84%       float64
 12  kickoff_time       NOT USED, R = 0     object 
 13  minutes            USED, R = 60%       int64  
 14  opponent_team      NOT USED, R = 0     int64  
 15  own_goals          NOT USED, R = 0     int64  
 16  penalties_missed   NOT USED, R = 0     int64  
 17  penalties_saved    NOT USED, R = 0     int64  
 18  red_cards          NOT USED, R = 0     int64  
 19  round              NOT USED, R = ?     int64  
 20  saves              NOT USED, R = ?     int64  
 21  selected           NOT USED, R = 30%   int64  
 22  team_a_score       NOT USED, R = 0     int64  
 23  team_h_score       NOT USED, R = 0     int64  
 24  threat             NOT USED, R = ?     int64  
 25  total_points       NOT USED, R = 1     int64  
 26  transfers_balance  NOT USED, R = 0     int64  
 27  transfers_in       NOT USED, R = 0     int64  
 28  transfers_out      NOT USED, R = 0     int64  
 29  value              NOT USED, R = 50%   int64  
 30  was_home           NOT USED, R = 0     bool   
 31  yellow_cards       NOT USED, R = 0     int64  
 32  last_minutes       526 non-null    float64
]

Current model:
X(name, ict_index, influence, minutes) => ExpectedPoints: int

Method:
1) Conduct a regression analysis to determine variables best correlated with expected points
.
.
.
n) List the players in order of expected points for each position