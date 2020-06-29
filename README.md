# koko_books
Calculate rental amount for verity of books, based on different story.
# Docker Build command
docker build . -t koko_books:latest
# Docker Run command 
docker run -p 9007:8080 -dit koko_books:latest
# To run test cases
docker run --entrypoint 'nosetests'  -t  koko_books:latest
# API 
http://virtual-machine:9007/kbooks/S1
OR
http://virtual-machine:9007/kbooks/S2
OR
http://virtual-machine:9007/kbooks/S3
# Payload 
Same payload can be used for diffrent endpoint. Ex. {'book_type' : [['book_name', 'rental_days']]}

{'fiction': [['The Paying Guests', '3'], ['A Tale of Two Cities', '5'], ['Watership Down', '6'], ['A Town Like Alice', '5'], ['The Book Thief', '1'], ['Brave New World', '1'], ['The Alchemist', '2']], 'regular': [['The Catcher in the Rye', '1'], ['1984', '3'], ['Ulysses', '1'], ['Catch-22', '3'], ['The Grapes of Wrath', '4'], ['The Lord of the Rings', '1'], ['One Hundred Years of Solitude', '1']], 'novels': [['Anna Karenina', '3'], ['To Kill a Mockingbird', '4'], ['The Great Gatsby', '3'], ['One Hundred Years of Solitude', '8'], ['A Passage to India', '4'], ['Invisible Man', '3'], ['Don Quixote', '5'], ['Beloved.', '8']]}
