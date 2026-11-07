SELECT
    child.id AS 'ID'
FROM ecoli_data grand
JOIN ecoli_data parent
  ON grand.id = parent.parent_id
JOIN ecoli_data child
  ON parent.id = child.parent_id
WHERE grand.parent_id IS NULL
ORDER BY ID ASC;