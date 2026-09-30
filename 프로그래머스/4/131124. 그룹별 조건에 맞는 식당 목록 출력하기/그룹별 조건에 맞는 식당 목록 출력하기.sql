-- 코드를 입력하세요
SELECT
      mp.member_name
    , rr.review_text
    , rr.review_date
FROM rest_review rr
JOIN member_profile mp
ON rr.member_id = mp.member_id
WHERE rr.member_id = (
    SELECT
        member_id
    FROM rest_review
    GROUP BY member_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
ORDER BY rr.review_date ASC, rr.review_text ASC;