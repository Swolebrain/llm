from load_document import load_document_main, delete_index_if_exists
from handle_question_with_added_context import handle_question_with_added_context
import os

index_name = 'seneca-morals-of-a-happy-life'
opensearch_endpoint_url = 'https://search-swolebrain-knn-test-i7upzwkmt52v7filsiswcr4v3y.eu-west-1.es.amazonaws.com'
aws_region = 'eu-west-1'
if not os.environ.get('OPENAI_API_KEY'):
    print("Put the OPENAI_API_KEY in your env vars")
    exit()

#delete_index_if_exists(index_name, opensearch_endpoint_url, aws_region)
#load_document_main(index_name, opensearch_endpoint_url, aws_region)
question = "How do i attain better knowledge of myself?"
result = handle_question_with_added_context(question, index_name, opensearch_endpoint_url, aws_region)
print(f"prompt: {question}, \nanswer:", result)


