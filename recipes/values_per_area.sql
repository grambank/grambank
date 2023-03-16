SELECT
  q1.cldf_macroarea, coalesce(cldf_value, '?'), cast(count_one AS float) / count_all * 100
FROM
  (
    SELECT 
      l.cldf_macroarea, count(v.cldf_id) AS count_all 
    FROM 
      ValueTable AS v, LanguageTable AS l 
    WHERE 
      l.cldf_macroarea IS NOT NULL AND l.cldf_id = v.cldf_languageReference AND v.cldf_parameterReference = 'GB020'
    GROUP BY 
      l.cldf_macroarea
  ) as q1
  LEFT JOIN
  (
    SELECT 
      l.cldf_macroarea, v.cldf_value, count(v.cldf_id) AS count_one 
    FROM 
      ValueTable AS v, LanguageTable AS l 
    WHERE 
      l.cldf_macroarea IS NOT NULL AND l.cldf_id = v.cldf_languageReference AND v.cldf_parameterReference = 'GB020' 
    GROUP BY 
      l.cldf_macroarea, v.cldf_value
    ) as q2
    ON q1.cldf_macroarea = q2.cldf_macroarea
ORDER BY
  q1.cldf_macroarea, coalesce(cldf_value, '?')
;

