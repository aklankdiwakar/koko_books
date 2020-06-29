# koko_books
Calculate rental amount for verity of books, based on different story.
# Docker Build command
docker build . -t koko_books:latest
# Docker Run command 
docker run -p 9007:8080 -dit koko_books:latest
# To run test cases
docker run --entrypoint 'nosetests'  -t  koko_books:latest
