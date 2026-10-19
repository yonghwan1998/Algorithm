SELECT
      tree.item_id AS 'ITEM_ID'
    , info.item_name AS 'ITEM_NAME'
FROM item_tree tree
JOIN item_info info
  ON tree.item_id = info.item_id
WHERE tree.parent_item_id IS NULL
ORDER BY ITEM_ID ASC;