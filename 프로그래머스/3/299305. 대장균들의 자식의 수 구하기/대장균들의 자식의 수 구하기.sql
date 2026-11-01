SELECT
      parent.id AS 'ID'
    , COUNT(child.parent_id) 'CHILD_COUNT'
FROM ecoli_data parent
LEFT JOIN ecoli_data child
  ON parent.id = child.parent_id
GROUP BY parent.id
ORDER BY ID ASC;