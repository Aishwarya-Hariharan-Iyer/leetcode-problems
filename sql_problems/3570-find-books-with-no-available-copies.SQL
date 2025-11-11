# Write your MySQL query statement below
WITH current_borrower_count AS (
    SELECT book_id, COUNT(*) AS current_borrowers
    FROM borrowing_records
    WHERE return_date IS NULL
    GROUP BY book_id
)

SELECT library_books.book_id, library_books.title, library_books.author, library_books.genre, library_books.publication_year, current_borrower_count.current_borrowers
FROM library_books, current_borrower_count
WHERE library_books.total_copies = 0 OR (library_books.book_id = current_borrower_count.book_id AND library_books.total_copies - current_borrower_count.current_borrowers = 0)
ORDER BY current_borrower_count.current_borrowers DESC, library_books.title ASC