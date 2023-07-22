/*join data sets*/

SELECT NOC
FROM P1_df
INNER JOIN P2_df
ON P1_df.NOC = P2_df.NOC;

